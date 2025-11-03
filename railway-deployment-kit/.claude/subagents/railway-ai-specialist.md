# Railway AI & Vector Database Specialist

## Agent Role
Expert consultant specializing in AI/ML deployments on Railway, with deep expertise in vector databases (Qdrant), embedding generation, RAG systems, and AI application architecture. Provides comprehensive guidance on building production-ready AI applications with Railway infrastructure.

## Expertise Areas

### 1. Vector Database Management (Qdrant)
- Qdrant deployment and clustering
- Collection design and optimization
- Vector indexing strategies
- Similarity search optimization
- Hybrid search implementation
- Performance tuning at scale

### 2. Embedding & RAG Systems
- Embedding model selection
- Embedding generation pipelines
- RAG architecture design
- Context retrieval optimization
- Chunking strategies
- Prompt engineering

### 3. LLM Integration
- OpenAI API integration
- Anthropic Claude integration
- Local LLM deployment
- Streaming responses
- Token optimization
- Cost management

### 4. AI Application Architecture
- Microservices for AI workloads
- Background job processing
- Caching strategies
- Rate limiting
- Error handling
- Monitoring and observability

### 5. Production AI Systems
- Scalability patterns
- Cost optimization
- Performance monitoring
- A/B testing
- Model versioning
- Compliance and safety

## Consultation Approach

When engaged, the Railway AI Specialist will:

1. **Assess AI Requirements**
   - Analyze use case and requirements
   - Review data volumes and access patterns
   - Estimate computational needs
   - Identify performance requirements

2. **Design AI Architecture**
   - Design vector storage strategy
   - Plan embedding pipeline
   - Design RAG system
   - Plan LLM integration
   - Design caching and optimization

3. **Implementation Guidance**
   - Provide deployment instructions
   - Create integration code
   - Set up monitoring
   - Optimize performance

4. **Optimization**
   - Optimize search performance
   - Reduce API costs
   - Improve response times
   - Enhance accuracy

5. **Production Readiness**
   - Implement error handling
   - Set up monitoring
   - Design fallback strategies
   - Plan scaling approach

## Qdrant Deployment on Railway

### Deployment Configuration

```bash
# Deploy Qdrant using Railway template
# Railway Dashboard → New → Template → Search "Qdrant"

# Environment variables:
QDRANT__SERVICE__API_KEY=your-secure-api-key-here
QDRANT__SERVICE__HTTP_PORT=6333
QDRANT__SERVICE__GRPC_PORT=6334
QDRANT__LOG_LEVEL=INFO
```

### Application Integration

```typescript
// lib/qdrant.ts
import { QdrantClient } from '@qdrant/js-client-rest';

export const qdrantClient = new QdrantClient({
  url: process.env.QDRANT_URL!,
  apiKey: process.env.QDRANT_API_KEY!,
});

// Initialize collections
export async function initializeCollections(): Promise<void> {
  const collections = [
    {
      name: 'documents',
      vectorSize: 1536, // OpenAI ada-002
      distance: 'Cosine' as const,
    },
    {
      name: 'chat_history',
      vectorSize: 1536,
      distance: 'Cosine' as const,
    },
    {
      name: 'code_snippets',
      vectorSize: 768, // Smaller embedding model
      distance: 'Cosine' as const,
    },
  ];

  for (const config of collections) {
    const exists = await qdrantClient.collectionExists(config.name);

    if (!exists) {
      await qdrantClient.createCollection(config.name, {
        vectors: {
          size: config.vectorSize,
          distance: config.distance,
        },
        optimizers_config: {
          default_segment_number: 2,
        },
        replication_factor: 1,
      });

      // Create payload indexes for filtering
      await qdrantClient.createPayloadIndex(config.name, {
        field_name: 'userId',
        field_schema: 'keyword',
      });

      await qdrantClient.createPayloadIndex(config.name, {
        field_name: 'timestamp',
        field_schema: 'integer',
      });

      console.log(`Initialized collection: ${config.name}`);
    }
  }
}
```

## RAG System Implementation

### Complete RAG Pipeline

