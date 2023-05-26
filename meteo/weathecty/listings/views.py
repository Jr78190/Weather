# le ficher views.py permet de recevoir des requetes et avoir des reponses
# il permet aussi de s'occuper de la base des données et des requetes ainsi que les templates 

from django.http import HttpResponse 
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello World <h1>')


