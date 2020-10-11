from django.db import models


class Company(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14)
    uf = models.CharField('UF', max_length=2)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __repr__(self):
        return self.name

