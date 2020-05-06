from http import HTTPStatus

from app.factories.in_memory_cache_factory import InMemoryCacheFactory
from app.managers.cache_event_observer import CacheEventObserver
from app.managers.cache_manager import CacheManager
from .config import Config
from .api_flask import ApiFlask
from .exceptions import ApiException
from .utilities.api_result import ApiResult


# For import *
__all__ = ['create_app', 'cache_manager']

# Init a cache
cache_manager = CacheManager(InMemoryCacheFactory())
cache_event_observer = CacheEventObserver()


def create_app(config=None, app_name=None):
    """Create an app instance based on the passed params"""
    # Should only be called in production/staging environment, can be handled
    # in the library
    if not app_name:
        app_name = Config.APP_NAME

    app = ApiFlask(app_name)

    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    """Load config to the app and add additional configurations if needed
    http://flask.pocoo.org/docs/0.12/api/#configuration
    """
    # Load the default config
    app.config.from_object(Config)

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    pass


def configure_blueprints(app):
    """Register all blueprints with the app"""
    from .apis.health import health
    from .apis.cache import cache
    for bp in [health, cache]:
        app.register_blueprint(bp)


def configure_error_handlers(app):
    """Configure automatic exception handling"""
    def handle_custom_api_exception(e):
        return e.to_result()

    def handle_unknown_exception(e):
        return ApiResult({}, str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

    app.register_error_handler(ApiException, handle_custom_api_exception)
    app.register_error_handler(Exception, handle_unknown_exception)

    # Jsonschema error handlers start block
    from jsonschema.exceptions import ValidationError, SchemaError
    app.register_error_handler(
        ValidationError, lambda err: ApiResult(
            {'error': str(err)}, 'Invalid request body', HTTPStatus.BAD_REQUEST
        )
    )
    app.register_error_handler(
        SchemaError, lambda err: ApiResult(
            {'error': str(err)}, 'Invalid schema at server',
            HTTPStatus.INTERNAL_SERVER_ERROR
        )
    )
    # Jsonschema error handlers end block
