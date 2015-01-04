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

## NodeMcu
Ensure `GPIO0` is `LOW` and `CH_PD` is `HIGH` for flashing. Remove `GPIO0` and RESET for normal operation.
```
wget https://raw.githubusercontent.com/themadinventor/esptool/master/esptool.py
wget https://github.com/nodemcu/nodemcu-firmware/raw/master/pre_build/latest/nodemcu_512k_latest.bin

chmod +x esptool.py
./esptool.py --port /dev/ttyUSB0 write_flash 0x00000 nodemcu_512k_latest.bin
```

## Examples
#### Web Server
```
./esp8266.py --restart exec esp8266_webserver.lua
./esp8266.py upload esp8266_webserver.html index.html
```
