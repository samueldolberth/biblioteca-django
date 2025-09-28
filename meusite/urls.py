from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),

    # página de listagem de livros
    path('livros/', views.livros, name='livros'),

    # página de cadastro de livros (formulário)
    path('', views.cadastro_livro, name='cadastro_livro'),

    # rota que salva livros
    path('salvar/', views.salvar_livro, name='salva_livros'),

    # ações de edição e exclusão
    path('excluir/<int:livro_id>/', views.exclui_livro, name='exclui_livro'),
    path('editar/<int:livro_id>/', views.edita_livro, name='edita_livro'),
]
