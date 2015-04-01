import serial

ser = serial.Serial('/dev/ttyAMA0', 4800)
ser.write("!")
ser.write("\n")

ser.close()
