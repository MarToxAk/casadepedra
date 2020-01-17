from django.db import models
from django.db.models import Q
from pprint import pprint
from casadepedra.core.models import DataAlteracao


class Configuracao(models.Model):
    valor_inicial = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 

    )
    valor_final = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True, 
        blank=True
    )
    parcela = models.PositiveIntegerField()
    entrada = models.BooleanField()
    
    class Meta:
        ordering = ('pk',)
    
    def __str__(self):
        return str(f"R$ {self.valor_inicial} {'Acima' if self.valor_final == None else f'á R$ {self.valor_final}'} = {self.parcela}x com entrada {'Sim' if self.entrada == True else 'Não'}")
    
    
class ConfiguracaoTexto(DataAlteracao):
    nome = models.CharField(
        max_length=50,
        unique=True
    )
    cotacao_texto = models.TextField(
        null=False,
        blank= False,
    )
    data_inicial = models.DateField(
        unique=True,        
    )
    data_final = models.DateField(
        
    )
    desconto = models.PositiveIntegerField()
    padrao = models.BooleanField(
        default=False,
    )
    check_in = models.BooleanField(
        default=False
    )
    check_out = models.BooleanField(
        default=False
    )
    num_dias = models.BooleanField(
        default=False
    )
    num_criancas = models.BooleanField(
        default=False
    )
    idade_crianca = models.BooleanField(
        default=False
    )
    num_pessoas = models.BooleanField(
        default=False
    )
    valor_total = models.BooleanField(
        default=False
    )
    valor_real = models.BooleanField(
        default=False
    )
    valor_desconto = models.BooleanField(
        default=False
    )
    valor_da_parcelas = models.BooleanField(
        default=False
    )
    valor_da_parcelas_menos_etrada = models.BooleanField(
        default=False
    )
    valor_50porc = models.BooleanField(
        default=False
    )
    valor_da_entrada = models.BooleanField(
        default=False
    )
    num_parcela = models.BooleanField(
        default=False
    )
    num_parcela_mais_1 = models.BooleanField(
        default=False
    )
    porcentagem = models.BooleanField(
        default=False
    )
    porcentagem_mais_5 = models.BooleanField(
        default=False
    )
    
    
    class Meta:
        ordering=('nome',)
        
    def __str__(self):
        return str(f"{self.pk} - {self.nome}")

    def save(self, *args, **kwargs):
        if self.padrao:
            try:
                temp = ConfiguracaoTexto.objects.get(padrao=True)
                if self != temp:
                    temp.padrao = False
                    temp.save()
            except ConfiguracaoTexto.DoesNotExist:
                pass
        super(ConfiguracaoTexto, self).save(*args, **kwargs)
    
        
class ConfiguracaoSvg(models.Model):
    nome = models.CharField(
        max_length=50,
        unique=True
    )
    cotacao_texto = models.TextField(
        null=False, 
        blank= False,
    )
    data_inicial = models.DateField(
        
    )
    data_final = models.DateField(
        
    )
    
    class Meta:
        ordering=('nome',)
        
    def __str__(self):
        return self.nome