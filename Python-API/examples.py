#!/usr/bin/env python
from Arduino import Arduino
from Arduino import m328
import time
#from Arduino import atmega328p_reg
#DDRB = 0x24

def Test():
    """
    Blinks an LED in 1 sec intervals
    """
    board = Arduino()
    #board.sendSerialCmd(0x35,m328.DDRB) #DDRB 5 = 1 = OUTPUT
    board.pinMode(13, 'OUTPUT')
    #board.sendSerialCmd(0x35,m328.PORTB)
    board.digitalWrite(13,'HIGH')
    print(board.digitalRead(13))
    time.sleep(2)
    #board.sendSerialCmd(0x45,m328.PORTB)
    board.digitalWrite(13,'LOW')
    

if __name__ == "__main__":
    #Blink(13, '115200','/dev/ttyUSB0')
    Test()
