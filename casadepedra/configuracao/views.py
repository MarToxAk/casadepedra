from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DetailView
from .models import ConfiguracaoTexto
from .forms import ConfiguracaoTextoForm, ConfiguracaoTextoAtualizarForm
# Create your views here.


class ConfiguracaoTextoCreateView(CreateView):
    model = ConfiguracaoTexto
    template_name = "configuracao/configuracao_texto_wpp.html"
    form_class = ConfiguracaoTextoForm
    success_url = '/'


class ConfiguracaoTextoUpdateView(UpdateView):
    model = ConfiguracaoTexto
    template_name = "configuracao/configuracao_texto_autalizar.html"
    form_class = ConfiguracaoTextoAtualizarForm
    success_url = '/'
    context_object_name = 'configuracao'

class ListaConfiguracaoViews(ListView):
    model = ConfiguracaoTexto
    context_object_name = 'configuracao'
    paginate_by = 12
    template_name = 'configuracao/configuracao_lista.html'
    def get_queryset(self):
        return ConfiguracaoTexto.objects.order_by('-criado' or '-modificado')

