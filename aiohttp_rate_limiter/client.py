import asyncio
import time

import aiohttp


class RateLimitedClient:

    def __init__(self, client:aiohttp.ClientSession, max_requests_per_second: int) -> None:
        self.max_requests_per_second = max_requests_per_second
        self._client = client
        self._last_request = time.monotonic()

    def _is_waiting(self):
        return time.monotonic() - self._last_request < 1 / self.max_requests_per_second

    async def _wait(self):
        while self._is_waiting():
            await asyncio.sleep(0.1)

    async def get(self, *args, **kwargs):
        await self._wait()
        self._last_request = time.monotonic()
        return self._client.get(*args,**kwargs)

    async def post(self, *args, **kwargs):
        await self._wait()
        self._last_request = time.monotonic()
        return self._client.post(*args,**kwargs)

    async def patch(self, *args, **kwargs):
        await self._wait()
        self._last_request = time.monotonic()
        return self._client.patch(*args,**kwargs)

    async def put(self, *args, **kwargs):
        await self._wait()
        self._last_request = time.monotonic()
        return self._client.put(*args,**kwargs)

    async def delete(self, *args, **kwargs):
        await self._wait()
        self._last_request = time.monotonic()
        return self._client.delete(*args,**kwargs)
 