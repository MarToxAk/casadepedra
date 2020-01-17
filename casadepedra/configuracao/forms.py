from django import forms
from .models import ConfiguracaoTexto
from .widget import Texto_Area_WppWidget, CheckBox_HiddenWidget
from django.contrib.admin.widgets import AdminDateWidget
from pprint import pprint
from datetime import datetime
from django.db.models import Q



class ConfiguracaoTextoAtualizarForm(forms.ModelForm):
    """ConfiguracaoTextoAtualizarForm definition."""
    cotacao_texto = forms.CharField(
        widget = Texto_Area_WppWidget(),
        initial="Escreva o texto aqui"
    )
    check_in = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    check_out = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_dias = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_criancas = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    idade_crianca = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_pessoas = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_total = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_real = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_desconto = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_da_parcelas = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_da_parcelas_menos_etrada = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_50porc = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_parcela = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_parcela_mais_1 = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    porcentagem = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    porcentagem_mais_5 = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_da_entrada = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    
              

    # TODO: Define form fields here
    class Meta:
        model = ConfiguracaoTexto
        fields = '__all__'

class ConfiguracaoTextoForm(forms.ModelForm):
    """ConfiguracaoTextoForm definition."""
    cotacao_texto = forms.CharField(
        widget = Texto_Area_WppWidget(),
        initial="Escreva o texto aqui"
    )
    check_in = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    check_out = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_dias = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_criancas = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    idade_crianca = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_pessoas = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_total = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_real = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_desconto = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_da_parcelas = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_da_parcelas_menos_etrada = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_50porc = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_parcela = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    num_parcela_mais_1 = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    porcentagem = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    porcentagem_mais_5 = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    valor_da_entrada = forms.BooleanField(
        widget = CheckBox_HiddenWidget,
        label="",
        initial=False,
        required=False,
    )
    

    def clean(self):

        def funcao_cus(valor):
            ls = []
            for valor in valor:
                ls.append(valor)
            return (('  /  '.join(map(str, ls))))

        cleaned_data = super().clean()
        data_inicial = cleaned_data.get('data_inicial')
        data_final =  cleaned_data.get('data_final')
        def teste():
            resultado = ConfiguracaoTexto.objects.filter(Q(data_inicial__range=(data_inicial,data_final))|Q(data_inicial__range=(data_inicial,data_final))|Q(data_inicial__lt=data_inicial,data_final__gt=data_final))
            pprint(resultado.count())
            if resultado.count() == 0:
                return False
            else:
                return True
                

        pprint(teste())
        if teste() == True:
            resultado = ConfiguracaoTexto.objects.filter(Q(data_inicial__range=(data_inicial,data_final))|Q(data_inicial__range=(data_inicial,data_final))|Q(data_inicial__lt=data_inicial,data_final__gt=data_final))
            msg = "Essa data já esta sendo utilizada por outra configuração."
            self.add_error('data_inicial', msg)
            self.add_error('data_final', msg)
            raise forms.ValidationError(
                    "As datas escolhidas já estão sendo usada por >> "
                    f"{funcao_cus(resultado)} (Tem {len(resultado)} Datas nesse intervalo)"
                )
            
        else:
            return cleaned_data

            

    # TODO: Define form fields here
    class Meta:
        model = ConfiguracaoTexto
        fields = '__all__'