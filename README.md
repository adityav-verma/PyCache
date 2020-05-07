# PyCache
A distributed in memory key-value store.

## How to setup and run
### Prerequisites
* [Docker](https://www.docker.com/products/docker-desktop)
* [Docker Compose](https://docs.docker.com/compose/)
The application uses docker containers and docker-compose to run multiple containers to simulate a cluster of nodes.
### Steps
1. Clone the repository
2. Navigate inside the directory
3. Copy the sample config to actual config by
	1.  `cp app/config.py.sample app/config.py`
4. Make sure docker is running
5. Run docker compose to start the cluster
	1. `docker-compose up`

Have a look at the API documentation ADD LINK HERE

### Tricky stuff
Often times, killing docker-compose and restart it might fail, since Kafka is not able to create a resource in Zookeeper. For this, wait for 1 min, then kill and start docker compose again.

**Why does this happen?**
When Kafka starts, it registers it’s own broker with Zookeeper, however, if we kill docker compose, Kafka misses the chance the de register itself. On next start it tries to do the same thing, but fails. Zookeeper after a min cleans up any dangling registrations. Hence we can restart and things work again.

## API Documentation
[API documentation](./docs/api_doc.md)

## Architecture

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