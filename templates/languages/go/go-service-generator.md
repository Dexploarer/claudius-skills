---
name: go-service-generator
description: Generate production-ready Go services with best practices. Use when user asks to "create Go service", "generate Go API", or "scaffold Go microservice"
allowed-tools: [Write, Read, Grep, Glob]
---

# Go Service Generator - Idiomatic Go Code

Expert at generating production-ready Go services following Go best practices and idioms.

## When to Use

- "Create a Go HTTP service"
- "Generate Go REST API"
- "Build Go microservice"
- "Scaffold Go gRPC service"

## What This Generates

For a service named `UserService`:

```
user-service/
├── cmd/
│   └── server/
│       └── main.go                 # Entry point
├── internal/
│   ├── handler/
│   │   └── user.go                 # HTTP handlers
│   ├── service/
│   │   └── user.go                 # Business logic
│   ├── repository/
│   │   └── user.go                 # Data access
│   └── model/
│       └── user.go                 # Domain models
├── pkg/
│   └── api/
│       └── user.pb.go              # Generated proto (if gRPC)
├── migrations/
│   └── 001_create_users.sql       # Database migrations
├── go.mod                          # Dependencies
├── go.sum                          # Checksums
├── Makefile                        # Build automation
├── Dockerfile                      # Container image
└── README.md                       # Documentation
```

## Generation Process

### Phase 1: Project Setup

```go
// go.mod
module github.com/username/user-service

go 1.21

require (
    github.com/gorilla/mux v1.8.1
    github.com/lib/pq v1.10.9
    github.com/rs/zerolog v1.31.0
    github.com/golang-migrate/migrate/v4 v4.16.2
)
```

### Phase 2: Domain Model

```go
// internal/model/user.go
package model

import (
    "time"
    "errors"
)

var (
    ErrUserNotFound = errors.New("user not found")
    ErrInvalidEmail = errors.New("invalid email address")
    ErrDuplicateEmail = errors.New("email already exists")
)

// User represents a user in the system
type User struct {
    ID        string    `json:"id" db:"id"`
    Email     string    `json:"email" db:"email"`
    Name      string    `json:"name" db:"name"`
    CreatedAt time.Time `json:"created_at" db:"created_at"`
    UpdatedAt time.Time `json:"updated_at" db:"updated_at"`
}

// Validate validates the user data
func (u *User) Validate() error {
    if u.Email == "" {
        return ErrInvalidEmail
    }
    if u.Name == "" {
        return errors.New("name is required")
    }
    // Add email format validation
    return nil
}

// CreateUserRequest represents a request to create a user
type CreateUserRequest struct {
    Email string `json:"email"`
    Name  string `json:"name"`
}

// UpdateUserRequest represents a request to update a user
type UpdateUserRequest struct {
    Email *string `json:"email,omitempty"`
    Name  *string `json:"name,omitempty"`
}

// ListUsersRequest represents pagination and filtering
type ListUsersRequest struct {
    Page   int    `json:"page"`
    Limit  int    `json:"limit"`
    Search string `json:"search,omitempty"`
}

// ListUsersResponse represents paginated results
type ListUsersResponse struct {
    Users      []User `json:"users"`
    Total      int    `json:"total"`
    Page       int    `json:"page"`
    TotalPages int    `json:"total_pages"`
}
```

### Phase 3: Repository Layer

