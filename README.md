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

## API Documentation
[API documentation](./docs/api_doc.md)

## Architecture
[API documentation](./docs/architecture.md)