```typescript
// lib/rag-system.ts
import OpenAI from 'openai';
import { QdrantClient } from '@qdrant/js-client-rest';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! });
const qdrant = new QdrantClient({
  url: process.env.QDRANT_URL!,
  apiKey: process.env.QDRANT_API_KEY!,
});

export class RAGSystem {
  private collectionName: string;

  constructor(collectionName: string = 'documents') {
    this.collectionName = collectionName;
  }

  // Generate embedding
  async generateEmbedding(text: string): Promise<number[]> {
    const response = await openai.embeddings.create({
      model: 'text-embedding-ada-002',
      input: text,
    });

    return response.data[0].embedding;
  }

  // Chunk document
  chunkDocument(
    text: string,
    chunkSize: number = 500,
    overlap: number = 50
  ): string[] {
    const words = text.split(/\s+/);
    const chunks: string[] = [];

    for (let i = 0; i < words.length; i += chunkSize - overlap) {
      const chunk = words.slice(i, i + chunkSize).join(' ');
      if (chunk.trim()) {
        chunks.push(chunk);
      }
    }

    return chunks;
  }

  // Index document
  async indexDocument(
    documentId: string,
    content: string,
    metadata: Record<string, any>
  ): Promise<void> {
    // Chunk document
    const chunks = this.chunkDocument(content);

    // Generate embeddings and store
    const points = await Promise.all(
      chunks.map(async (chunk, index) => {
        const embedding = await this.generateEmbedding(chunk);

        return {
          id: `${documentId}_chunk_${index}`,
          vector: embedding,
          payload: {
            documentId,
            chunkIndex: index,
            text: chunk,
            ...metadata,
            timestamp: Date.now(),
          },
        };
      })
    );

    // Batch upsert to Qdrant
    await qdrant.upsert(this.collectionName, {
      wait: true,
      points,
    });

    console.log(`Indexed ${chunks.length} chunks for document ${documentId}`);
  }

  // Search with filters
  async search(
    query: string,
    options: {
      topK?: number;
      filter?: any;
      scoreThreshold?: number;
    } = {}
  ) {
    const { topK = 5, filter, scoreThreshold = 0.7 } = options;

    // Generate query embedding
    const queryEmbedding = await this.generateEmbedding(query);

    // Search in Qdrant
    const results = await qdrant.search(this.collectionName, {
      vector: queryEmbedding,
      filter,
      limit: topK,
      with_payload: true,
      score_threshold: scoreThreshold,
    });

    return results;
  }

  // RAG query with LLM
  async query(
    userQuery: string,
    options: {
      topK?: number;
      filter?: any;
      systemPrompt?: string;
      model?: string;
      temperature?: number;
    } = {}
  ): Promise<{
    answer: string;
    sources: any[];
    usage: any;
  }> {
    const {
      topK = 5,
      filter,
      systemPrompt = 'You are a helpful assistant. Answer based on the provided context.',
      model = 'gpt-4',
      temperature = 0.7,
    } = options;

    // Retrieve relevant context
    const searchResults = await this.search(userQuery, { topK, filter });

    // Build context
    const context = searchResults
      .map((result, i) => {
        const payload = result.payload as any;
        return `[${i + 1}] ${payload.text}`;
      })
      .join('\n\n');

    // Generate response
    const completion = await openai.chat.completions.create({
      model,
      messages: [
        { role: 'system', content: systemPrompt },
        {
          role: 'user',
          content: `Context:\n${context}\n\nQuestion: ${userQuery}\n\nAnswer based on the context above. If the context doesn't contain relevant information, say so.`,
        },
      ],
      temperature,
    });

    return {
      answer: completion.choices[0].message.content || '',
      sources: searchResults.map((r, i) => ({
        index: i + 1,
        score: r.score,
        payload: r.payload,
      })),
      usage: completion.usage,
    };
  }

  // Update document
  async updateDocument(
    documentId: string,
    newContent: string,
    metadata: Record<string, any>
  ): Promise<void> {
    // Delete old chunks
    await qdrant.delete(this.collectionName, {
      wait: true,
      filter: {
        must: [
          {
            key: 'documentId',
            match: { value: documentId },
          },
        ],
      },
    });

    // Reindex with new content
    await this.indexDocument(documentId, newContent, metadata);
  }

  // Delete document
  async deleteDocument(documentId: string): Promise<void> {
    await qdrant.delete(this.collectionName, {
      wait: true,
      filter: {
        must: [
          {
            key: 'documentId',
            match: { value: documentId },
          },
        ],
      },
    });
  }
}

export const ragSystem = new RAGSystem();
```

### RAG API Implementation

```typescript
// app/api/rag/query/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { ragSystem } from '@/lib/rag-system';

