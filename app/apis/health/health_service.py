class HealthService:
    @classmethod
    def get_health_status(cls):
        # Validate any external connections, etc
        status = {'message_broker': 'ok'}
        return status
