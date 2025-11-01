---
name: rust-service-generator
description: Generate production-ready Rust web services with async/await, database integration, and best practices
allowed-tools: [Read, Write, Edit, Grep, Glob]
---

# Rust Service Generator

Generate complete, production-ready Rust web services following Rust best practices and idiomatic patterns.

## What This Skill Creates

A complete Rust service with:
- ✅ Axum web framework (async, ergonomic)
- ✅ SQLx for database operations (compile-time checked)
- ✅ Repository pattern with traits
- ✅ Service layer with business logic
- ✅ Custom error types with thiserror
- ✅ Async/await throughout
- ✅ Comprehensive tests with tokio::test
- ✅ Cargo workspace structure
- ✅ Docker multi-stage build
- ✅ Logging with tracing
- ✅ Configuration management
- ✅ Health checks and metrics

## Usage

```
"Generate a Rust service for managing users with CRUD operations"
"Create a Rust API service for products with PostgreSQL"
"Build a Rust microservice for orders with authentication"
```

## Project Structure

The generated service follows standard Rust project layout:

```
my-service/
├── Cargo.toml              # Workspace configuration
├── Cargo.lock              # Dependency lock file
├── .env.example            # Environment variables template
├── Dockerfile              # Multi-stage build
├── docker-compose.yml      # Local development setup
├── migrations/             # Database migrations (SQLx)
│   └── 20240101000000_create_users.sql
├── src/
│   ├── main.rs            # Application entry point
│   ├── lib.rs             # Library exports
│   ├── config.rs          # Configuration management
│   ├── error.rs           # Custom error types
│   ├── domain/            # Domain models
│   │   ├── mod.rs
│   │   └── user.rs
│   ├── repository/        # Data access layer
│   │   ├── mod.rs
│   │   └── user_repository.rs
│   ├── service/           # Business logic layer
│   │   ├── mod.rs
│   │   └── user_service.rs
│   ├── handler/           # HTTP handlers
│   │   ├── mod.rs
│   │   ├── user_handler.rs
│   │   └── health.rs
│   └── routes.rs          # Route definitions
└── tests/
    ├── integration_test.rs
    └── common/
        └── mod.rs
```

## Instructions for Claude

When the user requests a Rust service generation:

### Step 1: Gather Requirements

Ask for:
1. **Service name**: What should the service be called?
2. **Resource**: What entity to manage (e.g., users, products, orders)?
3. **Database**: PostgreSQL (default), MySQL, or SQLite?
4. **Additional features**: Authentication? Caching? Message queue?

### Step 2: Create Project Structure

```bash
cargo new --lib {service-name}
cd {service-name}
mkdir -p src/{domain,repository,service,handler} tests/common migrations
```

### Step 3: Generate Cargo.toml

Create a comprehensive `Cargo.toml` with all dependencies:

```toml
[package]
name = "{service-name}"
version = "0.1.0"
edition = "2021"

[lib]
path = "src/lib.rs"

[[bin]]
name = "{service-name}"
path = "src/main.rs"

[dependencies]
# Web framework
axum = { version = "0.7", features = ["macros"] }
tokio = { version = "1", features = ["full"] }
tower = "0.4"
tower-http = { version = "0.5", features = ["cors", "trace", "compression-full"] }

# Database
sqlx = { version = "0.7", features = ["runtime-tokio", "postgres", "uuid", "chrono", "migrate"] }

# Serialization
serde = { version = "1", features = ["derive"] }
serde_json = "1"

# Error handling
thiserror = "1"
anyhow = "1"

# Logging and tracing
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter", "json"] }

# Validation
validator = { version = "0.18", features = ["derive"] }

# UUID and time
uuid = { version = "1", features = ["v4", "serde"] }
chrono = { version = "0.4", features = ["serde"] }

# Configuration
config = "0.14"
dotenvy = "0.15"

# Security
argon2 = "0.5"  # For password hashing
jsonwebtoken = "9"  # For JWT

[dev-dependencies]
tokio-test = "0.4"
mockall = "0.12"
reqwest = { version = "0.11", features = ["json"] }
```

### Step 4: Create Domain Models

Generate `src/domain/{resource}.rs`:

**Example for User resource:**

