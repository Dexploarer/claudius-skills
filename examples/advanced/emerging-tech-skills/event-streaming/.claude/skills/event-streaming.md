# Event Streaming Architecture

**Category:** Distributed Systems & Messaging
**Level:** Advanced
**Auto-trigger:** When user mentions Kafka, event streaming, event sourcing, or stream processing

---

## Description

Implements event streaming architectures using Apache Kafka, Pulsar, or cloud-native streaming services. Covers topics, partitioning, consumer groups, exactly-once semantics, and stream processing.

---

## Activation Phrases

- "Set up Kafka"
- "Create event streaming"
- "Implement event sourcing"
- "Configure stream processing"
- "Set up Kafka consumer"

---

## Core Concepts

### Producers & Consumers
```typescript
// Kafka producer
const producer = kafka.producer();
await producer.send({
  topic: 'user-events',
  messages: [
    { key: userId, value: JSON.stringify(event) }
  ]
});

// Kafka consumer with consumer group
const consumer = kafka.consumer({ groupId: 'analytics-group' });
await consumer.subscribe({ topic: 'user-events' });
await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    await processEvent(message.value);
  }
});
```

---

**Last Updated:** 2025-11-02
