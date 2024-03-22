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
    path('cats/<int:cat_id>/', views.cat_profile, name='cat_profile'),
    path('dogs/<int:dog_id>/', views.dog_profile, name='dog_profile'),
    path('update_cat_profile/<int:cat_id>/', views.update_cat_profile, name='update_cat_profile'),
    path('delete_cat_profile/<int:cat_id>/', views.delete_cat_profile, name='delete_cat_profile'),
    path('update_dog_profile/<int:dog_id>/', views.update_dog_profile, name='update_dog_profile'),
    path('delete_dog_profile/<int:dog_id>/', views.delete_dog_profile, name='delete_dog_profile'),
    
]