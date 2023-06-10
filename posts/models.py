from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    # este metodo en particular tiene que llamarse __str__ obligatoriamente para que funcione
    def __str__(self):
        return self.text[:50]