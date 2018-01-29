#!/bin/bash
# My first script

/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino9/bin/avrdude -C/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino9/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyUSB0 -b57600 -D -Uflash:w:/home/david/Files/GitHub_noSync/Arduino-UART-API/Linux-UPLOAD-FW-scripts/OnLineCom_v06.hex:i