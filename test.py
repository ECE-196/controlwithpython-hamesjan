from serial import Serial, SerialException

with Serial('/dev/cu.usbmodem14201', 9600) as ser:
    # while True:
    #     print(ser.readline().decode())
    # ser.write(bytes([0x1]))
    # input()
    ser.write(bytes([0x1]))
    print(ser.read() == bytes([0xaa]))

    ser.write(bytes([0x0]))
    print(ser.read() == bytes([0xaa]))

    ser.write(bytes([0x2]))
    print(ser.read() == bytes([0xff]))


# with Serial('/your/port', 9600) as ser:
    # keep port open to see the LED turn on
# import serial.tools.list_ports
# ports = serial.tools.list_ports.comports()

# for port, desc, hwid in sorted(ports):
#     print("{}: {} [{}]".format(port, desc, hwid))
