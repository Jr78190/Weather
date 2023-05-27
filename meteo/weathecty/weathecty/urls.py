# le ficher urls.py permet d'importer les views.py necessaire afin d'associer les URLS
# importation de include pour importer d'autre URLS

from django.urls import path, include 


urlpatterns = [
    path('', include('listings.urls') ),
]
