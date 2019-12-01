from django.db import models


class Product(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()
    objects = models.Manager()
def __str__(self):
    return self.descricao

