import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        print(f"Received from Android: {message}")
        await websocket.send("Got your SMS data")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Server running on ws://0.0.0.0:8765")
        await asyncio.Future()

asyncio.run(main())