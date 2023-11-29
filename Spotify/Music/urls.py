from django.urls import path
from .views import SongListCreateView, SongDetailView, ArtistListCreateView, ArtistDetailView


urlpatterns = [
    path('', SongListCreateView.as_view(), name='song-list-create'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail')]