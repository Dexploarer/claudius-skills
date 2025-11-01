---
name: php-service-generator
description: Generate production-ready PHP services with Laravel, database integration, and best practices
allowed-tools: [Read, Write, Edit, Grep, Glob]
---

# PHP Service Generator

Generate complete, production-ready PHP services following Laravel best practices and modern PHP standards.

## What This Skill Creates

A complete PHP service with:
- ✅ Laravel 10+ framework
- ✅ Eloquent ORM for database
- ✅ Repository pattern
- ✅ Service layer with business logic
- ✅ Request validation with Form Requests
- ✅ Resource transformers for API responses
- ✅ PHPUnit tests
- ✅ Docker with PHP-FPM and Nginx
- ✅ PSR-4 autoloading
- ✅ Logging and error handling
- ✅ Database migrations and seeders
- ✅ API documentation

## Usage

```
"Generate a PHP Laravel service for managing users with CRUD operations"
"Create a PHP API service for products with MySQL"
"Build a PHP microservice for orders with authentication"
```

## Project Structure

The generated service follows Laravel conventions:

```
my-service/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── Api/
│   │   │   │   └── UserController.php
│   │   │   └── Controller.php
│   │   ├── Requests/
│   │   │   ├── CreateUserRequest.php
│   │   │   └── UpdateUserRequest.php
│   │   ├── Resources/
│   │   │   ├── UserResource.php
│   │   │   └── UserCollection.php
│   │   └── Middleware/
│   ├── Models/
│   │   └── User.php
│   ├── Repositories/
│   │   ├── Contracts/
│   │   │   └── UserRepositoryInterface.php
│   │   └── UserRepository.php
│   ├── Services/
│   │   └── UserService.php
│   ├── Exceptions/
│   │   └── Handler.php
│   └── Providers/
│       └── RepositoryServiceProvider.php
├── bootstrap/
│   └── app.php
├── config/
│   ├── app.php
│   ├── database.php
│   └── logging.php
├── database/
│   ├── migrations/
│   │   └── 2024_01_01_000000_create_users_table.php
│   ├── seeders/
│   │   └── DatabaseSeeder.php
│   └── factories/
│       └── UserFactory.php
├── routes/
│   ├── api.php
│   └── web.php
├── tests/
│   ├── Feature/
│   │   └── UserApiTest.php
│   └── Unit/
│       ├── UserRepositoryTest.php
│       └── UserServiceTest.php
├── docker/
│   ├── nginx/
│   │   └── default.conf
│   └── php/
│       └── Dockerfile
├── docker-compose.yml
├── composer.json
├── phpunit.xml
├── .env.example
└── README.md
```

## Instructions for Claude

When the user requests a PHP service generation:

### Step 1: Gather Requirements

Ask for:
1. **Service name**: What should the service be called?
2. **Resource**: What entity to manage (e.g., users, products, orders)?
3. **Database**: MySQL (default), PostgreSQL, or SQLite?
4. **Additional features**: Authentication? File uploads? Queues?

### Step 2: Create Laravel Project

```bash
composer create-project laravel/laravel {service-name}
cd {service-name}
mkdir -p app/Repositories/Contracts app/Services
```

### Step 3: Generate composer.json

Update `composer.json` with necessary dependencies:

```json
{
    "name": "company/{service-name}",
    "type": "project",
    "description": "Production-ready {service-name} API",
    "keywords": ["laravel", "api", "rest"],
    "license": "MIT",
    "require": {
        "php": "^8.2",
        "laravel/framework": "^10.0",
        "laravel/sanctum": "^3.0",
        "laravel/tinker": "^2.8"
    },
    "require-dev": {
        "fakerphp/faker": "^1.23",
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.18",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^7.0",
        "phpunit/phpunit": "^10.0",
        "spatie/laravel-ignition": "^2.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ],
        "test": "phpunit",
        "test-coverage": "phpunit --coverage-html coverage"
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}
```

### Step 4: Create Model

Generate `app/Models/{Resource}.php`:

