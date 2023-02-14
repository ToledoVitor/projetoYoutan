import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from youtan_django.core.models import (
    EntidadeFinanceira,
    Lance,
    Leilao,
    Imovel,
    Veiculo,
)


class Command(BaseCommand):
    help = "Esse comando tem o propósito de popular todos os dados necessários \
            para que seja possível testar o projeto. Estes dados não são reais \
            e não devem ser usados nunca em produção"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        user = User.objects.all().exists()
        if not user:
            User.objects.create_superuser(username='admin',
                                          email='admin@mail.com',
                                          password='admin')
            self.stdout.write(
                self.style.SUCCESS("SuperUser criado com sucesso")
            )

        entidades_existem = EntidadeFinanceira.objects.all().exists()
        if not entidades_existem:
            self.create_entidades()
            self.stdout.write(
                self.style.SUCCESS("Entidades Financeiras criadas com sucesso")
            )

        imoveis_existem = Imovel.objects.all().exists()
        if not imoveis_existem:
            self.create_imoveis()
            self.stdout.write(
                self.style.SUCCESS("Imoveis criados com sucesso")
            )

        veiculos_existem = Veiculo.objects.all().exists()
        if not veiculos_existem:
            self.create_veiculos()
            self.stdout.write(
                self.style.SUCCESS("Veiculos criados com sucesso")
            )

        leiloes_existem = Leilao.objects.all().exists()
        if not leiloes_existem:
            self.create_leiloes()
            self.stdout.write(
                self.style.SUCCESS("Leiloes criados com sucesso")
            )

        lances_existem = Lance.objects.all().exists()
        if not lances_existem:
            self.create_lances()
            self.stdout.write(
                self.style.SUCCESS("Lances criados com sucesso")
            )


    def create_entidades(self):
        EntidadeFinanceira.objects.create(
            name="Leilões Entidades Financeiras", cnpj="24.391.770/000"
        )
        EntidadeFinanceira.objects.create(
            name="Moura Instituições financeiras", cnpj="48.102.168/000"
        )
        EntidadeFinanceira.objects.create(
            name="Pague pouco finanças", cnpj="81.667.762/000"
        )

    def create_imoveis(self):
        lagos_path = os.path.dirname(os.path.realpath(__file__)) + "/images/imoveis/casa_praia.jpg"
        Imovel.objects.create(name="Casa Região dos Lagos",
                              image=lagos_path,
                              thumbnail=lagos_path,
                              tipo_imovel=Imovel.TipoImovel.RESIDENCIAL,
                              logradouro="Rua dos Lagos",
                              bairro="Bairro Cabo Frito",
                              numero="200",
                              cep="22220000",
                              cidade="Cabo Frio",
                              deleted=False)


        rural_path = os.path.dirname(os.path.realpath(__file__)) + "/images/imoveis/casa_campo.jpg"
        Imovel.objects.create(name="Casa Rural - MG",
                              image=rural_path,
                              thumbnail=rural_path,
                              tipo_imovel=Imovel.TipoImovel.RURAL,
                              logradouro="Rua dos Limões",
                              bairro="Bairro do Tanque",
                              numero="1002",
                              cep="15000000",
                              cidade="Três corações",
                              estado="MG",
                              deleted=False)

    def create_veiculos(self):
        r1200_path = os.path.dirname(os.path.realpath(__file__)) + "/images/veiculos/r1200.jpg"
        Veiculo.objects.create(name="BMW R1200 seminova",
                               image=r1200_path,
                               thumbnail=r1200_path,
                               tipo_veiculo=Veiculo.TipoVeiculo.MOTO,
                               placa="ASS6545",
                               ano="2019",
                               deleted=False)

        harley_path = os.path.dirname(os.path.realpath(__file__)) + "/images/veiculos/harley.jpg"
        Veiculo.objects.create(name="Harley Davidson - 2020",
                               image=harley_path,
                               thumbnail=harley_path,
                               tipo_veiculo=Veiculo.TipoVeiculo.MOTO,
                               placa="AXY2770",
                               ano="2020",
                               deleted=False)

        nivus_path = os.path.dirname(os.path.realpath(__file__)) + "/images/veiculos/nivus.jpg"
        Veiculo.objects.create(name="Volks NIvus",
                               image=nivus_path,
                               thumbnail=nivus_path,
                               tipo_veiculo=Veiculo.TipoVeiculo.CARRO,
                               placa="FVC5J48",
                               ano="2022",
                               deleted=False)

    def create_leiloes(self):
        entidades = EntidadeFinanceira.objects.all()
        imoveis = Imovel.objects.all()
        veiculos = Veiculo.objects.all()

        Leilao.objects.create(item_object=imoveis[0],
                              item_id=imoveis[0].id,
                              minimum_increment=100000.00,
                              entidade_financeira=entidades[0],
                              ended=False)

        Leilao.objects.create(item_object=imoveis[1],
                              item_id=imoveis[1].id,
                              minimum_increment=250000.00,
                              entidade_financeira=entidades[1],
                              ended=False)

        Leilao.objects.create(item_object=veiculos[0],
                              item_id=veiculos[0].id,
                              minimum_increment=6800.00,
                              entidade_financeira=entidades[2],
                              ended=False)

        Leilao.objects.create(item_object=veiculos[1],
                              item_id=veiculos[1].id,
                              minimum_increment=7500.00,
                              entidade_financeira=entidades[1],
                              ended=False)

        Leilao.objects.create(item_object=veiculos[2],
                              item_id=veiculos[2].id,
                              minimum_increment=10000.00,
                              entidade_financeira=entidades[0],
                              ended=False)

    def create_lances(self):
        leiloes = Leilao.objects.all()
        Lance.objects.create(created_by_id=1,
                             leilao_id=leiloes[0].id,
                             money_value=leiloes[0].minimum_increment,
                             deleted=False)

        Lance.objects.create(created_by_id=1,
                             leilao_id=leiloes[1].id,
                             money_value=leiloes[1].minimum_increment,
                             deleted=False)

        Lance.objects.create(created_by_id=1,
                             leilao_id=leiloes[1].id,
                             money_value=(leiloes[1].minimum_increment * 2),
                             deleted=False)

        Lance.objects.create(created_by_id=1,
                             leilao_id=leiloes[1].id,
                             money_value=(leiloes[1].minimum_increment * 3),
                             deleted=False)

        Lance.objects.create(created_by_id=1,
                             leilao_id=leiloes[2].id,
                             money_value=(leiloes[2].minimum_increment * 2),
                             deleted=False)

        Lance.objects.create(created_by_id=1,
                             leilao_id=leiloes[3].id,
                             money_value=leiloes[3].minimum_increment,
                             deleted=False)
