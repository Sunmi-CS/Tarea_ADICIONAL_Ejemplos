from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    GENRE_CHOICES = [
        ('pop','Pop'),
        ('rock','Rock'),
        ('hiphop','Hip-Hop'),
        ('jazz','Jazz'),
        ('classical','Classical'),
        ('other','Other'),
    ]
    title = models.CharField(max_length=200)
    duration_seconds = models.PositiveIntegerField()  # duración en segundos
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default='other')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    created_at = models.DateTimeField(auto_now_add=True)

    def duration_display(self):
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
