from django import forms
import datetime
from datetime import timezone
from casadepedra.cotacao.models import CotacaoModels
from casadepedra.cotacao.widgets import RadioSelectButtonGroup, FormBootstrap, SelectOptionBootstrap, FormBootstrapHidden, SelectOptionBootstrapAction, FormBootstrapnoPage
from casadepedra.cotacao.servicos import servicos_tarefas
from pprint import pprint


CHOICE_IDADE = (
    ('', 'Sem Criança'),
    (0,'Zero Ano'),
    (1,'Um Ano'),
    (2,'Dois Anos'),
    (3,'Três Anos'),
    (4,'Quatro Anos'),
    (5,'Cinco Anos'),
    (6,'Seis Anos'),
    (7,'Sete Anos'),
    (8,'Oito Anos'),
    (9,'Nove Anos'),
    (10,'Dez Anos'),
    (11,'Onze Anos'),
    (12,'Doze Anos'),
    (13,'Treze Anos'),
    (14,'Quatorze Anos'),
    (15,'Quinze Anos'),
    (16,'Dezesseis Anos'),
    (17,'Dezessete Anos'),
)

class CotacaoForms(forms.ModelForm):
    
    nome = forms.CharField(
        required=True,
        label="Nome:",
        widget=FormBootstrap(
            attrs={'placeholder': 'Nome do Hospede', 'class': 'form-control'}),
    )
    telefone = forms.CharField(
        required=True,
        label="Telefone:",
        widget=FormBootstrap(
            attrs={'placeholder': '+55(xx)xxxxx-xxxx', 'class': 'form-control'}),
    )
    num_adultos = forms.ChoiceField(
        required=True,
        label="Numero de Adultos:",
        widget=SelectOptionBootstrap,
        choices=((1, 'Um Adulto'), (2, 'Dois Adultos'),
                 (3, 'Três Adultos'), (4, 'Quatro Adultos'), (5, 'Cinco Adultos')),
        initial=1,
    )
    num_criancas = forms.ChoiceField(
        required=True,
        label="Quantidade de Crianças:",
        widget=SelectOptionBootstrapAction,
        choices=((0, 'Sem Criança'), (1, 'Uma Criança'), (2, 'Duas Crianças'),
                 (3, 'Três Crianças'), (4, 'Quatro Crianças')),
        initial=0,
    )
    check_in = forms.DateField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Data da Entrada do Hospede', 'autocomplete': "off"}),
        label="Data do Check-In:"
    )
    check_out = forms.DateField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Data da Saida do Hospede', 'autocomplete': "off"}),
        label="Data do Check-Out:"
    )

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out =  cleaned_data.get('check_out')
        num_adultos = cleaned_data.get('num_adultos')
        num_criancas = cleaned_data.get('num_criancas')
        idade_crianca1 = cleaned_data.get('idade_crianca1')
        idade_crianca2 = cleaned_data.get('idade_crianca2')
        idade_crianca3 = cleaned_data.get('idade_crianca3')
        idade_crianca4 = cleaned_data.get('idade_crianca4')

        resposta = servicos_tarefas.ServicoCotacao().valor_diaria_api_omnibees(check_in, check_out, num_adultos, num_criancas, idade_crianca1, idade_crianca2, idade_crianca3, idade_crianca4)
        resposta = resposta['HotelStaysType']['HotelStays'][0]['Status']
        if resposta == 'Close':
            msg = "Essa data esta fechada"
            self.add_error('check_in', msg)
            self.add_error('check_out', msg)
            raise forms.ValidationError(
                    "A disponibilidade dessa data esta fechada!!"
            )
        else:
            return cleaned_data


    class Meta:
        model = CotacaoModels
        fields = ['nome', 'telefone', 'check_in', 'check_out', 'num_adultos', 'num_criancas', 'idade_crianca1', 'idade_crianca2', 'idade_crianca3', 'idade_crianca4',]

