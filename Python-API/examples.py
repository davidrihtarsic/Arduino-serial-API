#!/usr/bin/env python
from Arduino import Arduino
from Arduino import m328
import time
#from Arduino import atmega328p_reg
#DDRB = 0x24

def Blink():
    """
    Blinks an LED in 1 sec intervals
    """
    board.pinMode(13, 'OUTPUT')
    #board.digitalWrite(13,'HIGH')
    board.digitalWrite(13,1)
    time.sleep(1)
    #board.digitalWrite(13,'LOW')
    board.digitalWrite(13,0)

def Read():
    board.pinMode(14,'INPUT_PULLUP')
    print(board.digitalRead(14)) # pin A0
    
def FastRead():
    t1=time.time()
    for x in range(1, 100):
        #print (board.digitalRead(14)) # pin A0
        board.digitalRead(14)
    t2=time.time()
    print(str(x/(t2-t1)) + ' Hz')
    
def ReadChannel():
    print(board.analogRead(0))
    
def ReadFastADCChannel():
    t1=time.time()
    for x in range(1, 100):
        #print (board.digitalRead(14)) # pin A0
        board.analogRead(0)
    t2=time.time()
    print(str(x/(t2-t1)) + ' Hz')

def ReadADCreg():
    t1=time.time()
    for x in range(1, 100):
        #print (board.digitalRead(14)) # pin A0
        board.analogRead(0)
    t2=time.time()
    print(str(x/(t2-t1)) + ' Hz')

def PrintCMDNum():
    print(board.cmd_buffer_num)

def DoLoopExample():
    board.pinMode(13, 'OUTPUT')
    board.cmdDo()
    board.digitalWrite(13,'HIGH')
    board.digitalWrite(13,'LOW')
    board.cmdLoop()
    
def registerWrite():
    board.registerWrite(m328.PORTB,32)

def registerRead():
    print(board.registerRead(m328.PORTB))

def waitBitSet():
    board.digitalWrite(13, 'HIGH')
    #board.waitUntilBitIsSet(0, m328.PINC)
    board.waitUntilBitIsSet(14)
    board.digitalWrite(13, 'LOW')
def waitBitCleared():
    board.digitalWrite(13, 'HIGH')
    #board.waitUntilBitIsSet(0, m328.PINC)
    board.waitUntilBitIsCleared(14)
    board.digitalWrite(13, 'LOW')

if __name__ == "__main__":
    #Blink(13, '115200','/dev/ttyUSB0')
    board = Arduino()
    
    Blink()
    Read()
    #PrintCMDNum()
    #PrintCMDNum()
    #ReadChannel()
    #print(board.readADC())
    #ReadFastADCChannel()
    #ReadADCreg()
    #PrintCMDNum()
    #DoLoopExample()
    #time.sleep(3)
    #board.softwareReset()
    #wait to reset
    #time.sleep(3)
    #Read()
    #registerWrite()
    #registerRead()
    #waitBitSet()
    #waitBitCleared()
    board.TimerOne.initialize()
    
    
    
