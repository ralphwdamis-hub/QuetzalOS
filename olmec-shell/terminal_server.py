import asyncio
import websockets
import subprocess

async def handle(websocket):
    process = await asyncio.create_subprocess_shell(
        'bash',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT
    )

    async def read_output():
        while True:
            data = await process.stdout.read(1024)
            if not data:
                break
            await websocket.send(data.decode('utf-8', errors='replace'))

    asyncio.ensure_future(read_output())

    async for message in websocket:
        process.stdin.write((message + '\n').encode())
        await process.stdin.drain()

async def main():
    print("Olmec Shell Server démarré sur ws://localhost:8765")
    async with websockets.serve(handle, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
