# notes/urls.py
from django.urls import path
from .views import NoteCreateView, NoteDetailView, NoteShareView, NoteUpdateView, NoteVersionHistoryView

urlpatterns = [
    path('notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/share/<int:pk>/', NoteShareView.as_view(), name='note-share'),
    path('notes/update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/version-history/<int:id>/', NoteVersionHistoryView.as_view(), name='note-version-history'),
]
