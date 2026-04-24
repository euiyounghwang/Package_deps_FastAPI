import requests
import sseclient
import asyncio
from aiohttp_sse_client import client as sse_client

url = "http://localhost:8000/stream"
# response = requests.get(url, stream=True)
# client = sseclient.SSEClient(response)

# for event in client.events():
#     print(f"Received: {event.data}")

async def main():
    async with sse_client.EventSource(url) as event_source:
        async for event in event_source:
            print(event.data)

asyncio.run(main())