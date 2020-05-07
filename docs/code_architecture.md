# Code Architecture

The entire code is written keeping interfaces in mind and not the implementations.
- This will allow us to swap out different implementations
- Factories are used to plug in the implementations

## Interfaces
- CacheInterface
  - Basic operations & attributes supported by a cache
- CacheItemInterface
  - Basic operations & attributes supported by a cache item
  