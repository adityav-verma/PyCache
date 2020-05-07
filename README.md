# PyCache
A distributed in memory key-value store.

## Architecture
The system is divided into the following components:
- Queries:
    - A `Flask API server`, which has a REST API interface for clients to consume
        - 3 containers of the flask server are run, to simulate 3 nodes, however, the system works for `n` nodes
- Load balancing:
    - `Nginx` is configured to distribute load between the nodes/containers in a round robin manner. Can horizontally scale the containers now.
- Replication across nodes:
    - Publisher/Subscriber mechanism is used for replication
    - `Kafka` is used as a kind of external commit-log, every add/expire operation is added to the log
    - Along with an app server, the containers also have a `worker/consumer` process running, which consumes the commit log and updates the in memory data
- Fault tolerance:
    - If a server goes down, Nginx forwards the request to next one. There by not impacting the client.
    - When a server comes back up, it can replay the entire commit log, and be back in sync with other servers

### Application Server
The server is a flask application, served via Nginx and a single worker of uWSGI.

**Why a single worker setup?**
A single worker is used as sharing memory across different worker processes/threads is not that straight forward, and would require using uWSGI cache or shared memory APIs. Can pick this as an improvement later on.

### Cache?
Cache is a Singleton class, which adheres to a `CacheInterface`, so that different implementations can swapped in or out without changing the core `CacheManager`.

### Sync?
Sync between different instances (nodes) of the cache sever is done via a `Pub/Sub` model

- `Kafka` is used as a shared log between instances.
  - A simple message queue like SQS is not used, since we need to persist data. A message queue looses the data, once it is consumed by the consumer.
- Any Create/Update/Delete operation is added to the shared log.
- Each cache server is paired with a log consumer, which reads the log and updates it's respective cache server

### Addition of new node / Restart of a node?
This uses the same `Pub/Sub` model. Every server, on startup, will start reading the log from the beginning and will eventually come in sync with the other servers.

**Limitation with the current approach?**
- In a production setup, the sever should not serve traffic unless it's completely in sync, to avoid state reads or cache misses
