from enum import Enum


class CacheOperation(Enum):
    SET = 'set'
    GET = 'get'
    EXPIRE = 'expire'
