# GraphQL Federation Architect

**Category:** API Architecture
**Level:** Advanced
**Auto-trigger:** When user mentions GraphQL federation, microservices GraphQL, or distributed GraphQL schemas

---

## Description

Implements GraphQL Federation for distributed microservices, including Apollo Federation setup, schema stitching, gateway configuration, and federated entity resolution across multiple GraphQL services.

---

## Activation Phrases

- "Set up GraphQL federation"
- "Create federated GraphQL schema"
- "Configure Apollo Federation"
- "Implement GraphQL gateway"
- "Set up microservices GraphQL"

---

## Code Examples

### Federated Subgraph (Users Service)

```typescript
// users-service/src/schema.ts
import { buildSubgraphSchema } from '@apollo/subgraph';
import { gql } from 'apollo-server';

const typeDefs = gql`
  extend schema
    @link(url: "https://specs.apollo.dev/federation/v2.0",
          import: ["@key", "@shareable", "@external"])

  type User @key(fields: "id") {
    id: ID!
    email: String!
    name: String!
    createdAt: String!
  }

  type Query {
    user(id: ID!): User
    users: [User!]!
  }
`;

const resolvers = {
  Query: {
    user: async (_: any, { id }: { id: string }) => {
      return await db.users.findUnique({ where: { id } });
    },
    users: async () => {
      return await db.users.findMany();
    }
  },
  User: {
    __resolveReference: async (reference: { id: string }) => {
      return await db.users.findUnique({ where: { id: reference.id } });
    }
  }
};

export const schema = buildSubgraphSchema({ typeDefs, resolvers });
```

### Federated Subgraph (Posts Service)

```typescript
// posts-service/src/schema.ts
import { buildSubgraphSchema } from '@apollo/subgraph';
import { gql } from 'apollo-server';

const typeDefs = gql`
  extend schema
    @link(url: "https://specs.apollo.dev/federation/v2.0",
          import: ["@key", "@external"])

  type User @key(fields: "id") {
    id: ID! @external
    posts: [Post!]!
  }

  type Post @key(fields: "id") {
    id: ID!
    title: String!
    content: String!
    authorId: ID!
    author: User!
  }

  type Query {
    post(id: ID!): Post
    posts: [Post!]!
  }
`;

const resolvers = {
  User: {
    posts: async (user: { id: string }) => {
      return await db.posts.findMany({ where: { authorId: user.id } });
    }
  },
  Post: {
    author: (post: { authorId: string }) => {
      return { __typename: 'User', id: post.authorId };
    }
  },
  Query: {
    post: async (_: any, { id }: { id: string }) => {
      return await db.posts.findUnique({ where: { id } });
    },
    posts: async () => {
      return await db.posts.findMany();
    }
  }
};

export const schema = buildSubgraphSchema({ typeDefs, resolvers });
```

### Apollo Gateway Configuration

```typescript
// gateway/src/index.ts
import { ApolloGateway, IntrospectAndCompose } from '@apollo/gateway';
import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'users', url: 'http://users-service:4001/graphql' },
      { name: 'posts', url: 'http://posts-service:4002/graphql' },
      { name: 'comments', url: 'http://comments-service:4003/graphql' }
    ],
    pollIntervalInMs: 10000 // Poll for schema updates
  }),
  buildService({ url }) {
    return new RemoteGraphQLDataSource({
      url,
      willSendRequest({ request, context }) {
        // Forward auth headers
        request.http.headers.set('authorization', context.token || '');
      }
    });
  }
});

const server = new ApolloServer({
  gateway,
  subscriptions: false
});

const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 },
  context: async ({ req }) => ({
    token: req.headers.authorization || ''
  })
});

console.log(`🚀 Gateway ready at ${url}`);
```

---

## Best Practices

1. **Use @key Directives** - Define entity keys for cross-service resolution
2. **Minimize N+1 Queries** - Use DataLoader for batching
3. **Version Schema Changes** - Use @deprecated for breaking changes
4. **Monitor Performance** - Track query execution time per subgraph
5. **Implement Caching** - Use automatic persisted queries

---

**Last Updated:** 2025-11-02
