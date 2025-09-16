from django.contrib import admin
from .models import Cliente, Imovel, Contrato

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cnpj')
    search_fields = ('nome', 'email', 'cnpj')
    list_filter = ('nome', 'cnpj')

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'bairro', 'cidade', 'valor_aluguel', 'disponivel')
    search_fields = ('endereco', 'bairro', 'cidade')
    list_filter = ('disponivel', 'cidade')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'imovel', 'data_inicio', 'data_fim', 'valor_mensal')
    search_fields = ('cliente__nome', 'imovel__endereco')
    list_filter = ('data_inicio', 'data_fim')


