## API Documentation

There are two API Hosts

**Load Balancer:**

`http://localhost:5000/`

This is going to route the request via Nginx, in Round Robin fashion


**Individual nodes:**

`http://localhost:8001/`, `http://localhost:8002/`, `http://localhost:8003/`

This will directly hit the node. Useful for testing node failure or replication.

### SET a Key and Value pair
**URL and method**

`POST <api_host>/api/cache/<key_name>/`

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


### GET the Value for a Key
**URL and method**

`GET <api_host>/api/cache/<key_name>/`

**Payload**
NA

**Response**:
```
200
{
    "message": "Cache key get success",
    "payload": {
        "key": <key_name>,
        "value": <value>,
        "last_updated_at": <datetime string in utc>
    }
}

```



### EXPIRE a Key
**URL and method**

`DELETE <api_host>/api/cache/<key_name>/`

**Payload**
NA

**Response**:
```
200
{
    "message": "Cache key expired",
    "payload": {}
}

```