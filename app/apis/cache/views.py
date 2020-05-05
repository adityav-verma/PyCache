from http import HTTPStatus

from flask import Blueprint, request

from app.app import cache_obj

from app.utilities import ApiResult

cache = Blueprint('cache', __name__, url_prefix='/api/cache')


@cache.route('/<string:cache_key>/', methods=['POST'])
def set_key(cache_key):
    # TODO: Support string, int, list and object
    value = request.json
    cache_item = cache_obj.set(cache_key, value)
    return ApiResult(payload=cache_item.value, message='Cache key set success', status=HTTPStatus.CREATED)


@cache.route('/<string:cache_key>/', methods=['GET'])
def get_key(cache_key):
    cache_item = cache_obj.get(cache_key)
    return ApiResult(payload=cache_item, message='Cache key get success', status=HTTPStatus.OK)


@cache.route('/<string:cache_key>/', methods=['DELETE'])
def expire_key(cache_key):
    cache_obj.expire(cache_key)
    return ApiResult(payload={}, message='Cache key expired', status=HTTPStatus.OK)
