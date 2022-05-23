#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets
import json
import logging

logger = logging.getLogger('websockets.server')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

def getResponse():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    response = { "time": now }

    return json.dumps(response)

async def time(websocket, path):    
    while True:
        await websocket.send(getResponse())
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, 'localhost', 5678)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()