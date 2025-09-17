from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Pet
from .forms import PetForm

def pet_list(request):
    q = request.GET.get('q', '').strip()
    pets = Pet.objects.all().order_by('-created_at')
    if q:
        pets = pets.filter(
            Q(name__icontains=q) | Q(species__icontains=q) | Q(breed__icontains=q)
        )
    return render(request, 'pets/pet_list.html', {'pets': pets, 'q': q})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets/pet_detail.html', {'pet': pet})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form, 'title': 'Crear Mascota'})

def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form, 'title': 'Editar Mascota'})

def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})
