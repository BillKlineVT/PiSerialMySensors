#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_Tap_Right_PulseCount
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
