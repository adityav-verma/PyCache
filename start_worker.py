import sys
import os

from app.app import create_app


worker_name = sys.argv[1]
app_host = os.environ['APPLICATION_HOSTNAME']


worker_app = create_app()

with worker_app.test_request_context(app_host):
    if worker_name == 'sync':
        pass
    else:
        raise Exception('Invalid worker name')
