# MCP41HVX1 Digital Potentiometer Driver for Raspberry Pi / Jetson Nano
#MCP41HVX1 #Ditgital variable resistor #Potentiometer #Raspberry Pi #Jetson Nano
# test PI

## Features Highlights:

- Single-Resistor Network
- SPI Serial Interface (10 MHz, Modes 0,0 and 1,1)
- Resistor Network Resolution
  - 7-bit: 127 Resistors (128 Taps >> 0 - 127) - MCP41HV31 series 
  - 8-bit: 255 Resistors (256 Taps >> 0 - 255) - MCP41HV51 series
- R<sub>AB</sub> Resistance Options:

    |R<sub>AB</sub> Value|Package Code|
    |:---:|:---:|
    |5k Ohm| -502|
    |10k Ohm|-103|
    |50k Ohm|-503|
    |100k Ohm|-104|
- High Terminal/Wiper Current (IW) Support:
  - 25 mA (for 5k Ohm)
  - 12.5 mA (for 10k Ohm)
  - 6.5 mA (for 50k Ohm and 100k Ohm)
- Resistor Network Terminal Disconnect Via:
  - Shutdown Pin (SHDN)
  - Terminal Control (TCON) Register
- Write Latch (WLAT) Pin to Control Update of Volatile Wiper Register (such as Zero Crossing)

## Hardware
1. MCP41HVX1 Single Potentiometer - Package Types : TSSOP-14

2. TSSOP14 to DIP14 Pinboard SMD to DIP Adapter (PCB Board)


## Wiring Diagram
<table>
<thead>
  <tr>
    <th colspan="2">Raspberry Pi / Jetson Nano</th>
    <th colspan="2">MCP41HVX1</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Pin</td>
    <td>Description</td>
    <td>Pin</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>+3.3v</td>
    <td>5v is also supported</td>
    <td>1</td>
    <td>Power 1.8v to 5.5v<br></td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;23</td>
    <td>SPI1_SCK</td>
    <td>2</td>
    <td>SCK</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;24</td>
    <td>SPI1_CS0</td>
    <td>3</td>
    <td>CS</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;19</td>
    <td>SPI_MOSI</td>
    <td>4</td>
    <td>SDI</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;21</td>
    <td>SPI_MISO</td>
    <td>5</td>
    <td>SDO</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>(GPIO feature is not yet supported)</td>
    <td>6</td>
    <td>WLAT</td>
  </tr>
  <tr>
    <td>+3.3v</td>
    <td>(GPIO feature is not yet supported)</td>
    <td>7</td>
    <td>SHDN</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>(Not supported yet,<br>Can use TCON command to shutdown)</td>
    <td>8</td>
    <td>NC</td>
  </tr>
  <tr>
    <td>GND</td>
    <td></td>
    <td>9</td>
    <td>DGND</td>
  </tr>
  <tr>
    <td>GND</td>
    <td></td>
    <td>10</td>
    <td>V-    (Connect to external power supply max 36 volts. <br>Common ground with Raspberry Pi)</td>
  </tr>
  <tr>
    <td></td>
    <td>(e.g. GND)</td>
    <td>11</td>
    <td>POB   (This is the potentiometer)</td>
  </tr>
  <tr>
    <td></td>
    <td>(e.g. 330 Ohm resistor and pin + of LED)</td>
    <td>12</td>
    <td>POW   (This is the wiper of the potentiometer)</td>
  </tr>
  <tr>
    <td></td>
    <td>(e.g. +5v)</td>
    <td>13</td>
    <td>POA   (This is the potentiometer)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>14</td>
    <td>V+    (Connect to external power supply max 36 volts)</td>
  </tr>
</tbody>
</table>

## Wiring example
![](reference/wiring_example.jpg)


## Licensing
This software is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.