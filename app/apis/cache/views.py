from http import HTTPStatus

from flask import Blueprint, request

from app.apis.cache.schemas import SyncPayload, CacheItemValue
from app.app import cache_manager

from app.utilities import ApiResult
from app.utilities.schema_validators import validate_request_schema

cache = Blueprint('cache', __name__, url_prefix='/api/cache')


@cache.route('/<string:cache_key>/', methods=['POST'])
@validate_request_schema(CacheItemValue)
def set_key(cache_key):
    # TODO: Support string, int, list and object
    value = request.json
    cache_item = cache_manager.set(cache_key, value)
    return ApiResult(
        payload=cache_item.to_dict(), message='Cache key set success',
        status=HTTPStatus.CREATED
    )


@cache.route('/<string:cache_key>/', methods=['GET'])
def get_key(cache_key):
    cache_item = cache_manager.get(cache_key)
    return ApiResult(
        payload=cache_item.to_dict() if cache_item else {},
        message='Cache key get success',
        status=HTTPStatus.OK
    )


@cache.route('/<string:cache_key>/', methods=['DELETE'])
def expire_key(cache_key):
    cache_manager.expire(cache_key)
    return ApiResult(payload={}, message='Cache key expired', status=HTTPStatus.OK)


@cache.route('/sync/', methods=['POST'])
@validate_request_schema(SyncPayload)
def sync():
    data = request.json
    cache_manager.sync(data['key'], data['value'], data['operation'])
    return ApiResult(payload={}, message='Cache key synced', status=HTTPStatus.OK)
