# Code Architecture

The entire code is written keeping interfaces in mind and not the implementations.
- This will allow us to swap out different implementations
- Factories are used to plug in the implementations

## Interfaces
- CacheInterface
  - Basic operations & attributes supported by a cache
- CacheItemInterface
  - Basic operations & attributes supported by a cache item
- EvictionPolicyInterface
  - Basic operations & attributes supported by a it
- CacheFactoryInterface
- SubscriberInterface
   - Commit log subscriber interface
- PublisherInterface
  - Commit log subscriber interface
- EventInterface, EventQueueInterface


## Components
- CacheManager is the component, with which the view interacts
  - It creates a new cache via factory
  - Plugs in the eviction policy
  - **New cache and policy can be plugged in from here**

- Replication worker
  - Subscribes to the commit log and updates the server cache via localhost API call
  - A new commit log can be plugged in here

- KafkaPublisher, KafkaSubscriber
  - Used to publish and subscribe from the commit log
  - A new commit log other than Kafka can be added which adheres to the interface
   
- Event, CacheEvent, EventQueue
- CacheEventObserver
  - Listens for a new event in the queue and publishes to commit log
  - A new commit log can be plugged in here