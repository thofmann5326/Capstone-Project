from django.test import TestCase
from barky.models import Bookmark


class BookmarkModelTestCase(TestCase):
    def test_create_bookmark(self):
        bookmark = Bookmark.objects.create(
            id='0', title='Test Bookmark', url='http://example.com')
        self.assertEqual(Bookmark.objects.count(), 1)
        self.assertEqual(bookmark.title, 'Test Bookmark')
