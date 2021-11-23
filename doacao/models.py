from django.db import models

class Usuario(models.Model):
   nome = models.CharField(max_length = 100, verbose_name="Nome")
   email = models.CharField(max_length= 100, verbose_name="e-mail")

   def __str__(self):
      return "{} ({})".format(self.nome, self.email) 

class Instituicao(models.Model):
   nome = models.CharField(max_length = 100, verbose_name="Nome da Instituição")
   email = models.CharField(max_length= 100, verbose_name="e-mail")
   endereco = models.CharField(max_length= 255,verbose_name="Endereço")

   def __str__(self):
      return "{} ({}) ({}) ".format(self.nome, self.email, self.endereco) 

class Produto(models.Model):
   nome = models.CharField(max_length = 100, verbose_name="Nome do Produto")
   quantidade = models.IntegerField(verbose_name="Quantidade")
   instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)

   def __str__(self):
      return "{} ({}) ({})".format(self.nome, self.quantidade, self.instituicao)



