# ESP8266

Expiriments with the [Espruino ESP8266](http://www.espruino.com/ESP8266) SoC

#### Pinout

![ESP8266 Pinout](http://www.espruino.com/refimages/ESP8266_pinout.png)

## NodeMcu
```
wget -O nodemcu_512k_latest.bin https://github.com/nodemcu/nodemcu-firmware/blob/master/pre_build/latest/nodemcu_512k_latest.bin?raw=true
./esptool.py --port /dev/ttyUSB0 write_flash 0x00000 ~/Downloads/nodemcu_512k_latest.bin
```

## Examples
#### Web Server
```
./esp8266.py --restart exec esp8266_webserver.lua
./esp8266.py upload esp8266_webserver.html index.html
```
