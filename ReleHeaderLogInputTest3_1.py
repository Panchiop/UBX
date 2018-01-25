import Adafruit_BBIO.GPIO as GPIO
import time
import os
import logging
import sys
import uuid
from datetime import datetime
from threading import Thread


a = 0

GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_14", GPIO.OUT)
GPIO.setup("P9_16", GPIO.OUT)
GPIO.setup("P9_18", GPIO.OUT)
GPIO.setup("P9_22", GPIO.OUT)
GPIO.setup("P9_24", GPIO.OUT)

stat =  "P9_11"
stat1 = "P9_13"
stat2 = "P9_15"
stat3 = "P9_17"
stat4 = "P9_21"
stat5 = "P9_23"

m = 0
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
l6 = 0


GPIO.setup(stat,  GPIO.IN)
GPIO.setup(stat1, GPIO.IN)
GPIO.setup(stat2, GPIO.IN)
GPIO.setup(stat3, GPIO.IN)
GPIO.setup(stat4, GPIO.IN)
GPIO.setup(stat5, GPIO.IN)

print str(uuid.uuid1())
uuid.uuid1()

string_uuid = uuid.uuid1()
string_uuid1 = uuid.uuid1()

def status(): #Relay 8_ZR_LIGHT2_PinInput_Status
    
    time.sleep(.1)
    global n1,l1
    GPIO.cleanup()
    if GPIO.input(stat):  
        print "1"
        time.sleep(.2)
        logger.info('ZR_LIGHT2_Node in Network: Success.')
        time.sleep(.2)
        logger.info('ZR_LIGHT2_Connection: Success.')
        n1 += 1      
        logger.info('Number of successful connections to the network of ZR_LIGHT2 = %d' % n1)
    else:
        print "0"
        time.sleep(.2)
        logger.error('ZR_LIGHT2_Node in Network: Fail.')
        l1 += 1      
        logger.info('Number of connections to the network Fail of ZR_LIGHT2 = %d' % l1)
    GPIO.cleanup() 
    time.sleep(.1)
    return;

def status1(): #Relay 7_ZC_LIGHT1_PinInput_Status
    
    time.sleep(.1)
    global n2,l2
    GPIO.cleanup()
    if GPIO.input(stat1):  
        print "1"
        time.sleep(.2)
        logger.info('ZC_LIGHT1_Node in Network: Success.')
        time.sleep(.2)
        logger.info('ZC_LIGHT1_Connection: Success.')
        n2 += 1      
        logger.info('Number of successful connections to the network of ZC_LIGHT1 = %d' % n2)
    else:
        print "0"
        time.sleep(.2)
        logger.error('ZC_LIGHT1_Node in Network: Fail.')
        l2 += 1      
        logger.info('Number of connections to the network Fail of ZC_LIGHT1 = %d' % l2)
    GPIO.cleanup() 
    time.sleep(.1)
    return;

def status2(): #Relay 6_ZED_Temp_PinInput_Status
    
    time.sleep(.1)
    global n3,l3
    GPIO.cleanup()
    if GPIO.input(stat2):  
        print "1"
        time.sleep(.2)
        logger.info('ZED_TEMP_Node in Network: Success.')
        time.sleep(.2)
        logger.info('ZED_TEMP_Connection: Success.')
        n3 += 1      
        logger.info('Number of successful connections to the network of ZED_TEMP = %d' % n3)
    else:
        print "0"
        time.sleep(.2)
        logger.error('ZED_TEMP_Node in Network: Fail.')
        l3 += 1      
        logger.info('Number of connections to the network Fail of ZED_TEMP = %d' % l3)
    GPIO.cleanup() 
    time.sleep(.1)
    return;

def status3(): #Relay 5_ZR_LIGHT3_PinInput_Status
    
    time.sleep(.1)
    global n4,l4
    GPIO.cleanup()
    if GPIO.input(stat3):  
        print "1"
        time.sleep(.2)
        logger.info('ZR_LIGHT3_Node in Network: Success.')
        time.sleep(.2)
        logger.info('ZR_LIGHT3_Connection: Success.')
        n4 += 1      
        logger.info('Number of successful connections to the network of ZR_LIGHT3 = %d' % n4)
    else:
        print "0"
        time.sleep(.2)
        logger.error('ZR_LIGHT3_Node in Network: Fail.')
        l4 += 1      
        logger.info('Number of connections to the network Fail of ZR_LIGHT3 = %d' % l4)
    GPIO.cleanup() 
    time.sleep(.1)
    return;

def status4(): #Relay 4_ZED_SWITCH_PinInput_Status
    
    time.sleep(.1)
    GPIO.cleanup()
    global n5,l5
    if GPIO.input(stat4):  
        print "1"
        time.sleep(.2)
        logger.info('ZED_SWITCH_Node in Network: Success.')
        time.sleep(.2)
        logger.info('ZED_SWITCH_Connection: Success.')
        n5 += 1      
        logger.info('Number of successful connections to the network of ZED_SWITCH = %d' % n5)
    else:
        print "0"
        time.sleep(.2)
        logger.error('ZED_SWITCH_Node in Network: Fail.')        
        l5 += 1      
        logger.info('Number of connections to the network Fail of ZED_SWITCH = %d' % l5)
    GPIO.cleanup() 
    time.sleep(.1)
    return;

