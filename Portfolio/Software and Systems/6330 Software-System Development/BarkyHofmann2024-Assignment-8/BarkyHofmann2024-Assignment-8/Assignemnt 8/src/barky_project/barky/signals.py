import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SimpleBookmarkConsumer
from .models import Bookmark

channel_layer = get_channel_layer()


def log_bookmark_to_csv(sender, instance, **kwargs):
    print("I am a signal! I was called because a Bookmark was saved!")

    file = Path(__file__).parent.parent / "barkyarch" / \
        "domain" / "created_log.csv"
    print(f"Writing to {file}")

    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        logwriter.writerow(
            [
                instance.id,
                instance.title,
                instance.url,
                instance.notes,
                instance.date_added,
            ]
        )


def send_bookmark_to_channel(sender, instance, **kwargs):
    print("Bookmark signal: Channel")
    print(f"Sending bookmark to channel: {instance}")

    async_to_sync(channel_layer.send)(
        "bookmarks-add", {"type": "print.bookmark", "data": instance.url}
    )


post_save.connect(log_bookmark_to_csv, sender=Bookmark)
post_save.connect(send_bookmark_to_channel, sender=Bookmark)
