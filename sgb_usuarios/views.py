from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def cadastra_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome_usuario')
        sobrenome = request.POST.get('sobrenome_usuario')
        email = request.POST.get('email_usuario')
        senha = request.POST.get('senha_usuario')

        username = f'{nome.strip().lower()}.{sobrenome.strip().lower()}'

        usuario = User.objects.filter(username=username).first()

        if usuario:
            return render(request, 'feedback_fail.html')
        else:
            usuario = User.objects.create_user( # não precisou salvar pois o objects.create ja salva no banco de dados (testado)
                username=username,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            #return HttpResponse('Usuário cadastrado com sucesso!')
            return render(request, 'feedback_success.html')
            