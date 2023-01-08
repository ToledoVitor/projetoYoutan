from django.views.decorators.http import require_GET, require_POST

from youtan_django.core.models import Leilao, Lance


@require_POST
def create_entidade(request):
    pass


@require_POST
def delete_entidade(request, entidade_id):
    pass


@require_GET
def get_leilao_info(request, leilao_id):
    pass


@require_GET
def get_leilao_lances(request, leilao_id):
    pass


@require_POST
def create_leilao_lance(request, leilao_id):
    pass


@require_GET
def get_lance_info(request, lance_id):
    pass


@require_POST
def delete_lance(request, lance_id):
    pass


@require_GET
def get_imovel_info(request, imovel_id):
    pass


@require_GET
def get_imovel_lances(request, imovel_id):
    pass


@require_GET
def get_veiculo_info(request, veiculo_id):
    pass


@require_GET
def get_veiculo_lances(request, veiculo_id):
    pass
