# ******************************************************
#  Raspberry Pi / Jetson Nano library for MCP41HVX1 digital potentiometers
#
#  Author: OneLife d2nnis@hotmail.com
#
#  Version: v0.0.5 beta
#  License: Apache 2.0
# *******************************************************

import spidev #pip3 install spidev
import time

# To activate spi function in Jetson Nano
    # Method 1 - using subprocess to activate
    #import subprocess
    #subprocess.run(['sudo', 'modprobe', 'spidev'])
    
    # Method 2 - activate in terminal
    # sudo modprobe spidev

class MCP41HVX1(object):

    def __init__(self,a,b):
        # jetson spi pinout : pin22 = CS0, pin 19,21,23 = MO, MI, SCK
        self.spi = spidev.SpiDev()
        self.spi.open(a,b)   # select the SPI device
        self.spi.max_speed_hz = 10000000  # speed of the SPI clock

    # define a function to send 2 bytes
    def write_pot(self,input):
        try:
            msb=input>>8 & 0xff  # shift the value 8 bits left so the row number is stored in msb
            lsb = input & 0xff # using binary AND to extract the ON OFF pattern to lsb
            print(msb, " | ", lsb)
            self.spi.xfer([msb,lsb])  # send the data array based on spi mechanism

        except IOError:
            #print("ReadError: wiper 0")
            return (0)

    def WiperGetPosition(self):
        try:
            cmd = 0x0c00
            arr = self.spi.xfer([cmd >> 8, cmd & 0xff])

        except IOError:
            #print("ReadError: wiper 0")
            return (0)

        else:
            return (arr[0] << 8 | arr[1] & 0xff) & 0xff

def main():
    #msb = 0
    lsbmin = 70 # min 75 for led
    lsbmax = 255
    while True:
        for lsb in range(lsbmin,lsbmax-1,1):
            spi.write_pot(lsb)
            print("Wiper Position = ",spi.WiperGetPosition())
            time.sleep(0.05)

        for lsb in range(lsbmax,lsbmin+1,-1):
            spi.write_pot(lsb)
            print("Wiper Position = ",spi.WiperGetPosition())
            time.sleep(0.05)

if __name__ == "__main__":
    spi = MCP41HVX1(0,0) # spi.open(0,0)
    main()
    


