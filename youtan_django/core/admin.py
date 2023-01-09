from django.contrib import admin

from .models import EntidadeFinanceira, Leilao, Lance, Imovel, Veiculo

admin.site.register(EntidadeFinanceira)
admin.site.register(Leilao)
admin.site.register(Lance)
admin.site.register(Imovel)
admin.site.register(Veiculo)
