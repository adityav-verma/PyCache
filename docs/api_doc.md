## API Documentation
The cluster supports 3 operations
* SET a Key and Value pair
* GET the value for a Key
* EXPIRE a Key

### SET a key
**URL and method**
 `POST http://localhost:5000/api/cache/<key_name>/`

**Payload**
The value can be a String, Number, List and Object. The following JsonSchema can be used for the payload

```
NumberCacheItem = {
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
```

**Response**:
```
201
{
    "message": "Cache key set success",
    "payload": {
        "key": <key_name>,
        "value": <value>,
        "last_updated_at": <datetime string in utc>
    }
}

```
