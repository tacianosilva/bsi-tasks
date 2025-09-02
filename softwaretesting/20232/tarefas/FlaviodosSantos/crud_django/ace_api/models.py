from django.db import models


# Create your models here.
class Ace(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=6)
    zona = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome 