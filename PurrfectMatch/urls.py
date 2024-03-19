"""
URL configuration for PurrfectMatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from pet_rehome import views
from django.contrib.auth import views as auth_views
#from sign_up.views import logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('Home_page.urls')), 
    path('sign_up/', include('sign_up.urls')),
    path('sign_up/', include('django.contrib.auth.urls')), 
    #path('', include('sign_up.urls')),
    path('home/' , include('Home_page.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_pet/', include('pet_rehome.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
