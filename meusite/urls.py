from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #path('livros/', views.livros, name='livros'),
    #path('salva_livros/', views.salvar_livro, name='salva_livros'),

    path('livros/', views.cadastro_livro, name='cadastro_livro'),
    path('excluir/<int:livro_id>', views.exclui_livro, name='exclui_livro'),
    path('editar/<int:livro_id>', views.edita_livro, name='edita_livro'),
]