def status5(): #Relay 3_ZR_LIGHT4_PinInput_Status
    
    time.sleep(.1)
    global n6,l6
    GPIO.cleanup()
    if GPIO.input(stat5):  
        print "1"
        time.sleep(.2)
        logger.info('ZR_LIGHT4_Node in Network: Success.')
        time.sleep(.2)
        logger.info('ZR_LIGHT4_Connection: Success.')
        n6 += 1      
        logger.info('Number of successful connections to the network of ZR_LIGHT4 = %d' % n6)
    else:
        print "0"
        time.sleep(.2)
        logger.error('ZR_LIGHT4_Node in Network: Fail.')
        l6 += 1      
        logger.info('Number of connections to the network of ZR_LIGHT4 = %d' % l6)
    GPIO.cleanup() 
    time.sleep(.1)
    return;
    
    
# Create a class that extends the FileHandler class from logging.FileHandler
class FileHandlerWithHeader(logging.FileHandler):

    # Pass the file name and header string to the constructor.
    def __init__(self, filename, header,  mode='a', encoding=None, delay=0):
        # Store the header information.
        self.header = header

        # Determine if the file pre-exists
        self.file_pre_exists = os.path.exists(filename)

        # Call the parent __init__
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)

        # Write the header if delay is False and a file stream was created.
        if not delay and self.stream is not None:
            self.stream.write('%s\n' % header)

    def emit(self, record):
        # Create the file stream if not already created.
        if self.stream is None:
            self.stream = self._open()

            # If the file pre_exists, it should already have a header.
            # Else write the header to the file so that it is the first line.
            if not self.file_pre_exists:
                self.stream.write('%s\n' % self.header)

        # Call the parent class emit function.
        logging.FileHandler.emit(self, record)

# Create a logger and set the logging level.
logger = logging.getLogger("test")
logger.setLevel(logging.INFO)

#KPUEncabezadoFormatter---------------------------------------------------------------------------------
encabezado = '-  Test 3  - Test3_1_Secuencial_ZCL1_ZRL2_ZEDTemp_ZRL3_ZEDSwitch1_ZRL4_OnOffWithRelay  -\
\n\n- Rev 2 - Date 6 january 2018 - Python version 3 - \
\nUIID_1 Test 3_1 15/Jan/2018: {!s} \
\n\n-Description: A network of six modules will be created,\
\nwhich will be: 4 lights, 1 switch and 1 temps module. For this, a routine will be created in a \
\nBeagleBoneBlack to activate or deactivate 6 relays in a certain period of time, \
\nin this case it will be 40 second to turn on and 20 seconds to turn off again this will be done one day. \
\nin this case the relays will turn on and they will turn off in a sequence\
\n\nThe module to be examined will be a light1 Coordinator. \
\nZC_Light1: CC2652 -Light Application -Coordinator -IEEE: 00:12:4B:00:13:14:D0:83\
\nZR_Light2: CC2652 -Light Application -Coordinator -IEEE: 00:12:4B:00:13:14:D3:03\
\nZR_Light3: CC2652 -Light Application -Coordinator -IEEE: 00:12:4B:00:13:14:E3:00\
\nZR_Light4: CC2652 -Light Application -Coordinator -IEEE: 00:12:4B:00:13:14:E8:80\
\nZED_Switch1: CC2652 -Light Application -Coordinator -IEEE: 00:12:4B:00:13:14:E7:01\
\nZED_Temperature: CC2652 -Light Application -Coordinator -IEEE: 00:12:4B:00:13:14:E9:03\
\n\nError list:\
\n\n- Status: Connection Success!!! \
\n- Node in Network: Fail. \
\n\n-Log list-\
\n'.format(string_uuid1)  

fh = FileHandlerWithHeader('Test3_1_Secuencial_ZCL1_ZRL2_ZEDTemp_ZRL3_ZEDSwitch1_ZRL4_OnOffWithRelay.log', encabezado,  delay=True)
#KPUEncabezadoFormatter----------------------------------------------------------------------------------

fh.setLevel(logging.INFO)

# Add formatter to the file handler.
formatter = logging.Formatter("- %(asctime)s - %(created)s - %(name)s - %(levelname)s - %(message)s")

fh.setFormatter(formatter)

# Add the handler to the logger.
logger.addHandler(fh)

# Since the constructor of the FileHandlerWithHeader was passed delay=True
# the file should not exist until the first log as long as the log file did
# not pre-exist.


def print_menu():       ##Menu
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Relay with 40 second ON and 20 seconds OFF"
    print "2. N/A"
    print "3. N/A"
    print "4. N/A"
    print "5. Exit"
    print 67 * "-"
    


print "Ready to start the test."
logger.info('------------------------------')
logger.info('------------------------------')
print str(uuid.uuid3(uuid.NAMESPACE_DNS, 'test3_1') ) #UUID with test1 name inside.

