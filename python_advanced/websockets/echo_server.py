#!/usr/bin/env python3 
"""Echo Websocket server."""
import asyncio

from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Echo every message back to the sender."""
    async for message in websocket:
        await websocket.send(message)

async def main():
    """Start the server on 127.0.0.1:8765 and run forever."""
    async with serve(connection_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
