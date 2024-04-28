import sys
from abc import ABC, abstractmethod
from datetime import datetime
import pytz

import requests
from django.db import transaction

from barky.models import Bookmark
from barkyarch.domain.model import DomainBookmark


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(
            "A command must implement the execute method")


class AddBookmarkCommand(Command):
    def execute(self, data: DomainBookmark, timestamp=None):
        bookmark = Bookmark(data.id, data.title, data.url,
                            data.notes, timestamp)
        bookmark.timestamp = datetime.now(pytz.UTC).isoformat()

        # again, we skip the ouw with django's transaction management
        with transaction.atomic():
            bookmark.save()


class ListBookmarksCommand(Command):

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return Bookmark.objects.all().order_by(self.order_by)


class DeleteBookmarkCommand(Command):

    def execute(self, data: DomainBookmark):
        bookmark = Bookmark.objects.get(url=data.url)
        with transaction.atomic():
            bookmark.delete()


class EditBookmarkCommand(Command):
    def execute(self, data: DomainBookmark):
        bookmark = Bookmark.update_from_domain(data)
        with transaction.atomic():
            bookmark.save()
