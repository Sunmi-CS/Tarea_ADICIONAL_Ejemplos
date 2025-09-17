from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('songs/create/', views.song_create, name='song_create'),
    path('songs/<int:pk>/edit/', views.song_update, name='song_update'),
    path('songs/<int:pk>/delete/', views.song_delete, name='song_delete'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),

    path('artists/', views.artist_list, name='artist_list'),
    path('artists/create/', views.artist_create, name='artist_create'),
    path('artists/<int:pk>/edit/', views.artist_update, name='artist_update'),
    path('artists/<int:pk>/delete/', views.artist_delete, name='artist_delete'),
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
]
