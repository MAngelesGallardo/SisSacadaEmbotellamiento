#!/usr/bin/env python

#########################################
# Imports
#########################################
# - Logging
import modbus
import logging

# - Comunicacion de ataques
from modbus	import ClientModbus as Client
from modbus	import ConnectionException 

# - World environement
from world import *

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = Client(NOZZLE_SERVER_IP, port=NOZZLE_SERVER_PORT)
try:
    client.connect()
    while True:
        rq = client.write(LEVEL_RO_ADDR, 1) 
        rq = client.write(LEVEL_TAG_SENSOR, 1) 
except KeyboardInterrupt:
    client.close()
except ConnectionException:
    print "Unable to connect / Connection lost"

