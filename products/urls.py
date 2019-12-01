from django.urls import path
from . import views

urlpatterns = [
    # path('base', views.base, name='base'),
    # path('', views.cadastro, name='cadastro'),
    # path('', views.listar, name='listar'),
    
    # path('products/<int:pk>/editar/', views.editar, name='editar'),
    # path('products/<int:pk>/deletar/', views.deletar, name='deletar'),


    path('index/', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
]