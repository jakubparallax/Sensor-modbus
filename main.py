import serial
import minimalmodbus
from time import sleep

client1 = minimalmodbus.Instrument('/dev/cu.usbserial-B002EFSZ', 17, debug=False)
client1.serial.baudrate = 9600
client1.serial.parity   = serial.PARITY_EVEN
client1.serial.stopbits = 1
client1.serial.timeout  = 1
client1.address         = 17
client1.mode = minimalmodbus.MODE_RTU
client1.clear_buffers_before_each_transaction = True

attempts = 0
success = 0

while True:
    attempts += 1
    try:
        result = client1.read_registers(40000, 1)[0]
        success += 1
        print("Response: " + str(result))
    except:
        print("No response")
    print("\nSuccess probability: " + str((success / attempts) * 100) + "%")
    sleep(5)
