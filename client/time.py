#!/usr/bin/env python

import asyncio
import websockets
import logging

logger = logging.getLogger('websockets.client')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


async def handler():
    async with websockets.connect('ws://localhost:5678') as websocket:
        while True:
            message = await websocket.recv()
            print("received: {}".format(message))

asyncio.get_event_loop().run_until_complete(handler())