logger.info(format(string_uuid1)) # logger for every time that the code run



print "Inicializacion de red" 
logger.info('Network Initialization')
time.sleep(5) 
print "listo"
logger.info('Network On')
logger.info('---------')

print_menu()    ## Displays menu
choice = input("Enter your choice [1-5]: ")
     

loop=True 
while loop:

    if choice==1: 
        
        #Set the GPIO in HI state
        GPIO.output("P9_12", GPIO.HIGH) 
        GPIO.output("P9_14", GPIO.HIGH) 
        GPIO.output("P9_16", GPIO.HIGH) 
        GPIO.output("P9_18", GPIO.HIGH) 
        GPIO.output("P9_22", GPIO.HIGH) 
        GPIO.output("P9_24", GPIO.HIGH) 

        time.sleep(10)
        #Relay_8_ZR_LIGHT2
        GPIO.output("P9_12", GPIO.HIGH) 
        print "ZR_LIGHT2_ON"
        logger.info('---------')
        logger.info('ZR_LIGHT2_ON')
        m1 += 1
        logger.info('Switched ON ZR_LIGHT2 = %d' % m1)
        time.sleep(2)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(3)



        GPIO.output("P9_12", GPIO.LOW)
        print "ZR_LIGHT2_OFF"
        logger.info('ZR_LIGHT2_OFF')
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        logger.info('---------')
        time.sleep(1)

    
        #Relay_7_ZC_LIGHT1
        GPIO.output("P9_14", GPIO.HIGH) 
        print "ZC_LIGHT1_ON"
        logger.info('---------')
        logger.info('ZC_LIGHT1_ON')
        m2 += 1
        logger.info('Switched ON ZC_LIGHT1 = %d' % m2)
        time.sleep(2)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(3)
        
        
        GPIO.output("P9_14", GPIO.LOW)
        print "ZC_LIGHT1_OFF"
        logger.info('ZC_LIGHT1_OFF')
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        logger.info('---------')
        time.sleep(1)

    
    
        #Relay_6_ZED_Temp
        GPIO.output("P9_16", GPIO.HIGH) 
        print "ZED_TEMP_ON"
        logger.info('---------')
        logger.info('ZED_TEMP_ON')
        m3 += 1
        logger.info('Switched ON ZED_TEMP = %d' % m3)
        time.sleep(2)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(3)
        
   
        GPIO.output("P9_16", GPIO.LOW)
        print "ZED_Temp_OFF"
        logger.info('ZED_TEMP_OFF')
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        logger.info('---------')
        time.sleep(1)

    
        #Relay_5_ZR_LIGHT3
        GPIO.output("P9_18", GPIO.HIGH) 
        print "ZR_LIGHT3_ON"
        logger.info('---------')
        logger.info('ZR_LIGHT3_ON')
        m4 += 1
        logger.info('Switched ON ZR_LIGHT3 = %d' % m4)
        time.sleep(2)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(3)
        
   
        GPIO.output("P9_18", GPIO.LOW)
        print "ZR_LIGHT3_OFF"
        logger.info('ZR_LIGHT31_OFF')
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        logger.info('---------')
        time.sleep(1)

    
    
        #Relay_4_ZED_SWITCH
        GPIO.output("P9_22", GPIO.HIGH) 
        print "ZED_SWITCH_ON"
        logger.info('---------')
        logger.info('ZED_SWITCH_ON')
        m5 += 1
        logger.info('Switched ON ZED_SWITCH = %d' % m5)
        time.sleep(2)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(3)
        
   
        GPIO.output("P9_22", GPIO.LOW)
        print "ZED_SWITCH_OFF"
        logger.info('ZED_SWITCH_OFF')
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        logger.info('---------')
        time.sleep(1)

    
        #Relay_3_ZR_LIGHT4
        GPIO.output("P9_24", GPIO.HIGH) 
        print "ZR_LIGHT4_ON"
        logger.info('---------')
        logger.info('ZR_LIGHT4_ON')
        m6 += 1
        logger.info('Switched ON ZR_LIGHT4 = %d' % m6)
        time.sleep(2)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(3)
        
   
        GPIO.output("P9_24", GPIO.LOW)
        print "ZR_LIGHT4_OFF"
        logger.info('ZR_LIGHT4_OFF')
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        status()
        time.sleep(1)
        status1()
        time.sleep(1)
        status2()
        time.sleep(1)
        status3()
        time.sleep(1)
        status4()
        time.sleep(1)
        status5()
        time.sleep(1)
        logger.info('---------')
        time.sleep(1)
        
        m += 1 # Iteration counter
        print ("Iteracion",m)
        logger.info('Iteration = %d' % m)
        time.sleep(2)
        logger.info('Number of connections to the network of ZR_LIGHT4 = %d' % l6)
        
        GPIO.cleanup() 
    
    elif choice==2:
        print "N/A"
        ## You can add your code or functions here
        loop=False
    elif choice==3:
        print "N/A"
        ## You can add your code or functions here
        loop=False
    elif choice==4:
        print "N/A"
        ## You can add your code or functions here
        loop=False
    elif choice==5:
        print "N/A"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
   
