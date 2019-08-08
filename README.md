# PiSerialMySensors

The purpose of this project is to integrate two of my home automation projects together.

I have had several [MySensors](https://www.mysensors.org/) related IoT projects up and running in my house for a couple of years now.  One of them was a re-purposed top freezer/bottom refrigerator and converting it to a 4-tap kegerator with dual-zone refrigeration control.  The other was a temperature-controlled fan controller inside an enclosed media center cabinet to allow for cooling air flow around the electronics. While the IoT projects continued to run (Arduino based) and transmit (NRF24 based) stable as a rock, the home automation hub I started with (OpenHAB2 on Raspberry Pi) fizzled out when I moved to the SmartThings Hub.  This left me no way to capture the wonderful stats being transmitted ever-so-reliabliy.

I then learned about a wonderful open source library called [ST_Anything](https://github.com/DanielOgorchock/ST_Anything) which allowed ESP8266 IoT microcontrollers to appear as SmartThings devices on your SmartThings Hub.  I added one of these and had great success with the interface (wireless outdoor motion sensors acting as SmartThings devices).  Then, recently, I noticed that the same author of ST_Anything made [OmniThing](https://github.com/DanielOgorchock/OmniThing), which allows Raspberry Pi-based projects to also connect as SmartThings deviced to the SmartThings hub.

This project allows a Raspberry Pi connected via USB-serial connection to an Arduino running the [MySensors Serial Gateway](https://www.mysensors.org/build/serial_gateway) to parse the data format and send it on to SmartThings via the OmniThing library.

TODO: Remove /tmp-based file IO storing of latest value to a SQL or time-series database for storage.

TODO: Add config file to define node IDs of MySensors network which will remove the hard-coded ladder logic of parsing data.

SmartThings iOS app with ST_Anything and OmniThing devices appearing:

<img src="https://github.com/BillKlineVT/PiSerialMySensors/blob/master/screenshots/SmartThings%20App.JPG" alt="" height="200"/>

SmartThings OmniThing devices logged using [SmartThings InfluxDB Logger](https://github.com/codersaur/SmartThings/tree/master/smartapps/influxdb-logger) connected to Raspberry Pi-hosted Grafana server:

<img src="https://github.com/BillKlineVT/PiSerialMySensors/blob/master/screenshots/Grafana-SmartThings-OmniThing-MySensors-Integration.JPG" alt="" height="200"/>
