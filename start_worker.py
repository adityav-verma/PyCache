import sys

from app.app import create_app


worker_name = sys.argv[1]
app_host = 'http://localhost/'


worker_app = create_app()

with worker_app.test_request_context(app_host):
    if worker_name == 'replication':
        while True:
            pass
    else:
        raise Exception('Invalid worker name')