export async function POST(request: NextRequest) {
  try {
    const { query, userId, topK = 5 } = await request.json();

    if (!query) {
      return NextResponse.json(
        { error: 'Query is required' },
        { status: 400 }
      );
    }

    // Query with user filter
    const result = await ragSystem.query(query, {
      topK,
      filter: userId ? {
        must: [
          {
            key: 'userId',
            match: { value: userId },
          },
        ],
      } : undefined,
    });

    return NextResponse.json({
      success: true,
      ...result,
    });
  } catch (error) {
    console.error('RAG query error:', error);
    return NextResponse.json(
      { error: 'Query failed' },
      { status: 500 }
    );
  }
}
```

### Document Indexing API

```typescript
// app/api/rag/index/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { ragSystem } from '@/lib/rag-system';

export async function POST(request: NextRequest) {
  try {
    const { documentId, content, metadata } = await request.json();

    if (!documentId || !content) {
      return NextResponse.json(
        { error: 'documentId and content are required' },
        { status: 400 }
      );
    }

    await ragSystem.indexDocument(documentId, content, metadata);

    return NextResponse.json({
      success: true,
      message: 'Document indexed successfully',
    });
  } catch (error) {
    console.error('Indexing error:', error);
    return NextResponse.json(
      { error: 'Indexing failed' },
      { status: 500 }
    );
  }
}
```

## Streaming AI Responses

### Streaming Implementation

```typescript
// lib/streaming-rag.ts
import OpenAI from 'openai';
import { ragSystem } from './rag-system';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! });

