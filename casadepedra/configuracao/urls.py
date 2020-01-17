from django.urls import path
from casadepedra.configuracao import views as v


app_name = 'configuracao'

urlpatterns = [
    path('', v.ConfiguracaoTextoCreateView.as_view(), name='ConfiguracaoWpp'),
    path('atualizar/<int:pk>/', v.ConfiguracaoTextoUpdateView.as_view(), name='ConfiguracaoUpdateWpp'),
    path('lista/', v.ListaConfiguracaoViews.as_view(), name='ConfiguracaoTextoLista'),

]