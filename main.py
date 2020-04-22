from importlib import util
import asyncio
from nio import (AsyncClient, SyncResponse, RoomMessageText)

async_client = AsyncClient(
    "https://matrix.org", "%%YOUR-USERNAME-HERE%%"
)

response = await async_client.login("%%YOUR-PASSWORD-HERE%%")
print(response)

async def main():
    response = await async_client.login("%%YOUR-PASSWORD-HERE%%")
    print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

