#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_Lower_Zone_Temp
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
