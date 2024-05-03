from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bookmarks', views.BookmarkViewSet, basename='bookmark')
router.register(r"snippets", views.SnippetViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

urlpatterns += router.urls
