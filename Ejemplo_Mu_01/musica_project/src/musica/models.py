from django.db import models

class Artista(models.Model):
    nombre=models.CharField(max_length=120)
    nacionalidad=models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nombre
    

class Musica(models.Model):
    GENEROS_MUSICA = [
        ('pop','Pop'),
        ('rock','Rock'),
        ('hiphop','Hip-Hop'),
        ('otro','Otro'),
    ]
    titulo = models.CharField(max_length=200)
    duracion = models.PositiveIntegerField() 
    genero = models.CharField(max_length=30, choices=GENEROS_MUSICA, default='otro')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='musica')


    def duracion(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{minutos}:{segundos:02d}"
    
    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"