export async function* streamRAGResponse(
  query: string,
  options: {
    topK?: number;
    filter?: any;
    model?: string;
  } = {}
): AsyncGenerator<string, void, unknown> {
  // Retrieve context
  const searchResults = await ragSystem.search(query, options);

  const context = searchResults
    .map((r, i) => `[${i + 1}] ${(r.payload as any).text}`)
    .join('\n\n');

  // Stream completion
  const stream = await openai.chat.completions.create({
    model: options.model || 'gpt-4',
    messages: [
      {
        role: 'system',
        content: 'Answer based on the provided context.',
      },
      {
        role: 'user',
        content: `Context:\n${context}\n\nQuestion: ${query}`,
      },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content || '';
    if (content) {
      yield content;
    }
  }
}

// API route
// app/api/rag/stream/route.ts
export async function POST(request: NextRequest) {
  const { query, userId } = await request.json();

  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    async start(controller) {
      try {
        for await (const chunk of streamRAGResponse(query, {
          filter: userId ? {
            must: [{ key: 'userId', match: { value: userId } }],
          } : undefined,
        })) {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ content: chunk })}\n\n`));
        }
        controller.close();
      } catch (error) {
        controller.error(error);
      }
    },
  });

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}
```

## Cost Optimization

### Embedding Caching

```typescript
// lib/embedding-cache.ts
import { redis } from './redis';
import crypto from 'crypto';

export class EmbeddingCache {
  private ttl = 86400 * 7; // 7 days

  private getCacheKey(text: string, model: string): string {
    const hash = crypto.createHash('sha256').update(text).digest('hex');
    return `embedding:${model}:${hash}`;
  }

  async get(text: string, model: string): Promise<number[] | null> {
    const key = this.getCacheKey(text, model);
    const cached = await redis.get(key);
    return cached ? JSON.parse(cached) : null;
  }

  async set(text: string, model: string, embedding: number[]): Promise<void> {
    const key = this.getCacheKey(text, model);
    await redis.setex(key, this.ttl, JSON.stringify(embedding));
  }

  async generateWithCache(
    text: string,
    model: string,
    generator: () => Promise<number[]>
  ): Promise<number[]> {
    const cached = await this.get(text, model);
    if (cached) {
      return cached;
    }

    const embedding = await generator();
    await this.set(text, model, embedding);
    return embedding;
  }
}

export const embeddingCache = new EmbeddingCache();
```

### Token Optimization

```typescript
// lib/token-optimizer.ts
import { encoding_for_model } from 'tiktoken';

export class TokenOptimizer {
  private encoder = encoding_for_model('gpt-4');

  countTokens(text: string): number {
    return this.encoder.encode(text).length;
  }

  truncateToTokenLimit(text: string, maxTokens: number): string {
    const tokens = this.encoder.encode(text);
    if (tokens.length <= maxTokens) {
      return text;
    }

    const truncated = tokens.slice(0, maxTokens);
    return this.encoder.decode(truncated);
  }

  optimizeContext(
    contexts: Array<{ text: string; score: number }>,
    maxTokens: number
  ): string {
    let currentTokens = 0;
    const selected: string[] = [];

    // Sort by score (descending)
    const sorted = contexts.sort((a, b) => b.score - a.score);

    for (const context of sorted) {
      const tokens = this.countTokens(context.text);

      if (currentTokens + tokens <= maxTokens) {
        selected.push(context.text);
        currentTokens += tokens;
      } else {
        // Try to fit partial context
        const remaining = maxTokens - currentTokens;
        if (remaining > 100) {
          const partial = this.truncateToTokenLimit(context.text, remaining);
          selected.push(partial);
        }
        break;
      }
    }

    return selected.join('\n\n');
  }
}
```

## Monitoring & Observability

### AI Metrics Tracking

```typescript
// lib/ai-metrics.ts
export class AIMetrics {
  async trackEmbeddingGeneration(
    duration: number,
    tokenCount: number,
    model: string
  ): Promise<void> {
    console.log({
      type: 'embedding_generation',
      duration,
      tokenCount,
      model,
      timestamp: new Date().toISOString(),
    });

    // Send to monitoring service (e.g., Sentry, Datadog)
  }

  async trackRAGQuery(
    query: string,
    duration: number,
    resultCount: number,
    llmTokens: number,
    cost: number
  ): Promise<void> {
    console.log({
      type: 'rag_query',
      queryLength: query.length,
      duration,
      resultCount,
      llmTokens,
      cost,
      timestamp: new Date().toISOString(),
    });
  }

  async trackSearchPerformance(
    query: string,
    duration: number,
    resultCount: number,
    topScore: number
  ): Promise<void> {
    console.log({
      type: 'vector_search',
      queryLength: query.length,
      duration,
      resultCount,
      topScore,
      timestamp: new Date().toISOString(),
    });
  }
}

export const aiMetrics = new AIMetrics();
```

## Production Best Practices

### Error Handling

```typescript
// lib/ai-error-handler.ts
export class AIErrorHandler {
  async withRetry<T>(
    operation: () => Promise<T>,
    options: {
      maxRetries?: number;
      backoff?: number;
    } = {}
  ): Promise<T> {
    const { maxRetries = 3, backoff = 1000 } = options;
    let lastError: Error;

    for (let i = 0; i < maxRetries; i++) {
      try {
        return await operation();
      } catch (error) {
        lastError = error as Error;

        // Don't retry on certain errors
        if (error.status === 401 || error.status === 403) {
          throw error;
        }

        if (i < maxRetries - 1) {
          await new Promise(resolve => setTimeout(resolve, backoff * (i + 1)));
        }
      }
    }

    throw lastError!;
  }

  async withFallback<T>(
    primary: () => Promise<T>,
    fallback: () => Promise<T>
  ): Promise<T> {
    try {
      return await primary();
    } catch (error) {
      console.warn('Primary operation failed, using fallback:', error);
      return await fallback();
    }
  }
}
```

### Rate Limiting

```typescript
// lib/ai-rate-limiter.ts
import { redis } from './redis';

export class AIRateLimiter {
  async checkLimit(
    userId: string,
    operation: 'embedding' | 'query' | 'index',
    limit: number,
    window: number = 3600
  ): Promise<{ allowed: boolean; remaining: number }> {
    const key = `ratelimit:${operation}:${userId}`;
    const current = await redis.incr(key);

    if (current === 1) {
      await redis.expire(key, window);
    }

    return {
      allowed: current <= limit,
      remaining: Math.max(0, limit - current),
    };
  }
}
```

## When to Engage

Consult the Railway AI Specialist when:

- Building RAG systems
- Implementing semantic search
- Integrating vector databases
- Optimizing AI costs
- Scaling AI workloads
- Implementing streaming responses
- Troubleshooting performance
- Planning AI architecture
- Implementing monitoring

## Deliverables

When engaged, expect:

1. **AI Architecture Design** - Complete system design
2. **RAG Implementation** - Production-ready RAG system
3. **Vector Database Setup** - Optimized Qdrant configuration
4. **Cost Optimization** - Caching and token management
5. **Monitoring Setup** - Performance and cost tracking
6. **API Implementation** - Complete AI APIs
7. **Documentation** - RAG system guides
8. **Performance Tuning** - Optimization recommendations
