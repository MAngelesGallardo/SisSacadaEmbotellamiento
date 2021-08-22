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

# - World
from world import *

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = Client(MOTOR_SERVER_IP, port=MOTOR_SERVER_PORT)
client2 = Client(NOZZLE_SERVER_IP, port=NOZZLE_SERVER_PORT)
try:
    client.connect()
    client2.connect()
    while True:
        rq = client2.write(NOZZLE_RW_ADDR, 1) 
        rq = client2.write(NOZZLE_TAG_RUN, 1)
        rq = client.write(MOTOR_RW_ADDR + MOTOR_TAG_RUN, 2)
except KeyboardInterrupt:
    client.close()
    client2.close()
except ConnectionException:
    print "Unable to connect / Connection lost"


