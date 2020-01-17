from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DetailView
from casadepedra.cotacao.models import CotacaoModels
from casadepedra.cotacao.forms import CotacaoForms
from casadepedra.cotacao.entidades.tarefas import Tarefas, TarefasEdicao
from casadepedra.cotacao.servicos import servicos_tarefas
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from pprint import pprint
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse



class CriacaoCotacaoViews(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    permission_required = ('cotacao.add_cotacaomodel')
    model = CotacaoModels
    form_class = CotacaoForms
    template_name = 'cotacao/cotacao_criacao.html'
    def get_success_url(self):
        return reverse('cotacao:ListaCotacaoUrls')

    def post(self, request, *args, **kwargs):
        form = CotacaoForms(request.POST)

        if form.is_valid():
            pprint('Sucesso')
            autor = request.user
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            num_adultos = int(form.cleaned_data['num_adultos'])
            num_criancas = int(form.cleaned_data['num_criancas'])
            idade_crianca1 = form.cleaned_data['idade_crianca1']
            idade_crianca2 = form.cleaned_data['idade_crianca2']
            idade_crianca3 = form.cleaned_data['idade_crianca3']
            idade_crianca4 = form.cleaned_data['idade_crianca4']
            pprint(check_in)
            pprint(check_out)
            dados_cotacao = Tarefas(autor, nome, telefone, check_in, check_out,
                                    num_adultos, num_criancas, idade_crianca1, idade_crianca2, idade_crianca4, idade_crianca4)
            servicos_tarefas.ServicoCotacao().servico_criar_cotacao(
                cotacao=dados_cotacao)
            return redirect('cotacao:ListaCotacaoUrls')
        return render(request, 'cotacao/cotacao_criacao.html', {'form': form})


class EdicaoCotacaoViews(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    permission_required = ('cotacao.add_cotacaomodel')
    redirect_field_name = 'redirect_to'
    model = CotacaoModels
    form_class = CotacaoForms
    context_object_name = 'cotacoes'
    template_name = 'cotacao/cotacao_edicao.html'
    success_url = reverse_lazy('AddCotacaoUrls')

    def post(self, request, *args, **kwargs):

        form = CotacaoForms(request.POST)

        if form.is_valid():
            autor = User.objects.get(username=request.user)
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            num_adultos = form.cleaned_data['num_adultos']
            num_criancas = form.cleaned_data['num_criancas']
            crianca1 = form.cleaned_data['crianca1']
            crianca2 = form.cleaned_data['crianca2']
            crianca3 = form.cleaned_data['crianca3']
            crianca4 = form.cleaned_data['crianca4']
            parcela = form.cleaned_data['parcela']
            disconto = form.cleaned_data['disconto']
            pk = pk = kwargs['pk']

            dados_cotacao = TarefasEdicao(autor, nome, telefone, check_in, check_out,
                                          num_adultos, num_criancas, crianca1, crianca2, crianca3, crianca4, parcela, disconto, pk)
            servicos_tarefas.ServicoCotacao().servico_edicao_cotacao(
                cotacao=dados_cotacao)
            return redirect('AddCotacaoUrls')
        else:
            form = CotacaoForms
            return form


class DetalheCotacaoViews(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    permission_required = ('cotacao.add_cotacaomodel')
    redirect_field_name = 'redirect_to'
    model = CotacaoModels
    context_object_name = 'dados'
    template_name = 'cotacao/cotacao_detalhe.html'


class ListaCotacaoViews(ListView):
    model = CotacaoModels
    context_object_name = 'cotacoes'
    paginate_by = 12
    template_name = 'cotacao/cotacao_lista.html'
    def get_queryset(self):
        return CotacaoModels.objects.order_by('-criado' or '-modificado')

