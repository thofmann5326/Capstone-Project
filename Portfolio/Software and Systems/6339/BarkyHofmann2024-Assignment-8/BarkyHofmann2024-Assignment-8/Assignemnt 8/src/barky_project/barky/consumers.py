import asyncio
import datetime
import json
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.generic.http import AsyncHttpConsumer
from barky.models import Bookmark


class SimpleBookmarkConsumer(AsyncConsumer):
    async def print_bookmark(self, message):
        print(f"WORKER: Bookmark: {message['data']}")


class BookmarkConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        bookmarks = Bookmark.objects.all()
        data = json.dumps(
            [{"title": bookmark.title, "url": bookmark.url}
                for bookmark in bookmarks]
        )
        await self.send_response(
            200, data, headers=[(b"Content-Type", b"application/json")]
        )

    async def handle(self, body):
        await self.send_headers(
            headers=[
                (b"Cache-Control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
            ]
        )
        while True:
            payload = "data: %s\n\n" % datetime.now().isoformat()
            await self.send_body(payload.encode("utf-8"), more_body=True)
            await asyncio.sleep(1)

    async def send_bookmark(self, bookmark):
        data = json.dumps({"title": bookmark.title, "url": bookmark.url})
        await self.channel_layer.send(
            "bookmarks-add", {"type": "send.bookmark", "data": data}
        )
