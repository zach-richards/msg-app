#!/usr/bin/env python

"""Client using the asyncio API."""

import asyncio
from websockets.asyncio.client import connect

message = ""

async def text(message):
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print(message)