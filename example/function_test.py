from mcp41hvx1 import MCP41HVX1
import time

# To activate spi function in Jetson Nano
    # Method 1 - using subprocess to activate
    #import subprocess
    #subprocess.run(['sudo', 'modprobe', 'spidev'])

    # Method 2 - activate in terminal
    # sudo modprobe spidev

def main():
    #msb = 0
    lsbmin = 70 # min 75 for led
    lsbmax = 255
    while True:
        for lsb in range(lsbmin,lsbmax-1,1):
            spi.write_pot(lsb)
            print("Wiper Position = ",spi.WiperGetPosition())
            time.sleep(0.1)

        for lsb in range(lsbmax,lsbmin+1,-1):
            spi.write_pot(lsb)
            print("Wiper Position = ",spi.WiperGetPosition())
            time.sleep(0.1)

if __name__ == "__main__":
    spi = MCP41HVX1(0,0)
    main()
