#!/bin/bash

file=/tmp/PiSerialMySensors/Media_Center_HVAC_Mode
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
