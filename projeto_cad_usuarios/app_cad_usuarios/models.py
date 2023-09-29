from django.db import models

class Usuario(models.Model):
    #irá criar automaticamente um campo com números ordenador e não duplicaveis que represetará usuaria
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    
