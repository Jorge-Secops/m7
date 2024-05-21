from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Coments(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    coments = models.CharField(max_length=200)

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Comuna(models.Model):
    name = models.CharField(max_length=100)  
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.name

class Inmueble(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