```go
// internal/repository/user.go
package repository

import (
    "context"
    "database/sql"
    "fmt"

    "github.com/username/user-service/internal/model"
)

// UserRepository defines the interface for user data access
type UserRepository interface {
    Create(ctx context.Context, user *model.User) error
    GetByID(ctx context.Context, id string) (*model.User, error)
    GetByEmail(ctx context.Context, email string) (*model.User, error)
    List(ctx context.Context, req model.ListUsersRequest) (*model.ListUsersResponse, error)
    Update(ctx context.Context, id string, req model.UpdateUserRequest) error
    Delete(ctx context.Context, id string) error
}

// PostgresUserRepository implements UserRepository using PostgreSQL
type PostgresUserRepository struct {
    db *sql.DB
}

// NewPostgresUserRepository creates a new PostgreSQL user repository
func NewPostgresUserRepository(db *sql.DB) *PostgresUserRepository {
    return &PostgresUserRepository{db: db}
}

// Create creates a new user
func (r *PostgresUserRepository) Create(ctx context.Context, user *model.User) error {
    query := `
        INSERT INTO users (id, email, name, created_at, updated_at)
        VALUES ($1, $2, $3, $4, $5)
    `

    _, err := r.db.ExecContext(ctx, query,
        user.ID,
        user.Email,
        user.Name,
        user.CreatedAt,
        user.UpdatedAt,
    )

    if err != nil {
        // Check for duplicate email constraint
        if isDuplicateKeyError(err) {
            return model.ErrDuplicateEmail
        }
        return fmt.Errorf("failed to create user: %w", err)
    }

    return nil
}

// GetByID retrieves a user by ID
func (r *PostgresUserRepository) GetByID(ctx context.Context, id string) (*model.User, error) {
    query := `
        SELECT id, email, name, created_at, updated_at
        FROM users
        WHERE id = $1
    `

    var user model.User
    err := r.db.QueryRowContext(ctx, query, id).Scan(
        &user.ID,
        &user.Email,
        &user.Name,
        &user.CreatedAt,
        &user.UpdatedAt,
    )

    if err == sql.ErrNoRows {
        return nil, model.ErrUserNotFound
    }
    if err != nil {
        return nil, fmt.Errorf("failed to get user: %w", err)
    }

    return &user, nil
}

// GetByEmail retrieves a user by email
func (r *PostgresUserRepository) GetByEmail(ctx context.Context, email string) (*model.User, error) {
    query := `
        SELECT id, email, name, created_at, updated_at
        FROM users
        WHERE email = $1
    `

    var user model.User
    err := r.db.QueryRowContext(ctx, query, email).Scan(
        &user.ID,
        &user.Email,
        &user.Name,
        &user.CreatedAt,
        &user.UpdatedAt,
    )

    if err == sql.ErrNoRows {
        return nil, model.ErrUserNotFound
    }
    if err != nil {
        return nil, fmt.Errorf("failed to get user by email: %w", err)
    }

    return &user, nil
}

// List retrieves paginated users
func (r *PostgresUserRepository) List(ctx context.Context, req model.ListUsersRequest) (*model.ListUsersResponse, error) {
    // Count total
    var total int
    countQuery := `SELECT COUNT(*) FROM users`
    args := []interface{}{}

    if req.Search != "" {
        countQuery += ` WHERE name ILIKE $1 OR email ILIKE $1`
        args = append(args, "%"+req.Search+"%")
    }

    err := r.db.QueryRowContext(ctx, countQuery, args...).Scan(&total)
    if err != nil {
        return nil, fmt.Errorf("failed to count users: %w", err)
    }

    // Get paginated results
    query := `
        SELECT id, email, name, created_at, updated_at
        FROM users
    `

    if req.Search != "" {
        query += ` WHERE name ILIKE $1 OR email ILIKE $1`
    }

    query += ` ORDER BY created_at DESC LIMIT $2 OFFSET $3`

    offset := (req.Page - 1) * req.Limit
    if req.Search != "" {
        args = []interface{}{"%"+req.Search+"%", req.Limit, offset}
    } else {
        args = []interface{}{req.Limit, offset}
    }

    rows, err := r.db.QueryContext(ctx, query, args...)
    if err != nil {
        return nil, fmt.Errorf("failed to list users: %w", err)
    }
    defer rows.Close()

    users := make([]model.User, 0)
    for rows.Next() {
        var user model.User
        err := rows.Scan(
            &user.ID,
            &user.Email,
            &user.Name,
            &user.CreatedAt,
            &user.UpdatedAt,
        )
        if err != nil {
            return nil, fmt.Errorf("failed to scan user: %w", err)
        }
        users = append(users, user)
    }

    totalPages := (total + req.Limit - 1) / req.Limit

    return &model.ListUsersResponse{
        Users:      users,
        Total:      total,
        Page:       req.Page,
        TotalPages: totalPages,
    }, nil
}

// Update updates a user
func (r *PostgresUserRepository) Update(ctx context.Context, id string, req model.UpdateUserRequest) error {
    // Build dynamic query based on what fields are provided
    query := "UPDATE users SET updated_at = NOW()"
    args := []interface{}{}
    argCount := 1

    if req.Email != nil {
        query += fmt.Sprintf(", email = $%d", argCount)
        args = append(args, *req.Email)
        argCount++
    }

    if req.Name != nil {
        query += fmt.Sprintf(", name = $%d", argCount)
        args = append(args, *req.Name)
        argCount++
    }

    query += fmt.Sprintf(" WHERE id = $%d", argCount)
    args = append(args, id)

    result, err := r.db.ExecContext(ctx, query, args...)
    if err != nil {
        if isDuplicateKeyError(err) {
            return model.ErrDuplicateEmail
        }
        return fmt.Errorf("failed to update user: %w", err)
    }

    rows, err := result.RowsAffected()
    if err != nil {
        return fmt.Errorf("failed to get rows affected: %w", err)
    }

    if rows == 0 {
        return model.ErrUserNotFound
    }

    return nil
}

// Delete soft deletes a user
func (r *PostgresUserRepository) Delete(ctx context.Context, id string) error {
    query := `UPDATE users SET deleted_at = NOW() WHERE id = $1 AND deleted_at IS NULL`

    result, err := r.db.ExecContext(ctx, query, id)
    if err != nil {
        return fmt.Errorf("failed to delete user: %w", err)
    }

    rows, err := result.RowsAffected()
    if err != nil {
        return fmt.Errorf("failed to get rows affected: %w", err)
    }

    if rows == 0 {
        return model.ErrUserNotFound
    }

    return nil
}

// Helper function to check for duplicate key errors
func isDuplicateKeyError(err error) bool {
    // PostgreSQL specific error check
    // In production, use pgx or pq driver-specific error types
    return err != nil && (
        // Add proper error checking based on your driver
        false // Placeholder
    )
}
```

