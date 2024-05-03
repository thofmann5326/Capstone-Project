from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from barky.models import Bookmark


class BookmarkViewSetTestCase(APITestCase):
    def test_create_bookmark(self):
        url = reverse('bookmark-list')
        data = {'id': '0', 'title': 'Test Bookmark',
                'url': 'http://example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bookmark.objects.count(), 1)
        self.assertEqual(Bookmark.objects.get().title, 'Test Bookmark')
