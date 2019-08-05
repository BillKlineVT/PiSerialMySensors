#!/bin/bash

file=/tmp/PiSerialMySensors/Media_Center_Desired_Temp
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
