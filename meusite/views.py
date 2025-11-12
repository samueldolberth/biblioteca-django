from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livro, Autor
from django.contrib.auth.decorators import login_required


# ---------- views home -------------

def index(request):
    return render(request, 'index.html')

def livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

# ---------- func crud --------------

def salvar_livro(request):
    if request.method == 'POST':
        titulo_livro = request.POST['titulo_livro']
        autor_livro = request.POST['autor_livro']
        editora = request.POST['editora']
        return render(request, 'livros.html', context={
            'titulo_livro': titulo_livro,
            'autor_livro': autor_livro,
            'editora': editora
        })
    return HttpResponse('Método não permitido', status=405)

@login_required  # anotação para proteger a view, só acessa se estiver logado
def cadastro_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        titulo = request.POST['titulo']
        autor_nome = request.POST['autor']
        ano_publicacao = request.POST['ano_publicacao']
        editora = request.POST['editora']

        # busca ou cria o autor
        autor, created = Autor.objects.get_or_create(nome=autor_nome)

        if livro_id:  # Se o ID do livro for fornecido, atualize o livro existente. Ele edita
            livro = get_object_or_404(Livro, id=livro_id)
            livro.titulo = titulo
            autor, created = Autor.objects.get_or_create(nome=autor) # puxa da classe autor
            livro.autor = autor
            livro.ano_publicacao = ano_publicacao
            livro.editora = editora
            livro.save()
        else:  # Caso contrário, crie um novo livro. Ele cria
            Livro.objects.create(
                titulo = titulo,
                autor = autor,
                ano_publicacao = ano_publicacao,
                editora = editora
            )
        return redirect('cadastro_livro')
    
    # objects é um gerenciador de modelos padrão do Django que permite interagir/consultar com o banco de dados
    # all é uma função que recupera todos os registros da tabela livro - é o select do BD
    
    autores = Autor.objects.all()  # Recupera todos os autores do banco de dados
    livros = Livro.objects.all()  # Recupera todos os livros do banco de dados
    return render(request, 'livros.html', {'livros': livros, 'autores': autores})

@login_required
def exclui_livro(request, livro_id):
    # get_object_or_404() - esta função busca no banco de dados um objeto da tabela Livro cujo campo id seja igual a livro_id. 
    # Se encontrar, retorna o objeto e guarda na variável livro. Se não encontrar, retorna uma página 404
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()
    # retorna ou permanece na página cadastra_livro
    return redirect('cadastro_livro')

def edita_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    autores = Autor.objects.all()
    livros = Livro.objects.all()

    if request.method == "POST":
        livro.titulo = request.POST['titulo']
        autor, created = Autor.objects.get_or_create(nome=autor)
        livro.autor = request.POST['autor']
        livro.ano_publicacao = request.POST['ano_publicacao']
        livro.editora = request.POST['editora']
        livro.save()
        return redirect('cadastro_livro')
    
    return render(request, 'livros.html', {'livros': livros,'autores': autores, 'livro_editar': livro})

def avaliacoes(request):
    return render(request, 'avaliacoes.html')

def salvar_avaliacao(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        avaliador = request.POST['avaliador']
        nota = request.POST['nota']
        comentario = request.POST['comentario']

        livro = get_object_or_404(Livro, id=livro_id)

        Avaliacao.objects.create(
            livro=livro,
            avaliador=avaliador,
            nota=nota,
            comentario=comentario
        )
        return redirect('avaliacoes')