### Phase 4: Service Layer

```go
// internal/service/user.go
package service

import (
    "context"
    "fmt"
    "time"

    "github.com/google/uuid"
    "github.com/rs/zerolog/log"

    "github.com/username/user-service/internal/model"
    "github.com/username/user-service/internal/repository"
)

// UserService handles business logic for users
type UserService struct {
    repo repository.UserRepository
}

// NewUserService creates a new user service
func NewUserService(repo repository.UserRepository) *UserService {
    return &UserService{repo: repo}
}

// CreateUser creates a new user
func (s *UserService) CreateUser(ctx context.Context, req model.CreateUserRequest) (*model.User, error) {
    log.Info().
        Str("email", req.Email).
        Msg("creating user")

    // Validate request
    if req.Email == "" || req.Name == "" {
        return nil, fmt.Errorf("email and name are required")
    }

    // Check if email already exists
    existingUser, err := s.repo.GetByEmail(ctx, req.Email)
    if err != nil && err != model.ErrUserNotFound {
        return nil, fmt.Errorf("failed to check existing user: %w", err)
    }
    if existingUser != nil {
        return nil, model.ErrDuplicateEmail
    }

    // Create user
    now := time.Now()
    user := &model.User{
        ID:        uuid.New().String(),
        Email:     req.Email,
        Name:      req.Name,
        CreatedAt: now,
        UpdatedAt: now,
    }

    if err := user.Validate(); err != nil {
        return nil, err
    }

    if err := s.repo.Create(ctx, user); err != nil {
        log.Error().
            Err(err).
            Str("email", req.Email).
            Msg("failed to create user")
        return nil, err
    }

    log.Info().
        Str("user_id", user.ID).
        Str("email", user.Email).
        Msg("user created")

    return user, nil
}

// GetUser retrieves a user by ID
func (s *UserService) GetUser(ctx context.Context, id string) (*model.User, error) {
    return s.repo.GetByID(ctx, id)
}

// ListUsers retrieves paginated users
func (s *UserService) ListUsers(ctx context.Context, req model.ListUsersRequest) (*model.ListUsersResponse, error) {
    // Set defaults
    if req.Page < 1 {
        req.Page = 1
    }
    if req.Limit < 1 || req.Limit > 100 {
        req.Limit = 20
    }

    return s.repo.List(ctx, req)
}

// UpdateUser updates a user
func (s *UserService) UpdateUser(ctx context.Context, id string, req model.UpdateUserRequest) (*model.User, error) {
    log.Info().
        Str("user_id", id).
        Msg("updating user")

    // Check if email is being changed and if it already exists
    if req.Email != nil {
        existingUser, err := s.repo.GetByEmail(ctx, *req.Email)
        if err != nil && err != model.ErrUserNotFound {
            return nil, fmt.Errorf("failed to check existing email: %w", err)
        }
        if existingUser != nil && existingUser.ID != id {
            return nil, model.ErrDuplicateEmail
        }
    }

    if err := s.repo.Update(ctx, id, req); err != nil {
        log.Error().
            Err(err).
            Str("user_id", id).
            Msg("failed to update user")
        return nil, err
    }

    return s.repo.GetByID(ctx, id)
}

// DeleteUser deletes a user
func (s *UserService) DeleteUser(ctx context.Context, id string) error {
    log.Info().
        Str("user_id", id).
        Msg("deleting user")

    return s.repo.Delete(ctx, id)
}
```

