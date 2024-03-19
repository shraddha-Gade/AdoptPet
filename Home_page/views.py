from django.shortcuts import render
from sign_up.models import CustomUser
from django.contrib.auth.decorators import login_required
from pet_rehome.models import Cat, Dog

# Create your views here.
def home_page(request):
    available_cats = Cat.objects.filter(is_available = True)
    available_dogs = Dog.objects.filter(is_available = True)
    return render(request , 'home_page.html' , {'available_cats' : available_cats , 'available_dogs' : available_dogs})
    #return render(request, 'home_page.html')


def cat_breeds(request):
    return render(request, 'cat_breeds.html')

def dog_breeds(request):
    return render(request, 'dog_breeds.html')



@login_required
def Myprofile(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)
