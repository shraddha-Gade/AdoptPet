from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Cat , Dog
from django.contrib.auth.decorators import login_required
from sign_up.models import CustomUser

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

def cat_profile(request, cat_id):
    # Retrieve the Cat object with the given ID, or return a 404 error if not found
    cat = get_object_or_404(Cat, id=cat_id)

    owner = cat.added_by
    # Pass the cat object to the template for rendering
    return render(request, 'pet_profile.html', {'pet': cat , 'owner' : owner})

def dog_profile(request, dog_id):
    # Retrieve the Dog object with the given ID, or return a 404 error if not found
    dog = get_object_or_404(Dog, id=dog_id)

    owner = dog.added_by

    # Pass the cat object to the template for rendering
    return render(request, 'pet_profile.html', {'pet': dog, 'owner' : owner})


def update_cat_profile(request , cat_id):
    cat = Cat.objects.get(pk=cat_id)

    if request.method == 'POST':
    # Access and update pet information from request.POST dictionary

        cat.name = request.POST['pet_name']
        cat.breed = request.POST['pet_breed']
        cat.gender = request.POST['pet_gender']
        cat.age = request.POST['pet_age']
        cat.vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        cat.city = request.POST['pet_city']
        cat.description = request.POST['pet_description']
        cat.image = request.FILES.get('pet_image')
        cat.available = True if request.POST.get('pet_available') == 'yes' else False
        

        # Additional fields (if applicable)

        # Image handling (if applicable)
        # You'll need to implement image upload validation and saving logic here

        cat.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('cat_profile', cat_id = cat.id)  # Replace with your success URL

    context = {'pet': cat}
    return render(request, 'update_cat.html', context)

def delete_cat_profile(request, cat_id):

    cat = Cat.objects.get(pk=cat_id)
    user = cat.added_by
    if request.method == 'POST':
        cat.delete()  # Delete the Cat object
        return redirect('cat_added_by_user' , user_id = user.id)  # Replace with your success URL (e.g., cat list)

    context = {'pet': cat , 'user':user}  # Pass the cat object to the template for confirmation (optional)
    return render(request, 'delete_cat_confirmation.html', context)  # Optional confirmation template

def update_dog_profile(request , dog_id):
    dog = Dog.objects.get(pk=dog_id)

    if request.method == 'POST':
    # Access and update pet information from request.POST dictionary

        dog.name = request.POST['pet_name']
        dog.breed = request.POST['pet_breed']
        dog.gender = request.POST['pet_gender']
        dog.age = request.POST['pet_age']
        dog.vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        dog.city = request.POST['pet_city']
        dog.description = request.POST['pet_description']
        dog.image = request.FILES.get('pet_image')
        dog.available = True if request.POST.get('pet_available') == 'yes' else False
        

        # Additional fields (if applicable)

        # Image handling (if applicable)
        # You'll need to implement image upload validation and saving logic here

        dog.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('dog_profile', dog_id = dog.id)  # Replace with your success URL

    context = {'pet': dog}
    return render(request, 'update_dog.html', context)

def delete_dog_profile(request, dog_id):

    dog = Dog.objects.get(pk=dog_id)
    user = dog.added_by
    if request.method == 'POST':
        dog.delete()  # Delete the Cat object
        return redirect('dog_added_by_user' , user_id = user.id)  # Replace with your success URL (e.g., cat list)

    context = {'pet': dog , 'user':user}  # Pass the cat object to the template for confirmation (optional)
    return render(request, 'delete_dog_confirmation.html', context)  # Optional confirmation template