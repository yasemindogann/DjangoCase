from django.db import models


class Contact(models.Model):
    baslik = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    link = models.URLField(max_length=300)
    aciklama = models.TextField()
    img = models.ImageField()
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.email