**Example for User resource:**

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class User extends Model
{
    use HasFactory, SoftDeletes;

    /**
     * The table associated with the model.
     *
     * @var string
     */
    protected $table = 'users';

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'email',
        'name',
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    protected $hidden = [
        'deleted_at',
    ];

    /**
     * The attributes that should be cast.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'created_at' => 'datetime',
        'updated_at' => 'datetime',
        'deleted_at' => 'datetime',
    ];

    /**
     * Validation rules for user creation.
     *
     * @return array<string, mixed>
     */
    public static function createRules(): array
    {
        return [
            'email' => 'required|email|unique:users,email',
            'name' => 'required|string|min:1|max:100',
        ];
    }

    /**
     * Validation rules for user update.
     *
     * @param int|null $userId
     * @return array<string, mixed>
     */
    public static function updateRules(?int $userId = null): array
    {
        return [
            'email' => 'sometimes|email|unique:users,email,' . $userId,
            'name' => 'sometimes|string|min:1|max:100',
        ];
    }
}
```

### Step 5: Create Repository Interface

Generate `app/Repositories/Contracts/{Resource}RepositoryInterface.php`:

```php
<?php

namespace App\Repositories\Contracts;

use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Database\Eloquent\Collection;
use App\Models\User;

interface UserRepositoryInterface
{
    /**
     * Create a new user.
     *
     * @param array<string, mixed> $data
     * @return User
     */
    public function create(array $data): User;

    /**
     * Find user by ID.
     *
     * @param int $id
     * @return User|null
     */
    public function findById(int $id): ?User;

    /**
     * Find user by email.
     *
     * @param string $email
     * @return User|null
     */
    public function findByEmail(string $email): ?User;

    /**
     * Get all users with pagination.
     *
     * @param int $perPage
     * @param array<string, mixed> $filters
     * @return LengthAwarePaginator
     */
    public function paginate(int $perPage = 15, array $filters = []): LengthAwarePaginator;

    /**
     * Update user.
     *
     * @param int $id
     * @param array<string, mixed> $data
     * @return User|null
     */
    public function update(int $id, array $data): ?User;

    /**
     * Delete user.
     *
     * @param int $id
     * @return bool
     */
    public function delete(int $id): bool;

    /**
     * Restore soft-deleted user.
     *
     * @param int $id
     * @return bool
     */
    public function restore(int $id): bool;
}
```

### Step 6: Create Repository Implementation

Generate `app/Repositories/{Resource}Repository.php`:

```php
<?php

namespace App\Repositories;

use App\Models\User;
use App\Repositories\Contracts\UserRepositoryInterface;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Facades\DB;

class UserRepository implements UserRepositoryInterface
{
    /**
     * Create a new user.
     *
     * @param array<string, mixed> $data
     * @return User
     */
    public function create(array $data): User
    {
        return User::create($data);
    }

    /**
     * Find user by ID.
     *
     * @param int $id
     * @return User|null
     */
    public function findById(int $id): ?User
    {
        return User::find($id);
    }

    /**
     * Find user by email.
     *
     * @param string $email
     * @return User|null
     */
    public function findByEmail(string $email): ?User
    {
        return User::where('email', $email)->first();
    }

    /**
     * Get all users with pagination and optional filters.
     *
     * @param int $perPage
     * @param array<string, mixed> $filters
     * @return LengthAwarePaginator
     */
    public function paginate(int $perPage = 15, array $filters = []): LengthAwarePaginator
    {
        $query = User::query();

        // Apply search filter
        if (isset($filters['search']) && !empty($filters['search'])) {
            $search = $filters['search'];
            $query->where(function ($q) use ($search) {
                $q->where('name', 'LIKE', "%{$search}%")
                  ->orWhere('email', 'LIKE', "%{$search}%");
            });
        }

        // Apply sorting
        $sortBy = $filters['sort_by'] ?? 'created_at';
        $sortOrder = $filters['sort_order'] ?? 'desc';
        $query->orderBy($sortBy, $sortOrder);

        return $query->paginate($perPage);
    }

    /**
     * Update user.
     *
     * @param int $id
     * @param array<string, mixed> $data
     * @return User|null
     */
    public function update(int $id, array $data): ?User
    {
        $user = $this->findById($id);

        if (!$user) {
            return null;
        }

        $user->update($data);
        return $user->fresh();
    }

    /**
     * Delete user (soft delete).
     *
     * @param int $id
     * @return bool
     */
    public function delete(int $id): bool
    {
        $user = $this->findById($id);

        if (!$user) {
            return false;
        }

        return $user->delete();
    }

    /**
     * Restore soft-deleted user.
     *
     * @param int $id
     * @return bool
     */
    public function restore(int $id): bool
    {
        $user = User::withTrashed()->find($id);

        if (!$user) {
            return false;
        }

        return $user->restore();
    }
}
```

### Step 7: Create Service Layer

Generate `app/Services/{Resource}Service.php`:

```php
<?php

namespace App\Services;

