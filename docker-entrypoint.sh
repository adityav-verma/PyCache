#!/bin/bash

# A script failure should exist the shell
# https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
# https://explainshell.com/explain?cmd=set+-euxo%20pipefail#
set -exo pipefail

_start_application () {
  echo "Staring nginx"
  service nginx start

  echo "Staring uWSGI"
  uwsgi uwsgi.ini
}

run_dev () {
  echo "Starting cluster components"
  if [ $WORKER ]
  then
    echo "Starting replication worker: $WORKER"
    python start_workers.py $WORKER
    tail -f /dev/null
  else
    echo "Starting cache server"
    _start_application
  fi
}

run_dev