```rust
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use sqlx::FromRow;
use uuid::Uuid;
use validator::Validate;

/// User entity - represents a user in the system
#[derive(Debug, Clone, Serialize, Deserialize, FromRow)]
pub struct User {
    pub id: Uuid,
    pub email: String,
    pub name: String,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

/// Request to create a new user
#[derive(Debug, Deserialize, Validate)]
pub struct CreateUserRequest {
    #[validate(email(message = "Invalid email format"))]
    pub email: String,

    #[validate(length(min = 1, max = 100, message = "Name must be 1-100 characters"))]
    pub name: String,
}

/// Request to update an existing user
#[derive(Debug, Deserialize, Validate)]
pub struct UpdateUserRequest {
    #[validate(email(message = "Invalid email format"))]
    pub email: Option<String>,

    #[validate(length(min = 1, max = 100, message = "Name must be 1-100 characters"))]
    pub name: Option<String>,
}

/// Request for listing users with pagination
#[derive(Debug, Deserialize, Validate)]
pub struct ListUsersRequest {
    #[validate(range(min = 1, max = 100))]
    #[serde(default = "default_limit")]
    pub limit: i64,

    #[validate(range(min = 0))]
    #[serde(default)]
    pub offset: i64,

    pub search: Option<String>,
}

fn default_limit() -> i64 {
    20
}

/// Response for list operations
#[derive(Debug, Serialize)]
pub struct ListUsersResponse {
    pub users: Vec<User>,
    pub total: i64,
    pub limit: i64,
    pub offset: i64,
}

impl User {
    /// Create a new user with generated ID and timestamps
    pub fn new(email: String, name: String) -> Self {
        let now = Utc::now();
        Self {
            id: Uuid::new_v4(),
            email,
            name,
            created_at: now,
            updated_at: now,
        }
    }
}
```

Create `src/domain/mod.rs`:

```rust
pub mod user;

pub use user::{
    CreateUserRequest, ListUsersRequest, ListUsersResponse, UpdateUserRequest, User,
};
```

### Step 5: Create Custom Error Types

Generate `src/error.rs`:

```rust
use axum::{
    http::StatusCode,
    response::{IntoResponse, Response},
    Json,
};
use serde_json::json;
use thiserror::Error;

/// Application error types
#[derive(Error, Debug)]
pub enum AppError {
    #[error("Resource not found: {0}")]
    NotFound(String),

    #[error("Duplicate resource: {0}")]
    Duplicate(String),

    #[error("Validation error: {0}")]
    Validation(String),

    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),

    #[error("Internal server error")]
    Internal(#[from] anyhow::Error),

    #[error("Unauthorized")]
    Unauthorized,

    #[error("Forbidden")]
    Forbidden,
}

/// Custom result type for the application
pub type Result<T> = std::result::Result<T, AppError>;

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let (status, error_message) = match self {
            AppError::NotFound(msg) => (StatusCode::NOT_FOUND, msg),
            AppError::Duplicate(msg) => (StatusCode::CONFLICT, msg),
            AppError::Validation(msg) => (StatusCode::BAD_REQUEST, msg),
            AppError::Database(ref e) => {
                tracing::error!("Database error: {:?}", e);
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    "Database error occurred".to_string(),
                )
            }
            AppError::Internal(ref e) => {
                tracing::error!("Internal error: {:?}", e);
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    "Internal server error".to_string(),
                )
            }
            AppError::Unauthorized => (StatusCode::UNAUTHORIZED, "Unauthorized".to_string()),
            AppError::Forbidden => (StatusCode::FORBIDDEN, "Forbidden".to_string()),
        };

        let body = Json(json!({
            "error": error_message,
        }));

        (status, body).into_response()
    }
}

/// Helper to convert validation errors
impl From<validator::ValidationErrors> for AppError {
    fn from(errors: validator::ValidationErrors) -> Self {
        AppError::Validation(errors.to_string())
    }
}
```

### Step 6: Create Repository Layer

Generate `src/repository/{resource}_repository.rs`:

**Example for User repository:**

