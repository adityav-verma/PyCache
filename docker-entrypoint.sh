#!/bin/bash

# A script failure should exist the shell
# https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
# https://explainshell.com/explain?cmd=set+-euxo%20pipefail#
set -exo pipefail

_start_application () {
  echo "Staring server"

  echo "Staring nginx"
  service nginx start

  echo "Staring uWSGI"
  uwsgi uwsgi.ini
}

_start_worker () {
  echo "Starting replication worker"
  python -u start_worker.py 'replication' > 'replication_logs.txt' &
}

run () {
  python -u wait_for_dependencies.py
  echo "Starting cluster components"
  _start_worker
  _start_application
}

run