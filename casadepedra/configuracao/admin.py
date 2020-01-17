from django.contrib import admin
from .models import Configuracao, ConfiguracaoTexto, ConfiguracaoSvg
# Register your models here.

@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'parcela',
    )
    
@admin.register(ConfiguracaoTexto)
class ConfiguracaoTextoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cotacao_texto',
        'data_inicial',
        'data_final',
    )
    
@admin.register(ConfiguracaoSvg)
class ConfiguracaoSvgAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cotacao_texto',
        'data_inicial',
        'data_final',
    )