# Architecture

![Architecture diagram](architecture_diagram.png)

## Cache Server
A cache server has two parts:
- A `Flask application`, serving API requests, and managing in memory cache
- A `Background worker`, which subscribes to central commit log and syncs the messages with the flask server. 

## Load-Balancer
`Nginx` is used to balance the traffic between all the nodes in Round Robin Fashion.

If a node is down Nginx will:
- Automatically redirect the traffic to the next node
- Won't push traffic to this node for the next 10 secs

In production environment, we might want to handle this with liveness or readiness health checks.

## Commit Log
A central commit log is maintained using `Kafka`.

- All SET and EXPIRE operations are put on the commit log for other cache servers to replicate.
- Also since, the commit log is persisted, **we use this to bring a new node with sync to all other nodes, by replaying all the logs from the beginning.**

In production, we would preferably use a managed solution for this by using AWS or GCP.
