import pytest
from model_bakery import baker

from django.test import RequestFactory
from django.contrib.auth.models import User

from youtan_django.core.models import (
    EntidadeFinanceira,
    Imovel,
    Leilao,
    Lance,
    Veiculo,
)

@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def common_user():
    return baker.make(User)


def test_create_entidade(rf, common_user):
    rf.post('api/v1/entidade-financeira/create')
    rf.user = common_user
    assert rf


def test_delete_entidade(rf, common_user):
    entidade = baker.make(EntidadeFinanceira)
    rf.get(f'api/v1/entidade-financeira/{entidade.id}/delete')
    rf.user = common_user
    assert rf


def test_get_leilao_info(rf, common_user):
    leilao = baker.make(Leilao)
    rf.get(f'api/v1/leilao/{leilao.id}/')
    rf.user = common_user
    assert rf


def test_get_leilao_lances(rf, common_user):
    leilao = baker.make(Leilao)
    rf.get(f'api/v1/leilao/{leilao.id}/lances')
    rf.user = common_user
    assert rf


def test_create_leilao_lance(rf, common_user):
    leilao = baker.make(Leilao)
    rf.post(f'api/v1/leilao/{leilao.id}/create_leilao_lance')
    rf.user = common_user
    assert rf


def test_get_lance_info(rf, common_user):
    lance = baker.make(Lance)
    rf.get(f'api/v1/lance/{lance.id}/')
    rf.user = common_user
    assert rf


def test_delete_lance(rf, common_user):
    lance = baker.make(Lance)
    rf.post(f'api/v1/lance/{lance.id}/delete')
    rf.user = common_user
    assert rf


def test_get_imovel_info(rf, common_user):
    imovel = baker.make(Imovel)
    rf.get(f'api/v1/imovel/{imovel.id}')
    rf.user = common_user
    assert rf


def test_get_imovel_lances(rf, common_user):
    imovel = baker.make(Imovel)
    rf.get(f'api/v1/imovel/{imovel.id}/lances')
    rf.user = common_user
    assert rf


def test_get_veiculo_info(rf, common_user):
    veiculo = baker.make(Veiculo)
    rf.get(f'api/v1/imovel/{veiculo.id}')
    rf.user = common_user
    assert rf


def test_get_veiculo_lances(rf, common_user):
    veiculo = baker.make(Veiculo)
    rf.get(f'api/v1/veiculo/{veiculo.id}/lances')
    rf.user = common_user
    assert rf
