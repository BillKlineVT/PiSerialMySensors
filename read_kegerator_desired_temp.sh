#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_Desired_Temp
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
