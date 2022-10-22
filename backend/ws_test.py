import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://0.0.0.0:6379") as websocket:
        await websocket.send("Hello world!")
        # await websocket.recv()

asyncio.run(hello())