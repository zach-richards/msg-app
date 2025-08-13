
# Run the server first and then the client to test

import asyncio
import websockets

PORT = 8765

async def echo(websocket, path=None): # handle messages
    async for message in websocket:
        await websocket.send(message)

async def main(): # Connect to the server and wait until shutdown
    server = await websockets.serve(echo, "localhost", PORT)
    print(f"Server listening on Port {PORT}")
    await server.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        import traceback
        traceback.print_exc()