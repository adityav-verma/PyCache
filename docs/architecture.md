## Architecture
### Queries
* A `Flask API server`, which has a REST API interface for clients to consume
* 3 containers of the flask server are run, to simulate 3 nodes, however, the system works for `n` nodes

### Load Balancing
* `Nginx` is configured to distribute load between the nodes/containers in a round robin manner. Can horizontally scale the containers now.

### Replication across nodes:
* Publisher/Subscriber mechanism is used for replication
*  `Kafka` is used as a kind of external commit-log, every add/expire operation is added to the log
* Along with an app server, the containers also have a `worker/consumer` process running, which consumes the commit log and updates the in memory data

### Fault tolerance:
* If a server goes down, Nginx forwards the request to next one. There by not impacting the client.
* When a server comes back up, it can replay the entire commit log, and be back in sync with other servers