```rust
use async_trait::async_trait;
use sqlx::{PgPool, Postgres, QueryBuilder};
use uuid::Uuid;

use crate::{
    domain::{CreateUserRequest, ListUsersRequest, ListUsersResponse, UpdateUserRequest, User},
    error::{AppError, Result},
};

/// Repository trait for user operations
#[async_trait]
pub trait UserRepository: Send + Sync {
    async fn create(&self, req: CreateUserRequest) -> Result<User>;
    async fn get_by_id(&self, id: Uuid) -> Result<User>;
    async fn get_by_email(&self, email: &str) -> Result<Option<User>>;
    async fn list(&self, req: ListUsersRequest) -> Result<ListUsersResponse>;
    async fn update(&self, id: Uuid, req: UpdateUserRequest) -> Result<User>;
    async fn delete(&self, id: Uuid) -> Result<()>;
}

/// PostgreSQL implementation of UserRepository
pub struct PostgresUserRepository {
    pool: PgPool,
}

impl PostgresUserRepository {
    pub fn new(pool: PgPool) -> Self {
        Self { pool }
    }
}

#[async_trait]
impl UserRepository for PostgresUserRepository {
    async fn create(&self, req: CreateUserRequest) -> Result<User> {
        let user = User::new(req.email, req.name);

        let result = sqlx::query_as::<_, User>(
            r#"
            INSERT INTO users (id, email, name, created_at, updated_at)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING id, email, name, created_at, updated_at
            "#,
        )
        .bind(&user.id)
        .bind(&user.email)
        .bind(&user.name)
        .bind(&user.created_at)
        .bind(&user.updated_at)
        .fetch_one(&self.pool)
        .await;

        match result {
            Ok(user) => Ok(user),
            Err(sqlx::Error::Database(db_err)) if is_unique_violation(&db_err) => {
                Err(AppError::Duplicate(format!(
                    "User with email {} already exists",
                    user.email
                )))
            }
            Err(e) => Err(AppError::Database(e)),
        }
    }

    async fn get_by_id(&self, id: Uuid) -> Result<User> {
        let user = sqlx::query_as::<_, User>(
            r#"
            SELECT id, email, name, created_at, updated_at
            FROM users
            WHERE id = $1
            "#,
        )
        .bind(id)
        .fetch_optional(&self.pool)
        .await?;

        user.ok_or_else(|| AppError::NotFound(format!("User with ID {} not found", id)))
    }

    async fn get_by_email(&self, email: &str) -> Result<Option<User>> {
        let user = sqlx::query_as::<_, User>(
            r#"
            SELECT id, email, name, created_at, updated_at
            FROM users
            WHERE email = $1
            "#,
        )
        .bind(email)
        .fetch_optional(&self.pool)
        .await?;

        Ok(user)
    }

    async fn list(&self, req: ListUsersRequest) -> Result<ListUsersResponse> {
        let mut query_builder: QueryBuilder<Postgres> = QueryBuilder::new(
            "SELECT id, email, name, created_at, updated_at FROM users WHERE 1=1"
        );

        // Add search filter if provided
        if let Some(search) = &req.search {
            query_builder.push(" AND (name ILIKE ");
            query_builder.push_bind(format!("%{}%", search));
            query_builder.push(" OR email ILIKE ");
            query_builder.push_bind(format!("%{}%", search));
            query_builder.push(")");
        }

        query_builder.push(" ORDER BY created_at DESC");
        query_builder.push(" LIMIT ");
        query_builder.push_bind(req.limit);
        query_builder.push(" OFFSET ");
        query_builder.push_bind(req.offset);

        let users = query_builder
            .build_query_as::<User>()
            .fetch_all(&self.pool)
            .await?;

        // Get total count
        let total: (i64,) = sqlx::query_as("SELECT COUNT(*) FROM users")
            .fetch_one(&self.pool)
            .await?;

        Ok(ListUsersResponse {
            users,
            total: total.0,
            limit: req.limit,
            offset: req.offset,
        })
    }

    async fn update(&self, id: Uuid, req: UpdateUserRequest) -> Result<User> {
        let mut query_builder: QueryBuilder<Postgres> = QueryBuilder::new("UPDATE users SET ");
        let mut separated = query_builder.separated(", ");

        if let Some(email) = &req.email {
            separated.push("email = ");
            separated.push_bind_unseparated(email);
        }

        if let Some(name) = &req.name {
            separated.push("name = ");
            separated.push_bind_unseparated(name);
        }

        separated.push("updated_at = NOW()");

        query_builder.push(" WHERE id = ");
        query_builder.push_bind(id);
        query_builder.push(" RETURNING id, email, name, created_at, updated_at");

        let user = query_builder
            .build_query_as::<User>()
            .fetch_optional(&self.pool)
            .await?;

        user.ok_or_else(|| AppError::NotFound(format!("User with ID {} not found", id)))
    }

    async fn delete(&self, id: Uuid) -> Result<()> {
        let result = sqlx::query("DELETE FROM users WHERE id = $1")
            .bind(id)
            .execute(&self.pool)
            .await?;

        if result.rows_affected() == 0 {
            return Err(AppError::NotFound(format!("User with ID {} not found", id)));
        }

        Ok(())
    }
}

/// Helper to check if error is a unique constraint violation
fn is_unique_violation(db_err: &sqlx::error::DatabaseError) -> bool {
    db_err.code().as_deref() == Some("23505")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_user_repository() {
        // Integration tests would go here
        // Requires test database setup
    }
}
```

