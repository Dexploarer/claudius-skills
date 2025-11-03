// Prisma configuration for Railway deployment
// prisma/seed.ts example and configuration

/**
 * Prisma Client Configuration
 *
 * Best practices for Railway:
 * 1. Use connection pooling
 * 2. Handle SSL properly
 * 3. Implement singleton pattern
 * 4. Add proper logging
 */

// lib/prisma.ts
import { PrismaClient } from '@prisma/client';

declare global {
  var prisma: PrismaClient | undefined;
}

export const prisma = global.prisma || new PrismaClient({
  log: process.env.NODE_ENV === 'development'
    ? ['query', 'error', 'warn']
    : ['error'],

  datasources: {
    db: {
      url: process.env.DATABASE_URL,
    },
  },
});

if (process.env.NODE_ENV !== 'production') {
  global.prisma = prisma;
}

// Middleware for query logging and performance tracking
prisma.$use(async (params, next) => {
  const before = Date.now();
  const result = await next(params);
  const after = Date.now();
  const duration = after - before;

  if (duration > 1000) {
    console.warn(`Slow query: ${params.model}.${params.action} took ${duration}ms`);
  }

  return result;
});

// Graceful shutdown
process.on('beforeExit', async () => {
  await prisma.$disconnect();
});

/**
 * Package.json scripts
 */
const scripts = {
  "prisma:generate": "prisma generate",
  "prisma:migrate:dev": "prisma migrate dev",
  "prisma:migrate:deploy": "prisma migrate deploy",
  "prisma:studio": "prisma studio",
  "prisma:seed": "ts-node prisma/seed.ts",
  "db:push": "prisma db push",
  "db:reset": "prisma migrate reset",

  // Railway-specific
  "railway:migrate": "railway run npx prisma migrate deploy",
  "railway:seed": "railway run npm run prisma:seed",
  "railway:studio": "railway run npx prisma studio",
};

/**
 * Seed script example
 * prisma/seed.ts
 */
const seedExample = `
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
  console.log('Start seeding...');

  // Create users
  const users = await Promise.all([
    prisma.user.create({
      data: {
        email: 'alice@example.com',
        name: 'Alice',
        posts: {
          create: [
            { title: 'Hello World', content: 'This is my first post', published: true },
            { title: 'Draft Post', content: 'Work in progress', published: false },
          ],
        },
      },
    }),
    prisma.user.create({
      data: {
        email: 'bob@example.com',
        name: 'Bob',
        posts: {
          create: [
            { title: 'Getting Started', content: 'Railway is awesome!', published: true },
          ],
        },
      },
    }),
  ]);

  console.log(\`Created \${users.length} users\`);
  console.log('Seeding finished.');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
`;

/**
 * Railway deployment workflow
 */
const railwayWorkflow = {
  steps: [
    '1. Add Postgres to Railway project',
    '2. Configure DATABASE_URL environment variable (automatic)',
    '3. Create Prisma schema',
    '4. Generate initial migration locally: npx prisma migrate dev --name init',
    '5. Deploy migration to Railway: railway run npx prisma migrate deploy',
    '6. Seed database (optional): railway run npm run prisma:seed',
    '7. Deploy application: railway up',
  ],

  commands: {
    local_development: 'railway run npm run dev',
    run_migrations: 'railway run npx prisma migrate deploy',
    view_database: 'railway run npx prisma studio',
    seed_database: 'railway run npm run prisma:seed',
  },
};

module.exports = {
  scripts,
  seedExample,
  railwayWorkflow,
};
