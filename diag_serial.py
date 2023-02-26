import serial
import time
ser = serial.Serial('\\.\\COM3', timeout=2, baudrate=10400)
# ser.open()

ser.write(b'ATZ\r')
print(ser.readlines())

ser.write(b"0105\r")
engine_coolant_temperature = ser.readlines()
print(engine_coolant_temperature)
data = engine_coolant_temperature[1].decode()
datatype = data[:5]
value =data[6:8]
print(f'datatype: {datatype} value: {value} in Celsius: {int(value, base=16)-40}')


ser.write(b"010C\r")
rpm = ser.readlines()
print(rpm)
data = rpm[1].decode()
datatype = data[:5]
value =data[6:8] + data[9:11]
print(f'datatype: {datatype} value: {value} in RPM: {int(value, base=16)/4}')

#  OSError(22, 'A szemaforhoz rendelt hat�rid� lej�rt.'
# [b'ATZ\rELM327 v1.5 
