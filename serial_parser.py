#!/usr/bin/python
import os,serial,time

device_name="NA"
device_units=""
device_temp_dir="/tmp/PiSerialMySensors/"

if not os.path.exists(device_temp_dir):
    os.makedirs(device_temp_dir)

#setup serial port
ser = serial.Serial(
port='/dev/ttyACM0',\
baudrate=115200,\
parity=serial.PARITY_NONE,\
stopbits=serial.STOPBITS_ONE,\
bytesize=serial.EIGHTBITS,\
timeout=2)

if ser.isOpen():
    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()
        time.sleep(1)  #give the serial port sometime to receive the data
        numOfLines = 0
        while True:
            if ser.isOpen() is False:
                ser.open()
            response = ser.readline()
            #print("read data: " + response)
            if len(response) > 1:
                fields = response.split(";")
                node_id=fields[0]
            if len(response) >=2:    
                child_sensor_id=fields[1]
            if len(response) >=3:
                command=fields[2]
            if len(response) >=4:
                ack=fields[3]
            if len(response) >=5:
                type=fields[4]
            if len(response) >=6:
                payload=fields[5].rstrip()
                if node_id == "1":
                    if child_sensor_id == "0":
                        device_name="Media_Center_Temp"
                        device_units="degress F"
                    if child_sensor_id == "1":
                        device_name="Media_Center_Desired_Temp"
                        device_units="degrees F"
                    if child_sensor_id == "2":
                        device_name="Media_Center_HVAC_Mode"
                        device_units="mode"
                if node_id == "9":
                    if child_sensor_id == "0":
                        device_name="Kegerator_Lower_Zone_Temp"
                        device_units="degrees F"
                    if child_sensor_id == "1":
                        device_name="Kegerator_Upper_Zone_Temp"
                        device_units="degrees F"
                    if child_sensor_id == "2":
                        device_name="Kegerator_Tap_Left_PulseCount"
                        device_units="pulses"
                    if child_sensor_id == "4":
                        device_name="Kegerator_Tap_Mid_Left_PulseCount"
                        device_units="pulses"
                    if child_sensor_id == "6":
                        device_name="Kegerator_Tap_Mid_Right_PulseCount"
                        device_units="pulses"
                    if child_sensor_id == "8":
                        device_name="Kegerator_Tap_Right_PulseCount"
                        device_units="pulses"
                    if child_sensor_id == "10":
                        device_name="Kegerator_Desired_Temp"
                        device_units="degrees F"
                    if child_sensor_id == "11":
                        device_name="Kegerator_HVAC_Mode"
                        device_units="mode"
                if "TSP" not in payload:
                  print "Received data from device " + device_name + ": " + payload + " " + device_units
                  temp_filepath=device_temp_dir+device_name
                  temp_file=open(temp_filepath,"w")
                  temp_file.write(payload)
                  temp_file.close()
                #print "Raw data: " + response
            #print "Raw data from mysensors:" + "device name: " + device_name + " node ID: " + node_id + " child sensor ID: " + child_sensor_id + " command: " + command + " ack: " + ack + " type: " + type + " payload: " + payload
            #ser.close()
            time.sleep(1)
    except Exception, e1:
        print ("error communicating...: ") + str(e1)
else:
    print ("cannot open serial port ")
