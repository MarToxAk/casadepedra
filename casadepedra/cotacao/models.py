from django.db import models
from django.contrib.auth.models import User
from casadepedra.core.models import DataAlteracao
from casadepedra.configuracao.models import Configuracao, ConfiguracaoTexto, ConfiguracaoSvg
from phonenumber_field.modelfields import PhoneNumberField
from casadepedra.cotacao.entidades.tarefas import TarefasConfiguracao
from casadepedra.cotacao.servicos import servicos_models


# Create your models here.
class CotacaoModels(DataAlteracao):
    """Model definition for CotacaoModels."""
    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=False, 
        blank=False
    )
    nome = models.CharField(
        max_length=100,
        unique=True, 
        blank=False, 
        null=False
    )
    telefone = PhoneNumberField(
        
    )
    check_in = models.DateField(
        blank=False, 
        null=False
    )
    check_out = models.DateField(
        blank=False, 
        null=False
    )
    num_adultos = models.PositiveIntegerField(
        blank=False, 
        null=True
    )
    num_criancas = models.PositiveIntegerField(
        blank=False, 
        null=False,
    )
    idade_crianca1 = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    idade_crianca2 = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    idade_crianca3 = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    idade_crianca4 = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    valor_cotacao = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default=0.00,
    )
    # TODO: Define fields here

    class Meta:
        ordering = ('-criado',)

    def __str__(self):
        return str(self.pk)
    
    def html_area(self):
        #textonii_whatsapp = ''
        teste = servicos_models.TextoWppCotacao(self.check_in, self.check_out, self.num_adultos, self.num_criancas, self.idade_crianca1, self.idade_crianca2, self.idade_crianca3, self.idade_crianca4, self.valor_cotacao)
        valor = teste.verificador_datas(teste)
                
        return valor