from django.contrib import admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from youtan_django.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

    path('api/v1/lances/', views.LanceView.as_view()),
    path('api/v1/lances/<int:lance_id>/', views.LanceView.as_view()),

    path('api/v1/houses/', views.HouseView.as_view()),
    path('api/v1/houses/<int:house_id>', views.HouseView.as_view()),

    path('api/v1/vehicles/', views.VehicleView.as_view()),
    path('api/v1/vehicles/<int:vehicle_id>', views.VehicleView.as_view()),

    path('api/v1/leiloes/', views.LeiloesView.as_view()),
    path('api/v1/<int:leilao_id>/leilao/', views.LeilaoDetailView.as_view()),

    path('api/v1/entidade-financeira/', views.EntidadeFinanceiraView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