use App\Models\User;
use App\Repositories\Contracts\UserRepositoryInterface;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use Illuminate\Validation\ValidationException;

class UserService
{
    /**
     * @var UserRepositoryInterface
     */
    protected UserRepositoryInterface $repository;

    /**
     * UserService constructor.
     *
     * @param UserRepositoryInterface $repository
     */
    public function __construct(UserRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    /**
     * Create a new user.
     *
     * @param array<string, mixed> $data
     * @return User
     * @throws ValidationException
     */
    public function createUser(array $data): User
    {
        // Check if email already exists
        if ($this->repository->findByEmail($data['email'])) {
            throw ValidationException::withMessages([
                'email' => ['A user with this email already exists.']
            ]);
        }

        DB::beginTransaction();
        try {
            $user = $this->repository->create($data);

            // Additional business logic here
            // e.g., send welcome email, create related records, etc.

            Log::info('User created', ['user_id' => $user->id]);

            DB::commit();
            return $user;
        } catch (\Exception $e) {
            DB::rollBack();
            Log::error('Failed to create user', [
                'error' => $e->getMessage(),
                'data' => $data
            ]);
            throw $e;
        }
    }

    /**
     * Get user by ID.
     *
     * @param int $id
     * @return User
     * @throws \Exception
     */
    public function getUserById(int $id): User
    {
        $user = $this->repository->findById($id);

        if (!$user) {
            throw new \Exception('User not found', 404);
        }

        return $user;
    }

    /**
     * List users with pagination.
     *
     * @param int $perPage
     * @param array<string, mixed> $filters
     * @return LengthAwarePaginator
     */
    public function listUsers(int $perPage = 15, array $filters = []): LengthAwarePaginator
    {
        return $this->repository->paginate($perPage, $filters);
    }

    /**
     * Update user.
     *
     * @param int $id
     * @param array<string, mixed> $data
     * @return User
     * @throws \Exception
     */
    public function updateUser(int $id, array $data): User
    {
        // Check if email is being changed to one that already exists
        if (isset($data['email'])) {
            $existingUser = $this->repository->findByEmail($data['email']);
            if ($existingUser && $existingUser->id !== $id) {
                throw ValidationException::withMessages([
                    'email' => ['A user with this email already exists.']
                ]);
            }
        }

        DB::beginTransaction();
        try {
            $user = $this->repository->update($id, $data);

            if (!$user) {
                throw new \Exception('User not found', 404);
            }

            Log::info('User updated', ['user_id' => $user->id]);

            DB::commit();
            return $user;
        } catch (\Exception $e) {
            DB::rollBack();
            Log::error('Failed to update user', [
                'error' => $e->getMessage(),
                'user_id' => $id,
                'data' => $data
            ]);
            throw $e;
        }
    }

    /**
     * Delete user.
     *
     * @param int $id
     * @return void
     * @throws \Exception
     */
    public function deleteUser(int $id): void
    {
        DB::beginTransaction();
        try {
            $deleted = $this->repository->delete($id);

            if (!$deleted) {
                throw new \Exception('User not found', 404);
            }

            Log::info('User deleted', ['user_id' => $id]);

            DB::commit();
        } catch (\Exception $e) {
            DB::rollBack();
            Log::error('Failed to delete user', [
                'error' => $e->getMessage(),
                'user_id' => $id
            ]);
            throw $e;
        }
    }
}
```

### Step 8: Create Form Requests

Generate `app/Http/Requests/Create{Resource}Request.php`:

```php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Contracts\Validation\Validator;
use Illuminate\Http\Exceptions\HttpResponseException;

class CreateUserRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true; // Implement authorization logic here
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array|string>
     */
    public function rules(): array
    {
        return [
            'email' => 'required|email|unique:users,email|max:255',
            'name' => 'required|string|min:1|max:100',
        ];
    }

    /**
     * Get custom error messages for validator errors.
     *
     * @return array<string, string>
     */
    public function messages(): array
    {
        return [
            'email.required' => 'Email address is required',
            'email.email' => 'Email address must be valid',
            'email.unique' => 'This email is already registered',
            'name.required' => 'Name is required',
            'name.min' => 'Name must be at least 1 character',
            'name.max' => 'Name cannot exceed 100 characters',
        ];
    }

    /**
     * Handle a failed validation attempt.
     *
     * @param Validator $validator
     * @return void
     *
     * @throws HttpResponseException
     */
    protected function failedValidation(Validator $validator): void
    {
        throw new HttpResponseException(
            response()->json([
                'message' => 'Validation failed',
                'errors' => $validator->errors()
            ], 422)
        );
    }
}
```

Generate `app/Http/Requests/Update{Resource}Request.php`:

```php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Contracts\Validation\Validator;
use Illuminate\Http\Exceptions\HttpResponseException;

class UpdateUserRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true; // Implement authorization logic here
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array|string>
     */
    public function rules(): array
    {
        $userId = $this->route('user');

        return [
            'email' => 'sometimes|email|unique:users,email,' . $userId . '|max:255',
            'name' => 'sometimes|string|min:1|max:100',
        ];
    }

    /**
     * Get custom error messages for validator errors.
     *
     * @return array<string, string>
     */
    public function messages(): array
    {
        return [
            'email.email' => 'Email address must be valid',
            'email.unique' => 'This email is already registered',
            'name.min' => 'Name must be at least 1 character',
            'name.max' => 'Name cannot exceed 100 characters',
        ];
    }

    /**
     * Handle a failed validation attempt.
     *
     * @param Validator $validator
     * @return void
     *
     * @throws HttpResponseException
     */
    protected function failedValidation(Validator $validator): void
    {
        throw new HttpResponseException(
            response()->json([
                'message' => 'Validation failed',
                'errors' => $validator->errors()
            ], 422)
        );
    }
}
```

### Step 9: Create API Resources

Generate `app/Http/Resources/{Resource}Resource.php`:

```php
<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class UserResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'email' => $this->email,
            'name' => $this->name,
            'created_at' => $this->created_at->toIso8601String(),
            'updated_at' => $this->updated_at->toIso8601String(),
        ];
    }
}
```

Generate `app/Http/Resources/{Resource}Collection.php`:

```php
<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\ResourceCollection;

class UserCollection extends ResourceCollection
{
    /**
     * Transform the resource collection into an array.
     *
     * @return array<int|string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'data' => $this->collection,
            'meta' => [
                'total' => $this->total(),
                'per_page' => $this->perPage(),
                'current_page' => $this->currentPage(),
                'last_page' => $this->lastPage(),
            ],
        ];
    }
}
```

### Step 10: Create Controller

Generate `app/Http/Controllers/Api/{Resource}Controller.php`:

```php
<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Requests\CreateUserRequest;
use App\Http\Requests\UpdateUserRequest;
use App\Http\Resources\UserResource;
use App\Http\Resources\UserCollection;
use App\Services\UserService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * @var UserService
     */
    protected UserService $userService;

    /**
     * UserController constructor.
     *
     * @param UserService $userService
     */
    public function __construct(UserService $userService)
    {
        $this->userService = $userService;
    }

    /**
     * Display a listing of users.
     *
     * @param Request $request
     * @return UserCollection
     */
    public function index(Request $request): UserCollection
    {
        $perPage = $request->input('per_page', 15);
        $filters = $request->only(['search', 'sort_by', 'sort_order']);

        $users = $this->userService->listUsers($perPage, $filters);

        return new UserCollection($users);
    }

    /**
     * Store a newly created user.
     *
     * @param CreateUserRequest $request
     * @return JsonResponse
     */
    public function store(CreateUserRequest $request): JsonResponse
    {
        try {
            $user = $this->userService->createUser($request->validated());

            return response()->json([
                'message' => 'User created successfully',
                'data' => new UserResource($user)
            ], 201);
        } catch (\Exception $e) {
            return response()->json([
                'message' => 'Failed to create user',
                'error' => $e->getMessage()
            ], 500);
        }
    }

    /**
     * Display the specified user.
     *
     * @param int $id
     * @return JsonResponse
     */
    public function show(int $id): JsonResponse
    {
        try {
            $user = $this->userService->getUserById($id);

            return response()->json([
                'data' => new UserResource($user)
            ]);
        } catch (\Exception $e) {
            $statusCode = $e->getCode() === 404 ? 404 : 500;
            return response()->json([
                'message' => $e->getMessage()
            ], $statusCode);
        }
    }

    /**
     * Update the specified user.
     *
     * @param UpdateUserRequest $request
     * @param int $id
     * @return JsonResponse
     */
    public function update(UpdateUserRequest $request, int $id): JsonResponse
    {
        try {
            $user = $this->userService->updateUser($id, $request->validated());

            return response()->json([
                'message' => 'User updated successfully',
                'data' => new UserResource($user)
            ]);
        } catch (\Exception $e) {
            $statusCode = $e->getCode() === 404 ? 404 : 500;
            return response()->json([
                'message' => 'Failed to update user',
                'error' => $e->getMessage()
            ], $statusCode);
        }
    }

