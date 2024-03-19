from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    #path('' , views.login_user , name = 'login_form'),
    path('sign_up' , views.sign_up , name = 'sign_up'),
    path('login_form' , views.login_user , name = 'login_form'),
    path('login_view' , views.login_view , name = 'login_view'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup_submit' , views.signup_submit , name = 'signup_submit')
]