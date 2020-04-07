from django.urls import path
from app_two import views

# TEMPLATE URLS
app_name = 'app_two'

urlpatterns = [
    path('', views.index),
    path('help/', views.help, name='help'),
    path('headings/', views.headings, name='headings'),
    path('dataentry/', views.relations, name='relations'),
    path('import_text/', views.import_text, name='import_text'),
    path('screens/', views.screens, name='screens'),
    path('update_text/', views.update_text, name='update_text'),
]
