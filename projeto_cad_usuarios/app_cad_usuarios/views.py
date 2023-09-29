from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html') 

def usuarios(request):
    novo_usuario = Usuario()
    # Extrair e salvar informações da tela para novo_usuario
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todoso os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
        #busca as informações no banco de dados
    }
    
    # Retornar os dados para  apagina de listagem de usuarios
    return render(request,'usuarios/usuarios.html', usuarios)
   
    