import serial,time

#ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

device_name="n/a"

ser = serial.Serial(
port='/dev/ttyACM0',\
baudrate=115200,\
parity=serial.PARITY_NONE,\
stopbits=serial.STOPBITS_ONE,\
bytesize=serial.EIGHTBITS,\
timeout=2)

if ser.isOpen():
    try:
        print "isOpen = true"
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()
        time.sleep(1)  #give the serial port sometime to receive the data
        numOfLines = 0
        while True:
            if ser.isOpen() is False:
                ser.open()
            response = ser.readline()
            print("read data: " + response)
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
                payload=fields[5]
                if node_id == "1":
                    if child_sensor_id == "0":
                        device_name="Media_Center_Temp"
                    if child_sensor_id == "1":
                        device_name="Media_Center_Desired_Temp"
                    if child_sensor_id == "2":
                        device_name="Media_Center_HVAC_Mode"
                if node_id == "9":
                    if child_sensor_id == "0":
                        device_name="Lower_Beer_Fridge_Temp"
                    if child_sensor_id == "1":
                        device_name="Upper_Beer_Fridge_Temp"
                    if child_sensor_id == "2":
                        device_name="Kegerator Tap Left PulseCount"
                    if child_sensor_id == "4":
                        device_name="Kegerator Tap Mid-Left PulseCount"
                    if child_sensor_id == "6":
                        device_name="Kegerator Tap Mid-Right PulseCount"
                    if child_sensor_id == "8":
                        device_name="Kegerator Tap Right PulseCount"
                    if child_sensor_id == "10":
                        device_name="Kegerator Desired Temperature"
                    if child_sensor_id == "11":
                        device_name="Kegerator HVAC Mode"
            print "Received data from mysensors:" + "device name: " + device_name + " node ID: " + node_id + " child sensor ID: " + child_sensor_id + " command: " + command + " ack: " + ack + " type: " + type + " payload: " + payload
            #ser.close()
            time.sleep(1)
    except Exception, e1:
        print ("error communicating...: ") + str(e1)
else:
    print ("cannot open serial port ")