Create `src/repository/mod.rs`:

```rust
pub mod user_repository;

pub use user_repository::{PostgresUserRepository, UserRepository};
```

### Step 7: Create Service Layer

Generate `src/service/{resource}_service.rs`:

```rust
use std::sync::Arc;
use validator::Validate;

use crate::{
    domain::{CreateUserRequest, ListUsersRequest, ListUsersResponse, UpdateUserRequest, User},
    error::{AppError, Result},
    repository::UserRepository,
};

/// Service for user business logic
pub struct UserService {
    repository: Arc<dyn UserRepository>,
}

impl UserService {
    pub fn new(repository: Arc<dyn UserRepository>) -> Self {
        Self { repository }
    }

    /// Create a new user
    pub async fn create_user(&self, req: CreateUserRequest) -> Result<User> {
        // Validate input
        req.validate()?;

        // Check if user already exists
        if let Some(_existing) = self.repository.get_by_email(&req.email).await? {
            return Err(AppError::Duplicate(format!(
                "User with email {} already exists",
                req.email
            )));
        }

        // Create user
        let user = self.repository.create(req).await?;

        tracing::info!("Created user: {}", user.id);
        Ok(user)
    }

    /// Get user by ID
    pub async fn get_user(&self, id: uuid::Uuid) -> Result<User> {
        self.repository.get_by_id(id).await
    }

    /// List users with pagination and search
    pub async fn list_users(&self, req: ListUsersRequest) -> Result<ListUsersResponse> {
        req.validate()?;
        self.repository.list(req).await
    }

    /// Update user
    pub async fn update_user(&self, id: uuid::Uuid, req: UpdateUserRequest) -> Result<User> {
        req.validate()?;

        // Check if email is being changed to one that already exists
        if let Some(new_email) = &req.email {
            if let Some(existing) = self.repository.get_by_email(new_email).await? {
                if existing.id != id {
                    return Err(AppError::Duplicate(format!(
                        "User with email {} already exists",
                        new_email
                    )));
                }
            }
        }

        let user = self.repository.update(id, req).await?;
        tracing::info!("Updated user: {}", user.id);
        Ok(user)
    }

    /// Delete user
    pub async fn delete_user(&self, id: uuid::Uuid) -> Result<()> {
        self.repository.delete(id).await?;
        tracing::info!("Deleted user: {}", id);
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use mockall::predicate::*;
    use mockall::mock;

    mock! {
        pub UserRepo {}

        #[async_trait::async_trait]
        impl UserRepository for UserRepo {
            async fn create(&self, req: CreateUserRequest) -> Result<User>;
            async fn get_by_id(&self, id: uuid::Uuid) -> Result<User>;
            async fn get_by_email(&self, email: &str) -> Result<Option<User>>;
            async fn list(&self, req: ListUsersRequest) -> Result<ListUsersResponse>;
            async fn update(&self, id: uuid::Uuid, req: UpdateUserRequest) -> Result<User>;
            async fn delete(&self, id: uuid::Uuid) -> Result<()>;
        }
    }

    #[tokio::test]
    async fn test_create_user_success() {
        let mut mock_repo = MockUserRepo::new();
        let expected_user = User::new("test@example.com".to_string(), "Test User".to_string());
        let expected_clone = expected_user.clone();

        mock_repo
            .expect_get_by_email()
            .with(eq("test@example.com"))
            .times(1)
            .returning(|_| Ok(None));

        mock_repo
            .expect_create()
            .times(1)
            .returning(move |_| Ok(expected_clone.clone()));

        let service = UserService::new(Arc::new(mock_repo));
        let req = CreateUserRequest {
            email: "test@example.com".to_string(),
            name: "Test User".to_string(),
        };

        let result = service.create_user(req).await;
        assert!(result.is_ok());
    }

    #[tokio::test]
    async fn test_create_user_duplicate_email() {
        let mut mock_repo = MockUserRepo::new();
        let existing_user = User::new("test@example.com".to_string(), "Existing".to_string());

        mock_repo
            .expect_get_by_email()
            .with(eq("test@example.com"))
            .times(1)
            .returning(move |_| Ok(Some(existing_user.clone())));

        let service = UserService::new(Arc::new(mock_repo));
        let req = CreateUserRequest {
            email: "test@example.com".to_string(),
            name: "Test User".to_string(),
        };

        let result = service.create_user(req).await;
        assert!(matches!(result, Err(AppError::Duplicate(_))));
    }
}
```

