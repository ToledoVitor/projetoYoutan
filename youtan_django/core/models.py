from io import BytesIO
from PIL import Image
from decimal import Decimal as D

from django.core.files import File
from django.db import models
from django.db.models.fields import DecimalField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

from youtan_django.core.commons import Estados


class EntidadeFinanceira(models.Model):
    name = models.CharField(default="", blank=True, max_length=256)
    cnpj = models.CharField(default="", blank=True, max_length=14)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Leilao(models.Model):
    item_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    item_object = GenericForeignKey("item_type", "item_id")
    # That's the field that holds the other model instance (Imovel or Veiculo) 
    item_id = models.PositiveIntegerField()
    
    minimum_increment = DecimalField(max_digits=12, decimal_places=2, default=D(0))
    ended = models.BooleanField(default=False)
    ended_at = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    entidade_financeira = models.ForeignKey(EntidadeFinanceira, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'Leilao {self.id} - FIM: {self.due_date}'

    def get_latest_lance_value(self):
        lance_value = (
            self
            .lance_set 
            .filter(deleted=False)
            .order_by("-created_at")
            .values_list("money_value", flat=True)
        )
        return lance_value[0] if lance_value else 0

    def get_item_type(self):
        return self.item_type.app_labeled_name

    def get_item_object(self):
        if self.item_type.app_labeled_name == 'core | imovel':
            return {
                'name': self.item_object.name,

                'image': self.item_object.get_image(),
                'thumbnail': self.item_object.get_thumbnail(),

                'tipo_imovel': self.item_object.tipo_imovel,
                'logradouro': self.item_object.logradouro,
                'bairro': self.item_object.bairro,
                'numero': self.item_object.numero,
                'cep': self.item_object.cep,
                'cidade': self.item_object.cidade,
                'estado': self.item_object.estado,
                'deleted': self.item_object.deleted,
                'created_at': self.item_object.created_at,
                'updated_at': self.item_object.updated_at,   
            }

        if self.item_type.app_labeled_name == 'core | veiculo':
            return {
                'name': self.item_object.name,

                'image': self.item_object.get_image(),
                'thumbnail': self.item_object.get_thumbnail(),

                'tipo_veiculo': self.item_object.tipo_veiculo,
                'placa': self.item_object.placa,
                'ano': self.item_object.ano,
                'deleted': self.item_object.deleted,
                'created_at': self.item_object.created_at,
                'updated_at': self.item_object.updated_at,   
            }
        
        raise ValidationError("Not a valid item_type")

    def get_entidade_financeira(self):
        return {
            'name': self.entidade_financeira.name,
            'cnpj': self.entidade_financeira.cnpj,
        }

class Lance(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE)
    money_value = DecimalField(max_digits=12, decimal_places=2, default=D(0))

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-money_value',)

    def __str__(self):
        return f'Lance {self.id} - ${self.money_value}'

    def get_leilao(self):
        return {
            'id': self.leilao.id,
            'minimum_increment': self.leilao.minimum_increment,
            'ended': self.leilao.ended,
            'ended_at': self.leilao.ended_at,
            'due_date': self.leilao.due_date,
        }


class Imovel(models.Model):
    class TipoImovel(models.TextChoices):
      RESIDENCIAL = "residencial"
      COMERCIAL = "comercial"
      RURAL = "rural"

    name = models.CharField(default="", blank=True, max_length=256)
    image = models.ImageField(upload_to='uploads/imoveis/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/imoveis/', blank=True, null=True)

    leilao = GenericRelation(Leilao)
    tipo_imovel = models.CharField(max_length=256, choices=TipoImovel.choices)

    logradouro = models.CharField(default="", blank=True, max_length=256)
    bairro = models.CharField(default="", blank=True, max_length=256)
    numero = models.CharField(default="", blank=True, max_length=256)
    cep = models.CharField(default="", blank=True, max_length=256)

    cidade = models.CharField(default="", blank=True, max_length=256)
    estado = models.CharField(max_length=2, choices=Estados.choices)

    deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:3000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:3000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:3000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, default_size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(default_size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


class Veiculo(models.Model):
    class TipoVeiculo(models.TextChoices):
        MOTO = "moto"
        CARRO = "carro"
        VAN = "van"

    name = models.CharField(default="", blank=True, max_length=256)
    image = models.ImageField(upload_to='uploads/veiculos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/veiculos/', blank=True, null=True)

    leilao = GenericRelation(Leilao)
    tipo_veiculo = models.CharField(max_length=5, choices=TipoVeiculo.choices)
    placa = models.CharField(default="", max_length=7, blank=True)
    ano = models.DateField(blank=True, null=True)

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:3000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:3000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:3000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, default_size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(default_size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail