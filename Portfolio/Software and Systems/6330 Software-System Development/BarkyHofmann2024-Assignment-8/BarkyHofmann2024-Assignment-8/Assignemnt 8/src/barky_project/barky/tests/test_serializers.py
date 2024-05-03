from barky.serializers import BookmarkSerializer
from barky.models import Bookmark
from django.test import TestCase


class BookmarkSerializerTestCase(TestCase):
    def test_valid_data(self):
        serializer = BookmarkSerializer(
            data={'id': '0', 'title': 'Test Bookmark', 'url': 'http://example.com'})
        # Check if serializer is valid
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_invalid_data(self):
        serializer = BookmarkSerializer(
            data={'id': '', 'title': '', 'url': 'invalid-url'})
        # Check if serializer is invalid
        self.assertFalse(serializer.is_valid())
