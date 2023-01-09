from django.http import Http404

from youtan_django.core.models import EntidadeFinanceira, Lance, Leilao, Imovel, Veiculo 

from rest_framework.views import APIView
from rest_framework.response import Response

from youtan_django.serializers import (
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

        Leilao.objects.create(
            item_object=item_object,
            item_id=data['item_id'],
            minimum_increment=data['minimum_increment'],
            ended=False,
            entidade_financeira_id=1
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


class HouseView(APIView):
    def get(self, request, format=None):
        houses = (
            Imovel
            .objects
            .filter(deleted=False)
        )
        serializer = imovel_serializer.ImovelSerializer(houses, many=True)
        return Response(serializer.data)

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

    def delete(self, request, vehicle_id, format=None):
        try:
            vehicle = Veiculo.objects.get(id=vehicle_id)
        except Veiculo.DoesNotExist:
            raise Http404

        vehicle.deleted = True
        vehicle.save()
        return Response({})


class EntidadeFinanceiraView(APIView):
    def post(self, request, format=None):
        EntidadeFinanceira.objects.create()
        return Response({})

