from django.http import Http404

from youtan_django.core.models import EntidadeFinanceira, Lance, Leilao, Imovel, Veiculo 

from rest_framework.views import APIView
from rest_framework.response import Response

from youtan_django.serializers import (
    entidade_serializer,
    imovel_serializer,
    lance_serializer,
    leilao_serializer,
    veiculo_serializer,
)

class LeiloesView(APIView):
    def get(self, request, format=None):
        leiloes = (
            Leilao
            .objects
            .filter(ended=False)
            .order_by('due_date')
            .all()
        )
        serializer = leilao_serializer.LeilaoSerializer(leiloes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data

        if not data['item_type']:
            raise Http404

        if data['item_type'] == 'house':
            item_object = Imovel.objects.get(id=data['item_id'])

        if data['item_type'] == 'vehicle':
            item_object = Veiculo.objects.get(id=data['item_id'])

        entidade_financeira = EntidadeFinanceira.objects.get(name=data['financial_entity'])
        Leilao.objects.create(
            item_object=item_object,
            item_id=data['item_id'],
            minimum_increment=data['minimum_increment'],
            entidade_financeira=entidade_financeira,
            ended=False,
        )
        return Response({})


class LeilaoDetailView(APIView):
    def get(self, request, leilao_id, format=None):
        try:
            leilao = Leilao.objects.get(id=leilao_id)
        except Leilao.DoesNotExist:
            raise Http404

        serializer = leilao_serializer.LeilaoSerializer(leilao, many=False)
        return Response(serializer.data)


class LanceView(APIView):
    def get(self, request, format=None):
        lances = (
            Lance
            .objects
            .filter(deleted=False)
        )
        serializer = lance_serializer.LanceSerializer(lances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        Lance.objects.create(
            money_value=data['value'],
            leilao_id=data['leilao_id'],
        )
        return Response({})

    def delete(self, request, lance_id, format=None):
        try:
            lance = Lance.objects.get(id=lance_id)
        except Lance.DoesNotExist:
            raise Http404

        lance.deleted = True
        lance.save()
        return Response({})


class HouseView(APIView):
    def get(self, request, format=None):
        houses = (
            Imovel
            .objects
            .filter(deleted=False)
        )
        serializer = imovel_serializer.ImovelSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if not data['image']:
            raise Http404

        Imovel.objects.create(
            name=data['name'],
            tipo_imovel=data['tipo_imovel'],
            logradouro=data['logradouro'],
            bairro=data['bairro'],
            numero=data['numero'],
            cep=data['cep'],
            cidade=data['cidade'],
            estado=data['estado'],
            image=data['image'],
        )
        return Response({})

    def delete(self, request, house_id, format=None):
        try:
            house = Imovel.objects.get(id=house_id)
        except Imovel.DoesNotExist:
            raise Http404

        house.deleted = True
        house.save()
        return Response({})


class VehicleView(APIView):
    def get(self, request, format=None):
        vehicles = (
            Veiculo
            .objects
            .filter(deleted=False)
        )
        serializer = veiculo_serializer.VeiculoSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if not data['image']:
            raise Http404

        Veiculo.objects.create(
            tipo_veiculo=data['tipo_veiculo'],
            placa=data['placa'],
            ano=data['ano'],
            image=data['image'],
        )
        return Response({})

    def delete(self, request, vehicle_id, format=None):
        try:
            vehicle = Veiculo.objects.get(id=vehicle_id)
        except Veiculo.DoesNotExist:
            raise Http404

        vehicle.deleted = True
        vehicle.save()
        return Response({})


class EntidadeFinanceiraView(APIView):
    def get(self, request, format=None):
        entidades = EntidadeFinanceira.objects.all()
        serializer = entidade_serializer.EntidadeFinanceiraSerializer(entidades, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Qual a regra de neg??cio??
        # Pelo que entendi, usu??rio n??o pode cadastrar, s?? admin
        return Response({})

