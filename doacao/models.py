from django.db import models

class Usuario(models.Model):
   nome = models.CharField(max_length = 100, verbose_name="Nome")
   email = models.CharField(max_length= 100, verbose_name="e-mail")

   def __str__(self):
      return "{} ({})".format(self.nome, self.email) 


class Produto(models.Model):
   nome = models.CharField(max_length = 100, verbose_name="Nome")
   quantidade = models.IntegerField(verbose_name="Quantidade")

   def __str__(self):
      return "{} ({})".format(self.nome, self.quantidade)

class Instituicao(models.Model):
   nome = models.CharField(max_length = 100, verbose_name="Nome")
   email = models.CharField(max_length= 100, verbose_name="e-mail")
   endereco = models.CharField(max_length= 255,verbose_name="Endereço")

   produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

   def __str__(self):
      return "{} ({}) ({}) ({})".format(self.nome, self.email, self.endereco, self.produto) 