Create `src/service/mod.rs`:

```rust
pub mod user_service;

pub use user_service::UserService;
```

### Step 8: Create HTTP Handlers

Generate `src/handler/{resource}_handler.rs`:

```rust
use axum::{
    extract::{Path, Query, State},
    http::StatusCode,
    Json,
};
use uuid::Uuid;

use crate::{
    domain::{CreateUserRequest, ListUsersRequest, UpdateUserRequest, User},
    error::Result,
    service::UserService,
};
use std::sync::Arc;

/// Application state shared across handlers
#[derive(Clone)]
pub struct AppState {
    pub user_service: Arc<UserService>,
}

/// Create a new user
///
/// POST /api/users
pub async fn create_user(
    State(state): State<AppState>,
    Json(req): Json<CreateUserRequest>,
) -> Result<(StatusCode, Json<User>)> {
    let user = state.user_service.create_user(req).await?;
    Ok((StatusCode::CREATED, Json(user)))
}

/// Get user by ID
///
/// GET /api/users/:id
pub async fn get_user(
    State(state): State<AppState>,
    Path(id): Path<Uuid>,
) -> Result<Json<User>> {
    let user = state.user_service.get_user(id).await?;
    Ok(Json(user))
}

/// List users with pagination
///
/// GET /api/users?limit=20&offset=0&search=john
pub async fn list_users(
    State(state): State<AppState>,
    Query(req): Query<ListUsersRequest>,
) -> Result<Json<crate::domain::ListUsersResponse>> {
    let response = state.user_service.list_users(req).await?;
    Ok(Json(response))
}

/// Update user
///
/// PUT /api/users/:id
pub async fn update_user(
    State(state): State<AppState>,
    Path(id): Path<Uuid>,
    Json(req): Json<UpdateUserRequest>,
) -> Result<Json<User>> {
    let user = state.user_service.update_user(id, req).await?;
    Ok(Json(user))
}

/// Delete user
///
/// DELETE /api/users/:id
pub async fn delete_user(
    State(state): State<AppState>,
    Path(id): Path<Uuid>,
) -> Result<StatusCode> {
    state.user_service.delete_user(id).await?;
    Ok(StatusCode::NO_CONTENT)
}

#[cfg(test)]
mod tests {
    use super::*;
    use axum::http::Request;
    use tower::ServiceExt;

    // Handler tests would go here
}
```

Create `src/handler/health.rs`:

```rust
use axum::{http::StatusCode, Json};
use serde_json::{json, Value};

/// Health check endpoint
///
/// GET /health
pub async fn health_check() -> (StatusCode, Json<Value>) {
    (
        StatusCode::OK,
        Json(json!({
            "status": "healthy",
            "service": env!("CARGO_PKG_NAME"),
            "version": env!("CARGO_PKG_VERSION"),
        })),
    )
}

/// Readiness check endpoint
///
/// GET /ready
pub async fn readiness_check() -> (StatusCode, Json<Value>) {
    // Add database connectivity check, etc.
    (
        StatusCode::OK,
        Json(json!({
            "ready": true,
        })),
    )
}
```

Create `src/handler/mod.rs`:

```rust
pub mod health;
pub mod user_handler;

pub use user_handler::AppState;
```

### Step 9: Create Routes

Generate `src/routes.rs`:

