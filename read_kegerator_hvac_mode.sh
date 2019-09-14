#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_HVAC_Mode
if [ -e $file ]; then
  if [[ `cat $file` == "Off" ]]; then
    echo "0"
  elif [[ `cat $file` == "CoolOn" ]]; then
    echo "1"
  elif [[ `cat $file` == "Circulate" ]]; then
    echo "2"
  else
    echo "-1"
  fi

else
  echo "-1"
fi
