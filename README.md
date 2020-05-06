# PyCache
A distributed in memory key value store

## Architecture
The system is distributed in the sense:
- Every node/server is a flask application, which supports Rest APIs to set, get and expire a key
- Nginx distributes load between the servers, hence making it possible to scale the system horizontally
- A users could directly make an API call to a server, by using it's address rather than Nginx
- Since, every node is acting as a master in this setup, syncing is done using Pub/Sub model

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
