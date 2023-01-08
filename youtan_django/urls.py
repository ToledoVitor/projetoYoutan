from django.contrib import admin
from django.urls import path, include

from youtan_django.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

    path('api/v1/entidade-financeira/create', views.create_entidade),
    path('api/v1/entidade-financeira/<int:entidade_id>/delete', views.delete_entidade),

    path('api/v1/leilao/<int:leilao_id>/', views.get_leilao_info),
    path('api/v1/leilao/<int:leilao_id>/lances', views.get_leilao_lances),
    path('api/v1/leilao/<int:leilao_id>/create_leilao_lance', views.create_leilao_lance),

    path('api/v1/lance/<int:lance_id>/', views.get_lance_info),
    path('api/v1/lance/<int:lance_id>/delete', views.delete_lance),

    path('api/v1/imovel/<int:imovel_id>/', views.get_imovel_info),
    path('api/v1/imovel/<int:imovel_id>/lances', views.get_imovel_lances),

    path('api/v1/veiculo/<int:veiculo_id>/', views.get_veiculo_info),
    path('api/v1/veiculo/<int:veiculo_id>/lances', views.get_veiculo_lances),
]
