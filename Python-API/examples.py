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
    board.digitalWrite(13,'HIGH')
    time.sleep(1)
    board.digitalWrite(13,'LOW')

def Read():
    board.pinMode(14,'INPUT:PULLUP')
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
    print(board.CMD_buffer_num)

def DoLoopExample():
    board.pinMode(13, 'OUTPUT')
    board.Cmd_Do()
    board.digitalWrite(13,'HIGH')
    board.digitalWrite(13,'LOW')
    board.Cmd_Loop()
    
    

if __name__ == "__main__":
    #Blink(13, '115200','/dev/ttyUSB0')
    board = Arduino()
    
    #Blink()
    Read()
    PrintCMDNum()
    PrintCMDNum()
    ReadChannel()
    ReadFastADCChannel()
    ReadADCreg()
    PrintCMDNum()
    DoLoopExample()
    
    
