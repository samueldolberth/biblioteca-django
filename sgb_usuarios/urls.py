from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    path('cadastro/', views.cadastra_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout_usuario/', views.logout_usuario, name='logout'),

    # redefinição de senha

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="usuarios/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuarios/password_reset_done.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/password_reset_confirm.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuarios/password_reset_complete.html"), name="password_reset_complete"),

]