```rust
use axum::{
    routing::{delete, get, post, put},
    Router,
};
use tower_http::{
    cors::CorsLayer,
    trace::{DefaultMakeSpan, DefaultOnResponse, TraceLayer},
    compression::CompressionLayer,
};
use tracing::Level;

use crate::handler::{health, user_handler, AppState};

/// Build the application router with all routes
pub fn create_router(state: AppState) -> Router {
    // API routes
    let api_routes = Router::new()
        .route("/users", post(user_handler::create_user))
        .route("/users", get(user_handler::list_users))
        .route("/users/:id", get(user_handler::get_user))
        .route("/users/:id", put(user_handler::update_user))
        .route("/users/:id", delete(user_handler::delete_user));

    // Health routes
    let health_routes = Router::new()
        .route("/health", get(health::health_check))
        .route("/ready", get(health::readiness_check));

    // Combine all routes
    Router::new()
        .nest("/api", api_routes)
        .merge(health_routes)
        .layer(
            TraceLayer::new_for_http()
                .make_span_with(DefaultMakeSpan::new().level(Level::INFO))
                .on_response(DefaultOnResponse::new().level(Level::INFO)),
        )
        .layer(CompressionLayer::new())
        .layer(CorsLayer::permissive()) // Configure appropriately for production
        .with_state(state)
}
```

### Step 10: Create Configuration

Generate `src/config.rs`:

```rust
use serde::Deserialize;

#[derive(Debug, Deserialize, Clone)]
pub struct Config {
    pub server: ServerConfig,
    pub database: DatabaseConfig,
}

#[derive(Debug, Deserialize, Clone)]
pub struct ServerConfig {
    #[serde(default = "default_host")]
    pub host: String,

    #[serde(default = "default_port")]
    pub port: u16,
}

#[derive(Debug, Deserialize, Clone)]
pub struct DatabaseConfig {
    pub url: String,

    #[serde(default = "default_max_connections")]
    pub max_connections: u32,
}

fn default_host() -> String {
    "0.0.0.0".to_string()
}

fn default_port() -> u16 {
    8080
}

fn default_max_connections() -> u32 {
    10
}

impl Config {
    pub fn from_env() -> Result<Self, config::ConfigError> {
        let config = config::Config::builder()
            .add_source(config::Environment::default().separator("__"))
            .build()?;

        config.try_deserialize()
    }
}
```

### Step 11: Create Main Application

Generate `src/main.rs`:

```rust
use anyhow::Context;
use sqlx::postgres::PgPoolOptions;
use std::sync::Arc;
use tokio::signal;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

use {service_name}::{
    config::Config,
    handler::AppState,
    repository::PostgresUserRepository,
    routes::create_router,
    service::UserService,
};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // Initialize tracing
    tracing_subscriber::registry()
        .with(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "info".into()),
        )
        .with(tracing_subscriber::fmt::layer())
        .init();

    // Load configuration
    dotenvy::dotenv().ok();
    let config = Config::from_env().context("Failed to load configuration")?;

    tracing::info!("Starting {} v{}", env!("CARGO_PKG_NAME"), env!("CARGO_PKG_VERSION"));

    // Create database connection pool
    let pool = PgPoolOptions::new()
        .max_connections(config.database.max_connections)
        .connect(&config.database.url)
        .await
        .context("Failed to connect to database")?;

    // Run migrations
    sqlx::migrate!("./migrations")
        .run(&pool)
        .await
        .context("Failed to run migrations")?;

    tracing::info!("Database migrations completed");

    // Initialize dependencies
    let user_repository = Arc::new(PostgresUserRepository::new(pool.clone()));
    let user_service = Arc::new(UserService::new(user_repository));

    // Create application state
    let state = AppState { user_service };

    // Build router
    let app = create_router(state);

    // Start server
    let addr = format!("{}:{}", config.server.host, config.server.port);
    let listener = tokio::net::TcpListener::bind(&addr)
        .await
        .context("Failed to bind to address")?;

    tracing::info!("Server listening on {}", addr);

    axum::serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await
        .context("Server error")?;

    Ok(())
}

/// Wait for shutdown signal
async fn shutdown_signal() {
    let ctrl_c = async {
        signal::ctrl_c()
            .await
            .expect("Failed to install Ctrl+C handler");
    };

    #[cfg(unix)]
    let terminate = async {
        signal::unix::signal(signal::unix::SignalKind::terminate())
            .expect("Failed to install signal handler")
            .recv()
            .await;
    };

    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();

    tokio::select! {
        _ = ctrl_c => {},
        _ = terminate => {},
    }

    tracing::info!("Shutdown signal received, starting graceful shutdown");
}
```

Generate `src/lib.rs`:

```rust
pub mod config;
pub mod domain;
pub mod error;
pub mod handler;
pub mod repository;
pub mod routes;
pub mod service;
```

### Step 12: Create Database Migration

Generate `migrations/20240101000000_create_users.sql`:

