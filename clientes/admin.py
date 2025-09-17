from django.contrib import admin
from .models import Cliente, Imovel, Contrato

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email', 'cnpj')
    list_filter = ('nome', 'email')

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'bairro', 'cidade', 'valor_aluguel', 'disponivel')
    search_fields = ('endereco', 'bairro', 'cidade', 'valor_aluguel')
    list_filter = ('disponivel', 'cidade', 'bairro', 'valor_aluguel')
    ordering = ('cidade', 'valor_aluguel')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'imovel', 'data_inicio', 'data_fim', 'valor_mensal')
    search_fields = ('cliente__nome', 'imovel__endereco')
    list_filter = ('data_inicio', 'data_fim')

class ValorAluguelFilter(admin.SimpleListFilter):
    title = 'Valor do Aluguel'
    parameter_name = 'valor_aluguel'

    def lookups(self, request, model_admin):
        return [
            ("baixo", "Até R$ 1000"),
            ("medio", "De R$ 1000 a R$ 3000"),
            ("alto", "Acima de R$ 3000"),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'baixo':
            return queryset.filter(valor_aluguel__lt=1000)
        if self.value() == 'medio':
            return queryset.filter(valor_aluguel__gte=1000, valor_aluguel__lte=3000)
        if self.value() == 'alto':
            return queryset.filter(valor_aluguel__gt=3000)
        return queryset
