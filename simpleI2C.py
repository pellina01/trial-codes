import sys
import smbus2 as smbus  # ,smbus2
import time

# Slave Addresses
I2C_SLAVE_ADDRESS = 11  # 0x0b ou 11
I2Cbus = smbus.SMBus(1)
# This function converts a string to an array of bytes.


def ConvertStringsToBytes(src):
    converted = bytes(src, "utf-8")
    convert = []
    for byte in converted:
        convert.append(byte)
    return convert


while True:
    string = input("enter command")
    byte = ConvertStringsToBytes(string)
    if string == "0":
        response = I2Cbus.read_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, 2)
        # print(''.join(response).decode('utf-8'))
        print(bytearray(response).decode("utf-8"))
    else:
        I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, byte)