```sql
-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create index on email for faster lookups
CREATE INDEX idx_users_email ON users(email);

-- Create index on created_at for sorting
CREATE INDEX idx_users_created_at ON users(created_at DESC);
```

### Step 13: Create Docker Configuration

Generate `Dockerfile`:

```dockerfile
# Build stage
FROM rust:1.75-slim as builder

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy manifests
COPY Cargo.toml Cargo.lock ./

# Copy source
COPY src ./src
COPY migrations ./migrations

# Build for release
RUN cargo build --release

# Runtime stage
FROM debian:bookworm-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

# Copy binary from builder
COPY --from=builder /app/target/release/{service-name} /usr/local/bin/app

# Copy migrations
COPY --from=builder /app/migrations ./migrations

# Create non-root user
RUN useradd -m -u 1001 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["app"]
```

Generate `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      SERVER__HOST: 0.0.0.0
      SERVER__PORT: 8080
      DATABASE__URL: postgresql://postgres:postgres@db:5432/myservice
      DATABASE__MAX_CONNECTIONS: 10
      RUST_LOG: info
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: myservice
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

### Step 14: Create Environment Configuration

Generate `.env.example`:

```bash
# Server Configuration
SERVER__HOST=0.0.0.0
SERVER__PORT=8080

# Database Configuration
DATABASE__URL=postgresql://postgres:postgres@localhost:5432/myservice
DATABASE__MAX_CONNECTIONS=10

# Logging
RUST_LOG=info
```

### Step 15: Create Tests

Generate `tests/integration_test.rs`:

```rust
use reqwest;
use serde_json::json;

#[tokio::test]
async fn test_health_endpoint() {
    let client = reqwest::Client::new();
    let response = client
        .get("http://localhost:8080/health")
        .send()
        .await
        .expect("Failed to send request");

    assert_eq!(response.status(), 200);
    let body: serde_json::Value = response.json().await.expect("Failed to parse JSON");
    assert_eq!(body["status"], "healthy");
}

#[tokio::test]
async fn test_create_and_get_user() {
    let client = reqwest::Client::new();

    // Create user
    let create_response = client
        .post("http://localhost:8080/api/users")
        .json(&json!({
            "email": "test@example.com",
            "name": "Test User"
        }))
        .send()
        .await
        .expect("Failed to create user");

    assert_eq!(create_response.status(), 201);
    let created_user: serde_json::Value = create_response.json().await.unwrap();
    let user_id = created_user["id"].as_str().unwrap();

    // Get user
    let get_response = client
        .get(&format!("http://localhost:8080/api/users/{}", user_id))
        .send()
        .await
        .expect("Failed to get user");

    assert_eq!(get_response.status(), 200);
    let user: serde_json::Value = get_response.json().await.unwrap();
    assert_eq!(user["email"], "test@example.com");
    assert_eq!(user["name"], "Test User");
}
```

### Step 16: Create Makefile

Generate `Makefile`:

```makefile
.PHONY: help dev test build docker-build docker-up docker-down clean migrate

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

dev: ## Run in development mode
	cargo watch -x run

test: ## Run tests
	cargo test

test-integration: ## Run integration tests
	cargo test --test '*'

build: ## Build release binary
	cargo build --release

docker-build: ## Build Docker image
	docker build -t {service-name}:latest .

docker-up: ## Start services with Docker Compose
	docker-compose up -d

docker-down: ## Stop Docker Compose services
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

migrate: ## Run database migrations
	sqlx migrate run

migrate-revert: ## Revert last migration
	sqlx migrate revert

clean: ## Clean build artifacts
	cargo clean
	docker-compose down -v

fmt: ## Format code
	cargo fmt

lint: ## Run clippy
	cargo clippy -- -D warnings

check: fmt lint test ## Run all checks
```

### Step 17: Create README

Generate `README.md`:

```markdown
# {Service Name}

Production-ready Rust web service built with Axum and SQLx.

## Features

- ✅ Async/await with Tokio
- ✅ Axum web framework
- ✅ SQLx with PostgreSQL
- ✅ Repository pattern
- ✅ Service layer
- ✅ Custom error handling
- ✅ Request validation
- ✅ Structured logging with tracing
- ✅ Docker support
- ✅ Database migrations
- ✅ Health checks
- ✅ Graceful shutdown

## Quick Start

### Prerequisites

- Rust 1.75+
- PostgreSQL 14+
- Docker (optional)

