#!/bin/bash

# echo "About to sleep for 5";
# echo "About to look at kb deployment user-env";


. /kb/deployment/user-env.sh

python ./scripts/prepare_deploy_cfg.py ./deploy.cfg ./work/config.properties

if [ -f ./work/token ] ; then
  export KB_AUTH_TOKEN=$(<./work/token)
fi

if [ $# -eq 0 ] ; then
  sh ./scripts/start_server.sh
elif [ "${1}" = "test" ] ; then
  echo "Run Tests"
  make test
elif [ "${1}" = "async" ] ; then
  sh ./scripts/run_async.sh
elif [ "${1}" = "init" ] ; then
  echo "Initialize module"
  echo "Initialize module"
  cd /data
  curl -s http://bioseed.mcs.anl.gov/~chenry/kmer.tgz|tar xzf -
  ln -s /data/kmer/Release70 /data/kmer/ACTIVE/Release70
  ln -s /data/kmer/Release70 /data/kmer/DEFAULT
  if [ -d kmer ] ; then
  	touch __READY__
  else
    echo "Init failed"
  fi
elif [ "${1}" = "bash" ] ; then
  bash
elif [ "${1}" = "report" ] ; then
  export KB_SDK_COMPILE_REPORT_FILE=./work/compile_report.json
  make compile
else
  echo Unknown
fi