### Phase 5: HTTP Handlers

```go
// internal/handler/user.go
package handler

import (
    "encoding/json"
    "net/http"
    "strconv"

    "github.com/gorilla/mux"
    "github.com/rs/zerolog/log"

    "github.com/username/user-service/internal/model"
    "github.com/username/user-service/internal/service"
)

// UserHandler handles HTTP requests for users
type UserHandler struct {
    service *service.UserService
}

// NewUserHandler creates a new user handler
func NewUserHandler(service *service.UserService) *UserHandler {
    return &UserHandler{service: service}
}

// RegisterRoutes registers all user routes
func (h *UserHandler) RegisterRoutes(r *mux.Router) {
    r.HandleFunc("/users", h.ListUsers).Methods("GET")
    r.HandleFunc("/users", h.CreateUser).Methods("POST")
    r.HandleFunc("/users/{id}", h.GetUser).Methods("GET")
    r.HandleFunc("/users/{id}", h.UpdateUser).Methods("PUT")
    r.HandleFunc("/users/{id}", h.DeleteUser).Methods("DELETE")
}

// CreateUser handles POST /users
func (h *UserHandler) CreateUser(w http.ResponseWriter, r *http.Request) {
    var req model.CreateUserRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        respondError(w, http.StatusBadRequest, "invalid request body")
        return
    }

    user, err := h.service.CreateUser(r.Context(), req)
    if err != nil {
        handleServiceError(w, err)
        return
    }

    respondJSON(w, http.StatusCreated, user)
}

// GetUser handles GET /users/{id}
func (h *UserHandler) GetUser(w http.ResponseWriter, r *http.Request) {
    id := mux.Vars(r)["id"]

    user, err := h.service.GetUser(r.Context(), id)
    if err != nil {
        handleServiceError(w, err)
        return
    }

    respondJSON(w, http.StatusOK, user)
}

// ListUsers handles GET /users
func (h *UserHandler) ListUsers(w http.ResponseWriter, r *http.Request) {
    page, _ := strconv.Atoi(r.URL.Query().Get("page"))
    limit, _ := strconv.Atoi(r.URL.Query().Get("limit"))
    search := r.URL.Query().Get("search")

    req := model.ListUsersRequest{
        Page:   page,
        Limit:  limit,
        Search: search,
    }

    response, err := h.service.ListUsers(r.Context(), req)
    if err != nil {
        handleServiceError(w, err)
        return
    }

    respondJSON(w, http.StatusOK, response)
}

// UpdateUser handles PUT /users/{id}
func (h *UserHandler) UpdateUser(w http.ResponseWriter, r *http.Request) {
    id := mux.Vars(r)["id"]

    var req model.UpdateUserRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        respondError(w, http.StatusBadRequest, "invalid request body")
        return
    }

    user, err := h.service.UpdateUser(r.Context(), id, req)
    if err != nil {
        handleServiceError(w, err)
        return
    }

    respondJSON(w, http.StatusOK, user)
}

// DeleteUser handles DELETE /users/{id}
func (h *UserHandler) DeleteUser(w http.ResponseWriter, r *http.Request) {
    id := mux.Vars(r)["id"]

    if err := h.service.DeleteUser(r.Context(), id); err != nil {
        handleServiceError(w, err)
        return
    }

    w.WriteHeader(http.StatusNoContent)
}

// Helper functions
func respondJSON(w http.ResponseWriter, status int, data interface{}) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(status)
    if err := json.NewEncoder(w).Encode(data); err != nil {
        log.Error().Err(err).Msg("failed to encode response")
    }
}

func respondError(w http.ResponseWriter, status int, message string) {
    respondJSON(w, status, map[string]string{"error": message})
}

func handleServiceError(w http.ResponseWriter, err error) {
    switch err {
    case model.ErrUserNotFound:
        respondError(w, http.StatusNotFound, "user not found")
    case model.ErrDuplicateEmail:
        respondError(w, http.StatusConflict, "email already exists")
    case model.ErrInvalidEmail:
        respondError(w, http.StatusBadRequest, "invalid email")
    default:
        log.Error().Err(err).Msg("internal server error")
        respondError(w, http.StatusInternalServerError, "internal server error")
    }
}
```

