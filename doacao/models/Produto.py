from django.db import models

class Produto(models.Model):
   id = models.BigIntegerField(primary_key = True)
   nome = models.CharField(max_length = 100)
   quantidade = models.IntegerField(max_length=500)

   def __str__(self):
        return self.description

 