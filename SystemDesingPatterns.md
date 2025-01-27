

# Basics of System Design


# Non Functional Requirements

## Scalability: How systems handle growing amounts of data or traffic.

- Decomnposition: Breaking down requirements into microservices, each having a single responsibility.
Uses an API gateway (like NGINX or Envoy) to route, rate limit and aggregate answers to and from different microservices.

- Horizontal scaling means using more duplicated application services (stateless) to load balance.
- Scaling of ML models is also possible, making them faster or more complex and slower sometimes.

- Vertical Scaling means using more powerful machines.

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
