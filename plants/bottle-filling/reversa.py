#!/usr/bin/env python
import modbus
import logging

# - Comunicacion ataques
from modbus	import ClientModbus as Client
from modbus	import ConnectionException 

# - World
from world import *


logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)
client = Client(MOTOR_SERVER_IP, port=MOTOR_SERVER_PORT)
try:
    client.connect()
    while True:
        rq = client.write(MOTOR_RW_ADDR + MOTOR_TAG_RUN, 2)
except KeyboardInterrupt:
    client.close()
except ConnectionException:
    print "Unable to connect / Connection lost"
