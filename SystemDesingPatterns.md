

# Basics of System Design


# Non Functional Requirements

## Scalability: How systems handle growing amounts of data or traffic.

- Decomnposition: Breaking down requirements into microservices, each having a single responsibility.
Uses an API gateway (like NGINX or Envoy) to route, rate limit and aggregate answers to and from different microservices.

- Horizontal scaling means using more duplicated application services (stateless) to load balance.
- Scaling of ML models is also possible, making them faster or more complex and slower sometimes.

- Vertical Scaling means using more powerful machines.

- Caching: Storing hot-data in memory for fast access, reducing load on the database.

- Buffer with message queues: High frequent write operations can put a strain on the database. Message queues work as a buffer, transforming synchronous operations into asynchronous.

- Seperating Read and Write in either READ-HEAVY or WRITE-HEAVY Systems: In most business use cases these should be handled differently:
  1. Replication implements a Leader-Follower architecture:
     - All Writes are routed to the leader, ensuring consistency.
     - Reads are distributed across followers, improving read scalability.
     - Fault Tolerance: If the leader fails, a follower can be promoted.
     - Used in read or write heavy systems.
  2. CQRS (Command Query Responsibility Segregation)
     - Using completely different data models for read and write operations.
     - Normalized data model optimized for writes. (Command side)
     - Denormalized data model optimized for reads.
     - Asynchronous update between to the.
     - Used in very complex query or different read and write scalability requirements.

## Reliability (Robustness): Ensuring systems are fault-tolerant and can recover from failures.

-

## Performance: Optimizing systems for speed and efficiency.

## Security: Protecting data and systems from unauthorized access.





## Microservices

## Event-driven architectures

## Batch vs stream processing

## Caching strategies

## Load balancing:

- Redirecting (routing) requests to different application servers to handle high-load scenarios. This is usually done with Round-Robin, Weightened Round-Robin, Hash-based (for user persistance) or Least connections algorithms.

## Fault tolerance mechanisms


## Data Architecture
Understanding of data lakes, data warehouses, and data marts.

Knowledge of batch vs. real-time processing.

Event-driven architectures.

## Distributed Systems
Understanding of distributed computing principles.

CAP theorem, consistency models, and fault tolerance.
