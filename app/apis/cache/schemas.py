from app.constants import CacheOperation

NumberCacheItem= {
    'type': 'number'
}


StringCacheItem = {
    'type': 'string',
    'minLength': 1
}


ObjectCacheItem = {
    'type': 'object'
}


ListItemValue = {
    'type': "array",
    "minItems": 1
}


CacheItemValue = {
    "anyOf": [NumberCacheItem, StringCacheItem, ObjectCacheItem, ListItemValue]
}


SyncPayload = {
    'type': 'object',
    'properties': {
        'operation': {
            'type': 'string',
            'enum': [CacheOperation.SET.value, CacheOperation.EXPIRE.value]
        },
        'key': {'type': 'string'},
        'value': CacheItemValue
    },
    'required': ['operation', 'key']
}