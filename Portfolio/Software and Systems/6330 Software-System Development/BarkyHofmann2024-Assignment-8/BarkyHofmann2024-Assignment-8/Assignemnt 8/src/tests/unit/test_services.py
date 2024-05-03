from django.apps import AppConfig
from django.conf import settings
from django.apps import apps
import django
import os
import sys
from pathlib import Path
import unittest

from barky_Original.domain.model import Bookmark

loc = Path(__file__).parent.parent.parent / "barky_project"

sys.path.append(os.path.join(os.path.dirname(__file__), f"{loc}"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barky_project.settings")


class TestCaseRepository(unittest.TestCase):
    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:

        django.setup()

    def test_repository_list(self):
        if apps.ready:
            print("Apps are ready")
            bm = apps.get_model("barky", "Bookmark")

            bm.objects.all().delete()

            bm.objects.create(
                id=1,
                title="Test Title",
                url="http://test.com",
                notes="Test notes",
                date_added="2021-01-01",
            )
            bm.objects.create(
                id=2,
                title="Test Title 2",
                url="http://test2 .com",
                notes="Test notes 2",
                date_added="2021-01-02",
            )

            self.assertEqual(bm.objects.all().count(), 2)

            self.assertEqual(bm.objects.first().id, 1)

            bm.objects.all().delete()

    def test_repository_create(self):
        pass

    def test_repository_update(self):
        pass

    def test_repository_delete(self):
        pass

    def test_repository_get(self):
        pass
