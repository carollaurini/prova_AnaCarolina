#!/bin/bash

container=''
CMD='docker-compose '
CMD_OPT=''

help () {
  echo "help:"
  echo "--start"
  echo "--stop"
  echo "exemple of use: ./run.sh --up"
}

while [ "$1" != "" ]; do
  PARAM=`echo $1 | awk -F= '{print $1}'`
  case $PARAM in
    -h | --help)
      help
      exit
    ;;
    --start)
      echo "[UP DEV]"
      CMD_OPT='up'
    ;;
    --start-bg)
      echo "[UP DEV]"
      CMD_OPT='up -d'
    ;;
    --stop)
      echo "[DOWN DEV]"
      CMD_OPT='down'
    ;;
    *)
      echo "ERROR: unknown parameter \"$PARAM\""
      usage
      exit 1
    ;;
  esac
  shift
done

if [ -z "$CMD_OPT" ]; then
  echo "ERROR: unknown parameter" 
else
  ${CMD} ${CMD_OPT}
fi
