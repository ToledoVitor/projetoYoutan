from decimal import Decimal as D

from django.db import models
from django.db.models.fields import DecimalField

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.commons import Estados


class EntidadeFinanceira(models.Model):
    name = models.CharField(default="", blank=True, max_length=256)
    cnpj = models.CharField(default="", blank=True, max_length=14)

    logradouro = models.CharField(default="", blank=True, max_length=256)
    bairro = models.CharField(default="", blank=True, max_length=256)
    numero = models.CharField(default="", blank=True, max_length=256)
    cep = models.CharField(default="", blank=True, max_length=256)

    cidade = models.CharField(default="", blank=True, max_length=256)
    estado = models.CharField(max_length=2, choices=Estados.Choices)


class Leilao(models.model):
    # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/#generic-relations
    item_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    item_object = GenericForeignKey("content_type", "object_id")
    # That's the field that holds the other model instance (Imovel or Veiculo) 
    item_id = models.PositiveIntegerField()
    
    minimum_increment = DecimalField(max_digits=12, decimal_places=2, default=D(0))

    entidade_financeira = models.ForeignKey(EntidadeFinanceira, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_latest_lance(self):
        return self.lance_set.order_by("-created_at").first()


class Lance(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE)

    money_value = DecimalField(max_digits=12, decimal_places=2, default=D(0))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Imovel(models.model):
    class TipoImovel(models.TextChoices):
      RESIDENCIAL = "residencial"
      COMERCIAL = "comercial"
      RURAL = "rural"

    leilao = GenericRelation(Leilao)
    tipo_imovel = models.CharField(max_length=256, choices=TipoImovel.Choices)

    logradouro = models.CharField(default="", blank=True, max_length=256)
    bairro = models.CharField(default="", blank=True, max_length=256)
    numero = models.CharField(default="", blank=True, max_length=256)
    cep = models.CharField(default="", blank=True, max_length=256)

    cidade = models.CharField(default="", blank=True, max_length=256)
    estado = models.CharField(max_length=2, choices=Estados.Choices)

    # Custom field that represent's if the current immobile is avaliable to receive offers
    avaliable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Veiculo(models.Model):
    class TipoVeiculo(models.TextChoices):
        MOTO = "moto"
        CARRO = "carro"
        VAN = "van"

    leilao = GenericRelation(Leilao)
    tipo_veiculo = models.CharField(max_length=5, choices=TipoVeiculo.choices)

    placa = models.CharField(default="", max_length=7, blank=True)

    # Custom field that represent's if the current vehicle is avaliable to receive offers
    avaliable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
