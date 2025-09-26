from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def cadastra_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome_usuario = request.POST('nome_usuario')
        email = request.POST('email')
        senha = request.POST('senha')

        usuario = User.objects.filter(username=nome_usuario).first()
        if usuario:
            return HttpResponse('Usuário já existe! Tente outro nome de usuário.')
        else:
            usuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
            usuario.save()
            return HttpResponse('Usuário cadastrado com sucesso!')