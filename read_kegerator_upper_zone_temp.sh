#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_Upper_Zone_Temp
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
