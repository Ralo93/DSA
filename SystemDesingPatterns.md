

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

In summary: Write to a message queue via a write service and have the workers/consumers update the databaset and write to the Cache.
Read from the Cache.

  ![image](https://github.com/user-attachments/assets/30e9b122-304b-4d6e-bb89-94f1f0bd866d)


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

- My to go choice is probably NGINX, as it supports HTTP, TCP, various balancing algorithms like IP-Hash or Round-Robin and can run on windows, mac and linux. And it can also run as a service in a docker container!

## Fault tolerance mechanisms


## Data Architecture
Understanding of data lakes, data warehouses, and data marts.

Knowledge of batch vs. real-time processing.

Event-driven architectures.

## Distributed Systems

Understanding of distributed computing principles.

CAP theorem, consistency models, and fault tolerance.
