from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    # este metodo en particular tiene que llamarse __str__ obligatoriamente para que funcione
    def __str__(self):
        return self.text[:50]
    
class Imagen(models.Model):
    img = models.ImageField()

    def __image__(self):
        return self.img()