    /**
     * Remove the specified user.
     *
     * @param int $id
     * @return JsonResponse
     */
    public function destroy(int $id): JsonResponse
    {
        try {
            $this->userService->deleteUser($id);

            return response()->json([
                'message' => 'User deleted successfully'
            ], 204);
        } catch (\Exception $e) {
            $statusCode = $e->getCode() === 404 ? 404 : 500;
            return response()->json([
                'message' => 'Failed to delete user',
                'error' => $e->getMessage()
            ], $statusCode);
        }
    }
}
```

### Step 11: Create Service Provider

Generate `app/Providers/RepositoryServiceProvider.php`:

```php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use App\Repositories\Contracts\UserRepositoryInterface;
use App\Repositories\UserRepository;

class RepositoryServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     */
    public function register(): void
    {
        $this->app->bind(
            UserRepositoryInterface::class,
            UserRepository::class
        );
    }

    /**
     * Bootstrap services.
     */
    public function boot(): void
    {
        //
    }
}
```

Register the service provider in `config/app.php`:

```php
'providers' => [
    // ...
    App\Providers\RepositoryServiceProvider::class,
],
```

### Step 12: Create Routes

Update `routes/api.php`:

```php
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\UserController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
*/

// Health check
Route::get('/health', function () {
    return response()->json([
        'status' => 'healthy',
        'service' => config('app.name'),
        'version' => '1.0.0',
        'timestamp' => now()->toIso8601String(),
    ]);
});

// User routes
Route::prefix('v1')->group(function () {
    Route::apiResource('users', UserController::class);
});
```

### Step 13: Create Migration

Generate `database/migrations/2024_01_01_000000_create_users_table.php`:

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('email')->unique();
            $table->string('name', 100);
            $table->timestamps();
            $table->softDeletes();

            // Indexes
            $table->index('email');
            $table->index('created_at');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('users');
    }
};
```

### Step 14: Create Factory

Generate `database/factories/{Resource}Factory.php`:

```php
<?php

namespace Database\Factories;

use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\User>
 */
class UserFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = User::class;

    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'email' => fake()->unique()->safeEmail(),
            'name' => fake()->name(),
        ];
    }
}
```

### Step 15: Create Tests

Generate `tests/Unit/UserRepositoryTest.php`:

```php
<?php

namespace Tests\Unit;

use App\Models\User;
use App\Repositories\UserRepository;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class UserRepositoryTest extends TestCase
{
    use RefreshDatabase;

    protected UserRepository $repository;

    protected function setUp(): void
    {
        parent::setUp();
        $this->repository = new UserRepository();
    }

    public function test_create_user(): void
    {
        $data = [
            'email' => 'test@example.com',
            'name' => 'Test User',
        ];

        $user = $this->repository->create($data);

        $this->assertInstanceOf(User::class, $user);
        $this->assertEquals('test@example.com', $user->email);
        $this->assertEquals('Test User', $user->name);
        $this->assertDatabaseHas('users', $data);
    }

    public function test_find_by_id(): void
    {
        $user = User::factory()->create();

        $found = $this->repository->findById($user->id);

        $this->assertInstanceOf(User::class, $found);
        $this->assertEquals($user->id, $found->id);
    }

    public function test_find_by_email(): void
    {
        $user = User::factory()->create(['email' => 'unique@example.com']);

        $found = $this->repository->findByEmail('unique@example.com');

        $this->assertInstanceOf(User::class, $found);
        $this->assertEquals($user->id, $found->id);
    }

    public function test_update_user(): void
    {
        $user = User::factory()->create();

        $updated = $this->repository->update($user->id, [
            'name' => 'Updated Name'
        ]);

        $this->assertEquals('Updated Name', $updated->name);
        $this->assertDatabaseHas('users', [
            'id' => $user->id,
            'name' => 'Updated Name'
        ]);
    }

    public function test_delete_user(): void
    {
        $user = User::factory()->create();

        $result = $this->repository->delete($user->id);

        $this->assertTrue($result);
        $this->assertSoftDeleted('users', ['id' => $user->id]);
    }

    public function test_paginate_users(): void
    {
        User::factory()->count(25)->create();

        $paginated = $this->repository->paginate(10);

        $this->assertCount(10, $paginated->items());
        $this->assertEquals(25, $paginated->total());
    }
}
```

Generate `tests/Unit/UserServiceTest.php`:

```php
<?php

namespace Tests\Unit;

use App\Models\User;
use App\Repositories\Contracts\UserRepositoryInterface;
use App\Services\UserService;
use Illuminate\Validation\ValidationException;
use Mockery;
use Tests\TestCase;

class UserServiceTest extends TestCase
{
    protected UserService $service;
    protected $mockRepository;

    protected function setUp(): void
    {
        parent::setUp();
        $this->mockRepository = Mockery::mock(UserRepositoryInterface::class);
        $this->service = new UserService($this->mockRepository);
    }

    protected function tearDown(): void
    {
        Mockery::close();
        parent::tearDown();
    }

    public function test_create_user_success(): void
    {
        $data = [
            'email' => 'test@example.com',
            'name' => 'Test User',
        ];

        $expectedUser = new User($data);
        $expectedUser->id = 1;

        $this->mockRepository
            ->shouldReceive('findByEmail')
            ->with('test@example.com')
            ->once()
            ->andReturn(null);

        $this->mockRepository
            ->shouldReceive('create')
            ->with($data)
            ->once()
            ->andReturn($expectedUser);

        $result = $this->service->createUser($data);

        $this->assertInstanceOf(User::class, $result);
        $this->assertEquals('test@example.com', $result->email);
    }

    public function test_create_user_duplicate_email(): void
    {
        $data = [
            'email' => 'existing@example.com',
            'name' => 'Test User',
        ];

        $existingUser = new User(['email' => 'existing@example.com']);

        $this->mockRepository
            ->shouldReceive('findByEmail')
            ->with('existing@example.com')
            ->once()
            ->andReturn($existingUser);

        $this->expectException(ValidationException::class);

        $this->service->createUser($data);
    }

    public function test_get_user_by_id_success(): void
    {
        $user = new User(['id' => 1, 'email' => 'test@example.com']);

        $this->mockRepository
            ->shouldReceive('findById')
            ->with(1)
            ->once()
            ->andReturn($user);

        $result = $this->service->getUserById(1);

        $this->assertInstanceOf(User::class, $result);
    }

    public function test_get_user_by_id_not_found(): void
    {
        $this->mockRepository
            ->shouldReceive('findById')
            ->with(999)
            ->once()
            ->andReturn(null);

        $this->expectException(\Exception::class);
        $this->expectExceptionMessage('User not found');

        $this->service->getUserById(999);
    }
}
```

Generate `tests/Feature/UserApiTest.php`:

```php
<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class UserApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_health_endpoint(): void
    {
        $response = $this->getJson('/api/health');

        $response->assertStatus(200)
            ->assertJson([
                'status' => 'healthy'
            ]);
    }

    public function test_create_user(): void
    {
        $data = [
            'email' => 'test@example.com',
            'name' => 'Test User',
        ];

        $response = $this->postJson('/api/v1/users', $data);

        $response->assertStatus(201)
            ->assertJson([
                'message' => 'User created successfully',
                'data' => [
                    'email' => 'test@example.com',
                    'name' => 'Test User',
                ]
            ]);

        $this->assertDatabaseHas('users', $data);
    }

    public function test_create_user_validation_error(): void
    {
        $data = [
            'email' => 'invalid-email',
            'name' => '',
        ];

        $response = $this->postJson('/api/v1/users', $data);

        $response->assertStatus(422)
            ->assertJsonStructure([
                'message',
                'errors' => ['email', 'name']
            ]);
    }

    public function test_get_user(): void
    {
        $user = User::factory()->create();

        $response = $this->getJson("/api/v1/users/{$user->id}");

        $response->assertStatus(200)
            ->assertJson([
                'data' => [
                    'id' => $user->id,
                    'email' => $user->email,
                    'name' => $user->name,
                ]
            ]);
    }

    public function test_list_users(): void
    {
        User::factory()->count(15)->create();

        $response = $this->getJson('/api/v1/users');

        $response->assertStatus(200)
            ->assertJsonStructure([
                'data',
                'meta' => ['total', 'per_page', 'current_page', 'last_page']
            ]);
    }

    public function test_update_user(): void
    {
        $user = User::factory()->create();

        $data = ['name' => 'Updated Name'];

        $response = $this->putJson("/api/v1/users/{$user->id}", $data);

        $response->assertStatus(200)
            ->assertJson([
                'message' => 'User updated successfully',
                'data' => [
                    'name' => 'Updated Name'
                ]
            ]);

        $this->assertDatabaseHas('users', [
            'id' => $user->id,
            'name' => 'Updated Name'
        ]);
    }

    public function test_delete_user(): void
    {
        $user = User::factory()->create();

        $response = $this->deleteJson("/api/v1/users/{$user->id}");

        $response->assertStatus(204);

        $this->assertSoftDeleted('users', ['id' => $user->id]);
    }

    public function test_search_users(): void
    {
        User::factory()->create(['name' => 'John Doe']);
        User::factory()->create(['name' => 'Jane Smith']);

        $response = $this->getJson('/api/v1/users?search=John');

        $response->assertStatus(200)
            ->assertJsonFragment(['name' => 'John Doe'])
            ->assertJsonMissing(['name' => 'Jane Smith']);
    }
}
```

