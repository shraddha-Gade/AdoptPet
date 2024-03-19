from django.urls import path

from . import views

urlpatterns = [
    
    path('add_cat' , views.add_cat , name = 'add_cat'),
    path('add_dog' , views.add_dog , name = 'add_dog'),
    path('submitted_cat' , views.submitted_cat , name = 'submitted_cat'),
    path('submitted_dog' , views.submitted_dog , name = 'submitted_dog'),
    path('cats/', views.cats_view, name='cats'),
    path('dogs/', views.dogs_view, name='dogs'),
    path('search/', views.search_results, name='search_results'),
    path('cat_breeds/', views.available_cat_breeds, name='available_cat_breeds'),
    path('dog_breeds/', views.available_dog_breeds, name='available_dog_breeds'),
]