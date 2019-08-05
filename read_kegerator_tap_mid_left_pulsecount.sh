#!/bin/bash

file=/tmp/PiSerialMySensors/Kegerator_Tap_Mid_Left_PulseCount
if [ -e $file ]; then
  cat $file
else
  echo "unknown"
fi
