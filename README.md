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

### Tricky stuff
Often times, killing docker-compose and restarting it might fail, since Kafka is not able to create a resource in Zookeeper. For this, wait for 1 min, then kill and start docker compose again.

**Why does this happen?**

When Kafka starts, it registers it’s own broker with Zookeeper, however, if we kill docker compose, Kafka misses the chance to de-register itself.

On the next start it tries to do the same thing, but fails. Zookeeper after a min cleans up any dangling registrations. Hence we can restart and things work again.


## Various cases to validate

### Basic SET, GET and EXPIRE operations
The API requests can be made to the load-balancer which will route them in round robin fashion, or to the individual nodes as well.

Refer to [API documentation](./docs/api_doc.md) for more details on both. 


### Node failure
We can simulate a node failure, by killing a container using docker. In the default setup, 3 cache containers are running, which we are free to kill.

```
# List all running containers
docker ps

# Kill the container whose name has `cache`
docker kill <container_name>
```
After killing the node, the APIs should still work, as the load-balancer will route them elsewhere.

We can even kill all the containers, however, the APIs will stop at this point.


### Node Reboot
We can simulate a node reboot/reattachment, by starting the container(s) using docker.

```
# List all containers, running and exited
docker ps -a

# Start the container whose name has `cache`
docker start <container_name>
```
**The node, after startup, will replay all the data from the commit log and will be in sync with other nodes.**

In production setup, we won't attach the node to the load-balancer until it has completed the sync (using readiness probe or something similar). However, in docker-compose there is no such option.


## API Documentation
[API documentation](./docs/api_doc.md)

## Architecture
[Architecture documentation](./docs/architecture.md)