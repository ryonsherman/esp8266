# ESP8266

Exploration of the [Espruino ESP8266](http://www.espruino.com/ESP8266) SoC

#### Pinout

![ESP8266 Pinout](http://www.espruino.com/refimages/ESP8266_pinout.png)

##### Wiring

* `GND` to `LOW`
* `VCC` to `HIGH` (3.3v)
* `CH_PD` to `HIGH` for normal operation
* `UTXD` to `RXD` on UART device
* `URXD` to `TXD` on UART device

#### Serial

[AT Commands](http://www.electrodragon.com/w/Wi07c#AT_Commands)

## NodeMcu
[NodeMcu](http://nodemcu.com/index_en.html) is an [open-source](https://github.com/nodemcu/nodemcu-firmware) firmware that provides a [Lua](http://www.lua.org) interface to the ESP8266.
#### Flashing
Ensure `GPIO0` is `LOW` and `CH_PD` is `HIGH` for flashing. Remove `GPIO0` and RESET for normal operation.
```
wget https://raw.githubusercontent.com/themadinventor/esptool/master/esptool.py
wget https://github.com/nodemcu/nodemcu-firmware/raw/master/pre_build/latest/nodemcu_512k_latest.bin

chmod +x esptool.py
./esptool.py --port /dev/ttyUSB0 write_flash 0x00000 nodemcu_512k_latest.bin
```

## Examples
`esp8266.py` is a script to aid in the upload and execution of lua scripts.

```
usage: esp8266.py [-h] [--verbose] [-d DEVICE] [-b BAUDRATE] [-t TIMEOUT]
                  [--restart]
                  {exec,upload,delete} ...

positional arguments:
  {exec,upload,delete}  action to perform
    exec                upload and execute file
    upload              upload file to destination
    delete              delete file from device

optional arguments:
  -h, --help            show this help message and exit
  --verbose             use verbose output

serial:
  -d DEVICE, --device DEVICE
                        device path (default /dev/ttyUSB0)
  -b BAUDRATE, --baud BAUDRATE
                        device baud rate (default: 9600)
  -t TIMEOUT, --timeout TIMEOUT
                        read timeout value (default: 0.1)

device:
  --restart, --reset    restart device before taking action
```
#### Web Server
```
./esp8266.py --restart exec examples/webserver/init.lua
./esp8266.py upload examples/webserver/index.html
```
