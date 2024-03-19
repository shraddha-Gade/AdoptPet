from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cat , Dog
from django.contrib.auth.decorators import login_required

@login_required
def add_cat(request):
    return render(request, 'add_cat.html')

@login_required
def add_dog(request):
    return render(request, 'add_dog.html')


def submitted_cat(request):
    if request.method == 'POST':
        print("Submitted view reached")
        name = request.POST.get('pet_name')
        gender = request.POST.get('pet_gender')
        breed = request.POST.get('pet_breed')
        age = request.POST.get('pet_age')
        vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        city = request.POST.get('pet_city')
        description = request.POST.get('pet_description')
        image = request.FILES.get('pet_image')

        pet1 = Cat(name=name, gender=gender, breed=breed, age=age, vaccinated=vaccinated,
                   city=city, description=description, image=image)
        pet1.save()
        n = 'Pet Added'
        messages.success(request, 'Pet Added Successfully')
        return redirect('home')  # Redirect to the add_pet page after successful form submission

    return render(request, 'add_cat.html')  # Render the same page if the request method is not POST or form submission fails

def submitted_dog(request):
    if request.method == 'POST':
        print("Submitted view reached")
        name = request.POST.get('pet_name')
        gender = request.POST.get('pet_gender')
        breed = request.POST.get('pet_breed')
        age = request.POST.get('pet_age')
        vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        city = request.POST.get('pet_city')
        description = request.POST.get('pet_description')
        image = request.FILES.get('pet_image')

        pet1 = Dog(name=name, gender=gender, breed=breed, age=age, vaccinated=vaccinated,
                   city=city, description=description, image=image)
        pet1.save()
        n = 'Pet Added'
        messages.success(request, 'Pet Added Successfully')
        return redirect('home')  # Redirect to the add_pet page after successful form submission

    return render(request, 'add_dog.html')  # Render the same page if the request method is not POST or form submission fails


def cats_view(request):
    cats = Cat.objects.all()  # Retrieve all cats from the database
    return render(request, 'cats_available.html', {'cats': cats})


def dogs_view(request):
    dogs = Dog.objects.all()  # Retrieve all cats from the database
    return render(request, 'dogs_available.html', {'dogs': dogs})

def search_results(request):
    # Get the selected pet type and city from the request parameters
    pet_type = request.GET.get('pet_type')
    city = request.GET.get('city')

    # Filter pets based on the selected pet type and city
    if pet_type == 'cat':
        pets = Cat.objects.filter(city = city)
    elif pet_type == 'dog':
        pets = Dog.objects.filter(city = city)
    else:
        # Handle other pet types or return an empty queryset
        pets = []


    # Pass the filtered pets to the template
    context = {
        'pets': pets,
        'selected_pet_type': pet_type,
        'selected_city': city
    }
    return render(request, 'search_results.html', context)


def available_cat_breeds(request):
    breed = request.GET.get('pet_breed')
    city =  request.GET.get('pet_city')

    pets = Cat.objects.filter(city = city , breed = breed)

    return render(request , 'available_cat_breeds.html' , {'pets' : pets})



def available_dog_breeds(request):
    breed = request.GET.get('pet_breed')
    city =  request.GET.get('pet_city')

    pets = Dog.objects.filter(city = city , breed = breed)

    return render(request , 'available_dog_breeds.html' , {'pets' : pets})