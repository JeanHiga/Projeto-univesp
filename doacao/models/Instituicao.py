from django.db import models

class Instituicao(models.Model):
   id = models.BigIntegerField(primary_key = True)
   nome = models.CharField(max_length = 100)
   email = models.CharField(max_length= 255)
   endereco = models.CharField(max_length= 255)
   
   def __str__(self):
        return self.description