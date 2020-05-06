from enum import Enum


class CacheOperation(Enum):
    SET = 'set'
    GET = 'get'
    EXPIRE = 'expire'


class EventType(Enum):
    CACHE_SET = 'cache_set'
    CACHE_EXPIRE = 'cache_expire'


class CacheEventTopic:
    NAME = 'cache'