### Development

1. **Clone and setup:**
   ```bash
   cp .env.example .env
   # Edit .env with your database URL
   ```

2. **Run PostgreSQL:**
   ```bash
   docker-compose up -d db
   ```

3. **Run migrations:**
   ```bash
   make migrate
   ```

4. **Start server:**
   ```bash
   make dev
   ```

### Docker

```bash
# Build and run with Docker Compose
make docker-build
make docker-up

# View logs
make docker-logs

# Stop services
make docker-down
```

## API Endpoints

### Health
- `GET /health` - Health check
- `GET /ready` - Readiness check

### Users
- `POST /api/users` - Create user
- `GET /api/users` - List users (with pagination)
- `GET /api/users/:id` - Get user by ID
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

## Testing

```bash
# Unit tests
make test

# Integration tests (requires running server)
make test-integration
```

## Project Structure

```
src/
├── main.rs              # Application entry point
├── lib.rs               # Library exports
├── config.rs            # Configuration
├── error.rs             # Error types
├── routes.rs            # Route definitions
├── domain/              # Domain models
├── repository/          # Data access layer
├── service/             # Business logic
└── handler/             # HTTP handlers
```

## Configuration

Environment variables (prefix with `__` for nested config):

- `SERVER__HOST` - Server host (default: 0.0.0.0)
- `SERVER__PORT` - Server port (default: 8080)
- `DATABASE__URL` - PostgreSQL connection string
- `DATABASE__MAX_CONNECTIONS` - Connection pool size (default: 10)
- `RUST_LOG` - Log level (default: info)

## Development

```bash
make help        # Show all commands
make dev         # Run with auto-reload
make test        # Run tests
make lint        # Run clippy
make fmt         # Format code
make check       # Run all checks
```

## License

MIT
```

## Customization Points

When generating a service, customize:

1. **Resource Name**: Replace `User` with your entity (Product, Order, etc.)
2. **Fields**: Modify domain model fields based on requirements
3. **Validations**: Add business-specific validation rules
4. **Database**: Change from PostgreSQL to MySQL or SQLite if needed
5. **Additional Features**:
   - Authentication (JWT, OAuth)
   - Caching (Redis)
   - Message queues (RabbitMQ, Kafka)
   - File uploads (S3)
   - Rate limiting
   - Metrics (Prometheus)

## Best Practices Included

### Rust Idioms
- ✅ Ownership and borrowing used correctly
- ✅ Trait-based abstractions
- ✅ Result type for error handling
- ✅ Async/await throughout
- ✅ No unwrap() in production code

### Architecture
- ✅ Clean separation of concerns
- ✅ Dependency injection via traits
- ✅ Repository pattern for data access
- ✅ Service layer for business logic
- ✅ Testable design with mocking

### Performance
- ✅ Connection pooling
- ✅ Async I/O
- ✅ Efficient query building
- ✅ Response compression
- ✅ Database indexing

### Security
- ✅ Input validation
- ✅ SQL injection prevention
- ✅ Error message sanitization
- ✅ CORS configuration
- ✅ Non-root Docker user

### Operations
- ✅ Structured logging
- ✅ Health checks
- ✅ Graceful shutdown
- ✅ Database migrations
- ✅ Docker multi-stage builds
- ✅ Environment-based config

## Example Usage

```bash
# Create a user
curl -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","name":"John Doe"}'

# Get all users
curl http://localhost:8080/api/users?limit=10&offset=0

# Get specific user
curl http://localhost:8080/api/users/{uuid}

# Update user
curl -X PUT http://localhost:8080/api/users/{uuid} \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe"}'

# Delete user
curl -X DELETE http://localhost:8080/api/users/{uuid}
```

## Troubleshooting

**Database connection failed:**
- Check DATABASE_URL is correct
- Ensure PostgreSQL is running
- Verify network connectivity

**Compilation errors:**
- Update Rust: `rustup update`
- Clean build: `make clean && cargo build`

**Tests failing:**
- Ensure test database is running
- Run migrations: `make migrate`
- Check test database URL

## Next Steps

After generating:

1. ✅ Review generated code
2. ✅ Customize domain models
3. ✅ Add business-specific validations
4. ✅ Implement authentication if needed
5. ✅ Add more endpoints
6. ✅ Write comprehensive tests
7. ✅ Configure CI/CD
8. ✅ Deploy to production

---

**Generated with Rust Service Generator** 🦀
