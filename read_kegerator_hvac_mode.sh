#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_HVAC_Mode
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
