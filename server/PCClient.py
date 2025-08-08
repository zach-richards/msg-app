
# Run the server first and then the client to test

import asyncio
import websockets

PORT = 8765
URI = f"ws://localhost:{PORT}"

async def hello():
    async with websockets.connect(URI) as websocket:
        # Send a message to the server
        message = "Hello from client!"
        await websocket.send(message)
        print(f"> Sent: {message}")

        # Wait for echo from the server
        response = await websocket.recv()
        print(f"< Received: {response}")

if __name__ == "__main__":
    try:
        asyncio.run(hello())
    except KeyboardInterrupt: # Error handling
        print("\nConnection stopped manually.")
    except ConnectionRefusedError:
        print("\nConnection refused. Is the server running?")
    except Exception as e:
        print(f"\nA client-side error occured: {e}")