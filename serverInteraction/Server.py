import asyncio
import websockets

PORT = 8765

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

async def main():
    server = await websockets.serve(echo, "localhost", PORT)
    print(f"Server listening on Port {PORT}")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())