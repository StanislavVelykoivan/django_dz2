from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet,create_note

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notes/', create_note),
]