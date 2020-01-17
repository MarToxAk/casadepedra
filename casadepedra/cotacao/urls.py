from django.contrib import admin
from django.urls import path, re_path
from casadepedra.cotacao import views
from django.urls import include

app_name = 'cotacao'

urlpatterns = [
    path('', views.CriacaoCotacaoViews.as_view(), name='AddCotacaoUrls'),
    path('lista/', views.ListaCotacaoViews.as_view(), name='ListaCotacaoUrls'),
    path('lista/edicao/<int:pk>/',
         views.EdicaoCotacaoViews.as_view(), name='EdicaoCotacaoUrls'),
    re_path(r"lista/detalhe/(?P<pk>\d+)/$",
            views.DetalheCotacaoViews.as_view(), name='DetalheCotacaoUrls'),
]
