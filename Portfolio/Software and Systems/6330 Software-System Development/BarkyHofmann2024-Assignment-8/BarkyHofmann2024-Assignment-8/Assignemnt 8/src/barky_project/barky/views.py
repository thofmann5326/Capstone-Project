from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Bookmark, Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import BookmarkSerializer, SnippetSerializer, UserSerializer


# Create your views here.
class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all().order_by("-date_added")
    serializer_class = BookmarkSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
