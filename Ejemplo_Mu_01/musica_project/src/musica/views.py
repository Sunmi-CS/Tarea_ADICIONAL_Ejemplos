from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Artist, Song
from .forms import ArtistForm, SongForm

# ---------- SONGS ----------
def song_list(request):
    q = request.GET.get('q', '').strip()
    songs = Song.objects.select_related('artist').order_by('-created_at')
    if q:
        songs = songs.filter(Q(title__icontains=q) | Q(genre__icontains=q) | Q(artist__name__icontains=q))
    context = {'songs': songs, 'q': q}
    return render(request, 'musica/song_list.html', context)

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'musica/song_form.html', {'form': form, 'title': 'Crear Canción'})

def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'musica/song_form.html', {'form': form, 'title': 'Editar Canción'})

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'musica/song_confirm_delete.html', {'song': song})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'musica/song_detail.html', {'song': song})

# ---------- ARTISTS ----------
def artist_list(request):
    artists = Artist.objects.all().order_by('name')
    return render(request, 'musica/artist_list.html', {'artists': artists})

def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'musica/artist_form.html', {'form': form, 'title': 'Crear Artista'})

def artist_update(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'musica/artist_form.html', {'form': form, 'title': 'Editar Artista'})

def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        artist.delete()
        return redirect('artist_list')
    return render(request, 'musica/artist_confirm_delete.html', {'artist': artist})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    songs = artist.songs.all()
    return render(request, 'musica/artist_detail.html', {'artist': artist, 'songs': songs})
