from django.urls import path
from . import views

urlpatterns = [

    path('cadastro/', views.cadastra_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login_usuario'),

]