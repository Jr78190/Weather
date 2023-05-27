# le ficher views.py permet de recevoir des requetes et avoir des reponses
# il permet aussi d'interagir avec la base de donnée et des requetes ainsi que les templates 

from django.shortcuts import render

def index (request):
    return render(request, 'listings/index.html')


