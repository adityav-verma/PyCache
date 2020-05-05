from flask import Blueprint

from app.utilities import ApiResult
from .health_service import HealthService

health = Blueprint('dummy', __name__, url_prefix='/api/health')


@health.route('/', methods=['GET'])
def index():
    data = HealthService.get_health_status()
    return ApiResult(
        payload=data,
        message='It works!!!'
    )