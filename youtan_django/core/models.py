from io import BytesIO
from PIL import Image
from decimal import Decimal as D

from django.core.files import File
from django.db import models
from django.db.models.fields import DecimalField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from youtan_django.core.commons import Estados


class EntidadeFinanceira(models.Model):
    name = models.CharField(default="", blank=True, max_length=256)
    slug = models.SlugField(default="")
    cnpj = models.CharField(default="", blank=True, max_length=14)

    logradouro = models.CharField(default="", blank=True, max_length=256)
    bairro = models.CharField(default="", blank=True, max_length=256)
    numero = models.CharField(default="", blank=True, max_length=256)
    cep = models.CharField(default="", blank=True, max_length=256)

    cidade = models.CharField(default="", blank=True, max_length=256)
    estado = models.CharField(max_length=2, choices=Estados.choices)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Leilao(models.Model):
    # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/#generic-relations

    item_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    item_object = GenericForeignKey("item_type", "item_id")
    # That's the field that holds the other model instance (Imovel or Veiculo) 
    item_id = models.PositiveIntegerField()
    
    minimum_increment = DecimalField(max_digits=12, decimal_places=2, default=D(0))

    # When it get's closed by user or admin    
    ended = models.BooleanField(default=False)
    ended_at = models.DateTimeField(blank=True, null=True)

    # When it will automatically ends
    due_date = models.DateTimeField(blank=True, null=True)

    entidade_financeira = models.ForeignKey(EntidadeFinanceira, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'Leilao {self.id} - FIM: {self.due_date}'

    def get_latest_lance(self):
        return (
            self
            .lance_set
            .filter(deleted=False)
            .order_by("-created_at")
            .first()
        )


class Lance(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE)

    money_value = DecimalField(max_digits=12, decimal_places=2, default=D(0))

    # Custom field that represent's if the current vehicle is deleted to receive offers
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-money_value',)

    def __str__(self):
        return f'Lance {self.id} - ${self.money_value}'


class Imovel(models.Model):
    class TipoImovel(models.TextChoices):
      RESIDENCIAL = "residencial"
      COMERCIAL = "comercial"
      RURAL = "rural"

    name = models.CharField(default="", blank=True, max_length=256)
    slug = models.SlugField(default="")
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

    # Custom field that represent's if the object is valid
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    slug = models.SlugField(default="")
    image = models.ImageField(upload_to='uploads/veiculos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/veiculos/', blank=True, null=True)

    leilao = GenericRelation(Leilao)
    tipo_veiculo = models.CharField(max_length=5, choices=TipoVeiculo.choices)
    placa = models.CharField(default="", max_length=7, blank=True)

    # Custom field that represent's if the object is valid
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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