### Step 16: Create Docker Configuration

Generate `docker/php/Dockerfile`:

```dockerfile
FROM php:8.2-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    libzip-dev \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd zip

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Set working directory
WORKDIR /var/www

# Copy application files
COPY . /var/www

# Install dependencies
RUN composer install --no-dev --optimize-autoloader

# Set permissions
RUN chown -R www-data:www-data /var/www \
    && chmod -R 755 /var/www/storage \
    && chmod -R 755 /var/www/bootstrap/cache

USER www-data

EXPOSE 9000

CMD ["php-fpm"]
```

Generate `docker/nginx/default.conf`:

```nginx
server {
    listen 80;
    index index.php index.html;
    server_name localhost;
    root /var/www/public;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass app:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
}
```

Generate `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: docker/php/Dockerfile
    container_name: {service-name}-app
    restart: unless-stopped
    working_dir: /var/www
    volumes:
      - ./:/var/www
    networks:
      - {service-name}-network
    depends_on:
      - db

  nginx:
    image: nginx:alpine
    container_name: {service-name}-nginx
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./:/var/www
      - ./docker/nginx/default.conf:/etc/nginx/conf.d/default.conf
    networks:
      - {service-name}-network
    depends_on:
      - app

  db:
    image: mysql:8.0
    container_name: {service-name}-db
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: ${DB_DATABASE}
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_USER: ${DB_USERNAME}
    ports:
      - "3306:3306"
    volumes:
      - dbdata:/var/lib/mysql
    networks:
      - {service-name}-network

networks:
  {service-name}-network:
    driver: bridge

volumes:
  dbdata:
    driver: local
```

### Step 17: Create Environment File

Generate `.env.example`:

```bash
APP_NAME="My Service"
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost:8080

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE=myservice
DB_USERNAME=root
DB_PASSWORD=secret

CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120
```

### Step 18: Update PHPUnit Configuration

Update `phpunit.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="vendor/phpunit/phpunit/phpunit.xsd"
         bootstrap="vendor/autoload.php"
         colors="true">
    <testsuites>
        <testsuite name="Unit">
            <directory suffix="Test.php">./tests/Unit</directory>
        </testsuite>
        <testsuite name="Feature">
            <directory suffix="Test.php">./tests/Feature</directory>
        </testsuite>
    </testsuites>
    <source>
        <include>
            <directory suffix=".php">./app</directory>
        </include>
    </source>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="BCRYPT_ROUNDS" value="4"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="DB_CONNECTION" value="sqlite"/>
        <env name="DB_DATABASE" value=":memory:"/>
        <env name="MAIL_MAILER" value="array"/>
        <env name="QUEUE_CONNECTION" value="sync"/>
        <env name="SESSION_DRIVER" value="array"/>
    </php>
</phpunit>
```

### Step 19: Create README

Generate `README.md`:

```markdown
# {Service Name}

Production-ready PHP Laravel API service.

## Features

- ✅ Laravel 10+ framework
- ✅ Repository pattern
- ✅ Service layer
- ✅ Form Request validation
- ✅ API Resources for responses
- ✅ Comprehensive tests (PHPUnit)
- ✅ Docker support
- ✅ Database migrations
- ✅ Soft deletes
- ✅ Logging and error handling

## Quick Start

### Prerequisites

- PHP 8.2+
- Composer
- MySQL 8.0+
- Docker (optional)

### Development Setup

1. **Install dependencies:**
   ```bash
   composer install
   ```

2. **Environment configuration:**
   ```bash
   cp .env.example .env
   php artisan key:generate
   ```

3. **Database setup:**
   ```bash
   php artisan migrate
   php artisan db:seed
   ```

4. **Start server:**
   ```bash
   php artisan serve
   ```

### Docker Setup

```bash
# Build and start containers
docker-compose up -d

# Run migrations
docker-compose exec app php artisan migrate

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

## API Endpoints

Base URL: `http://localhost:8080/api`

### Health
- `GET /health` - Health check

### Users (v1)
- `POST /v1/users` - Create user
- `GET /v1/users` - List users (paginated)
- `GET /v1/users/{id}` - Get user
- `PUT /v1/users/{id}` - Update user
- `DELETE /v1/users/{id}` - Delete user

### Query Parameters
- `per_page` - Items per page (default: 15)
- `search` - Search by name or email
- `sort_by` - Sort field (default: created_at)
- `sort_order` - Sort direction (asc/desc, default: desc)

## Testing

```bash
# Run all tests
php artisan test

# Run specific test suite
php artisan test --testsuite=Feature

# Generate coverage report
php artisan test --coverage
```

## Project Structure

```
app/
├── Http/
│   ├── Controllers/Api/    # API controllers
│   ├── Requests/           # Form requests
│   └── Resources/          # API resources
├── Models/                 # Eloquent models
├── Repositories/           # Data access layer
│   └── Contracts/          # Repository interfaces
├── Services/               # Business logic
└── Providers/              # Service providers
```

## Architecture

### Repository Pattern
Data access logic is isolated in repositories implementing interfaces. Controllers never access models directly.

### Service Layer
Business logic lives in services. Services use repositories and contain transaction management.

### Form Requests
All input validation uses dedicated Form Request classes with custom error messages.

### API Resources
Response transformation uses Laravel API Resources for consistent formatting.

## Development Commands

```bash
# Database
php artisan migrate              # Run migrations
php artisan migrate:rollback     # Rollback last migration
php artisan migrate:fresh --seed # Fresh database with seeds

# Testing
php artisan test                 # Run tests
php artisan test --parallel      # Run tests in parallel

# Code Quality
./vendor/bin/pint                # Format code (Laravel Pint)
```

## Configuration

All configuration via environment variables:

- `APP_*` - Application settings
- `DB_*` - Database connection
- `LOG_*` - Logging configuration
- See `.env.example` for full list

## Deployment

1. Set environment to production:
   ```bash
   APP_ENV=production
   APP_DEBUG=false
   ```

2. Optimize autoloader and config:
   ```bash
   composer install --no-dev --optimize-autoloader
   php artisan config:cache
   php artisan route:cache
   php artisan view:cache
   ```

3. Run migrations:
   ```bash
   php artisan migrate --force
   ```

4. Set proper permissions:
   ```bash
   chmod -R 755 storage bootstrap/cache
   ```

## Best Practices

### PSR Standards
- ✅ PSR-4 autoloading
- ✅ PSR-12 coding style
- ✅ Type hints and return types

### Laravel Conventions
- ✅ Eloquent models
- ✅ Resource controllers
- ✅ Form requests
- ✅ API resources
- ✅ Database migrations

### Security
- ✅ Input validation
- ✅ SQL injection prevention (Eloquent)
- ✅ Mass assignment protection
- ✅ CORS configuration
- ✅ Error message sanitization

### Testing
- ✅ Unit tests for services and repositories
- ✅ Feature tests for API endpoints
- ✅ Database factories
- ✅ Test isolation with RefreshDatabase

## Troubleshooting

**Database connection failed:**
- Check .env database credentials
- Ensure MySQL is running
- Verify DB_HOST (use `db` for Docker)

**Composer dependencies:**
- Clear cache: `composer clear-cache`
- Update: `composer update`

**Permission errors:**
- Fix storage permissions: `chmod -R 755 storage`

## License

MIT

---

**Generated with PHP Service Generator**
```

## Customization Points

When generating a service:

1. **Resource Name**: Replace `User` with your entity
2. **Fields**: Modify model attributes and validation rules
3. **Database**: Switch to PostgreSQL or other databases
4. **Additional Features**:
   - Authentication (Sanctum, Passport)
   - File uploads (S3 integration)
   - Queues (Redis, database)
   - Caching (Redis, Memcached)
   - Rate limiting
   - API versioning

## Example API Usage

```bash
# Create user
curl -X POST http://localhost:8080/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","name":"John Doe"}'

# List users with pagination
curl "http://localhost:8080/api/v1/users?per_page=10&search=john"

# Get user
curl http://localhost:8080/api/v1/users/1

# Update user
curl -X PUT http://localhost:8080/api/v1/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe"}'

# Delete user
curl -X DELETE http://localhost:8080/api/v1/users/1
```

---

**Generated with PHP Laravel Service Generator** 🐘