### Phase 6: Main Entry Point

```go
// cmd/server/main.go
package main

import (
    "context"
    "database/sql"
    "fmt"
    "net/http"
    "os"
    "os/signal"
    "syscall"
    "time"

    "github.com/gorilla/mux"
    _ "github.com/lib/pq"
    "github.com/rs/zerolog"
    "github.com/rs/zerolog/log"

    "github.com/username/user-service/internal/handler"
    "github.com/username/user-service/internal/repository"
    "github.com/username/user-service/internal/service"
)

func main() {
    // Configure logger
    zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
    log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})

    // Load configuration
    cfg := loadConfig()

    // Connect to database
    db, err := sql.Open("postgres", cfg.DatabaseURL)
    if err != nil {
        log.Fatal().Err(err).Msg("failed to connect to database")
    }
    defer db.Close()

    // Verify connection
    if err := db.Ping(); err != nil {
        log.Fatal().Err(err).Msg("failed to ping database")
    }
    log.Info().Msg("connected to database")

    // Initialize layers
    userRepo := repository.NewPostgresUserRepository(db)
    userService := service.NewUserService(userRepo)
    userHandler := handler.NewUserHandler(userService)

    // Setup router
    router := mux.NewRouter()

    // Register routes
    api := router.PathPrefix("/api/v1").Subrouter()
    userHandler.RegisterRoutes(api)

    // Health check
    router.HandleFunc("/health", healthCheck).Methods("GET")

    // Setup server
    srv := &http.Server{
        Addr:         fmt.Sprintf(":%s", cfg.Port),
        Handler:      router,
        ReadTimeout:  15 * time.Second,
        WriteTimeout: 15 * time.Second,
        IdleTimeout:  60 * time.Second,
    }

    // Start server
    go func() {
        log.Info().Str("port", cfg.Port).Msg("starting server")
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            log.Fatal().Err(err).Msg("failed to start server")
        }
    }()

    // Graceful shutdown
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit

    log.Info().Msg("shutting down server...")

    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    if err := srv.Shutdown(ctx); err != nil {
        log.Fatal().Err(err).Msg("server forced to shutdown")
    }

    log.Info().Msg("server exited")
}

type config struct {
    Port        string
    DatabaseURL string
}

func loadConfig() config {
    return config{
        Port:        getEnv("PORT", "8080"),
        DatabaseURL: getEnv("DATABASE_URL", "postgres://localhost/userdb?sslmode=disable"),
    }
}

func getEnv(key, fallback string) string {
    if value := os.Getenv(key); value != "" {
        return value
    }
    return fallback
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("OK"))
}
```

### Phase 7: Tests

```go
// internal/service/user_test.go
package service_test

import (
    "context"
    "testing"

    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/mock"

    "github.com/username/user-service/internal/model"
    "github.com/username/user-service/internal/service"
)

// MockUserRepository is a mock implementation
type MockUserRepository struct {
    mock.Mock
}

func (m *MockUserRepository) Create(ctx context.Context, user *model.User) error {
    args := m.Called(ctx, user)
    return args.Error(0)
}

func (m *MockUserRepository) GetByID(ctx context.Context, id string) (*model.User, error) {
    args := m.Called(ctx, id)
    if args.Get(0) == nil {
        return nil, args.Error(1)
    }
    return args.Get(0).(*model.User), args.Error(1)
}

func (m *MockUserRepository) GetByEmail(ctx context.Context, email string) (*model.User, error) {
    args := m.Called(ctx, email)
    if args.Get(0) == nil {
        return nil, args.Error(1)
    }
    return args.Get(0).(*model.User), args.Error(1)
}

// Add other methods...

func TestCreateUser(t *testing.T) {
    mockRepo := new(MockUserRepository)
    userService := service.NewUserService(mockRepo)

    ctx := context.Background()
    req := model.CreateUserRequest{
        Email: "test@example.com",
        Name:  "Test User",
    }

    // Mock: Email doesn't exist
    mockRepo.On("GetByEmail", ctx, req.Email).Return(nil, model.ErrUserNotFound)

    // Mock: Create succeeds
    mockRepo.On("Create", ctx, mock.AnythingOfType("*model.User")).Return(nil)

    user, err := userService.CreateUser(ctx, req)

    assert.NoError(t, err)
    assert.NotNil(t, user)
    assert.Equal(t, req.Email, user.Email)
    assert.Equal(t, req.Name, user.Name)
    assert.NotEmpty(t, user.ID)

    mockRepo.AssertExpectations(t)
}

func TestCreateUser_DuplicateEmail(t *testing.T) {
    mockRepo := new(MockUserRepository)
    userService := service.NewUserService(mockRepo)

    ctx := context.Background()
    req := model.CreateUserRequest{
        Email: "existing@example.com",
        Name:  "Test User",
    }

    existingUser := &model.User{ID: "123", Email: req.Email}

    // Mock: Email already exists
    mockRepo.On("GetByEmail", ctx, req.Email).Return(existingUser, nil)

    user, err := userService.CreateUser(ctx, req)

    assert.Error(t, err)
    assert.Equal(t, model.ErrDuplicateEmail, err)
    assert.Nil(t, user)

    mockRepo.AssertExpectations(t)
}
```

### Phase 8: Build Tools

```makefile
# Makefile
.PHONY: build test run docker-build docker-run clean

APP_NAME=user-service
VERSION?=latest

build:
	@echo "Building..."
	go build -o bin/$(APP_NAME) cmd/server/main.go

test:
	@echo "Running tests..."
	go test -v -race -coverprofile=coverage.out ./...
	go tool cover -html=coverage.out -o coverage.html

run:
	@echo "Running..."
	go run cmd/server/main.go

docker-build:
	@echo "Building Docker image..."
	docker build -t $(APP_NAME):$(VERSION) .

docker-run:
	@echo "Running Docker container..."
	docker run -p 8080:8080 --env-file .env $(APP_NAME):$(VERSION)

clean:
	@echo "Cleaning..."
	rm -rf bin/
	rm -f coverage.out coverage.html

lint:
	@echo "Linting..."
	golangci-lint run

migrate-up:
	@echo "Running migrations..."
	migrate -path migrations -database "$(DATABASE_URL)" up

migrate-down:
	@echo "Reverting migrations..."
	migrate -path migrations -database "$(DATABASE_URL)" down 1

.DEFAULT_GOAL := build
```

```dockerfile
# Dockerfile
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source
COPY . .

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server cmd/server/main.go

# Runtime image
FROM alpine:latest

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /app/server .
COPY migrations ./migrations

EXPOSE 8080

CMD ["./server"]
```

## Go Best Practices Implemented

✅ **Project Structure**
- Standard Go project layout
- `internal/` for private packages
- `pkg/` for public packages
- `cmd/` for entry points

✅ **Error Handling**
- Explicit error returns
- Error wrapping with `fmt.Errorf`
- Custom error types
- No panics in production code

✅ **Interfaces**
- Repository interface for testability
- Small, focused interfaces
- Interface segregation

✅ **Concurrency**
- Context propagation
- Graceful shutdown
- Timeout handling

✅ **Testing**
- Table-driven tests
- Mocks for dependencies
- High test coverage
- Benchmark tests

✅ **Performance**
- Efficient database queries
- Connection pooling
- Proper resource cleanup
- Memory-efficient code

## Notes

- Uses standard library where possible
- Minimal external dependencies
- Production-ready error handling
- Idiomatic Go code
- Follows Go conventions and style guide
