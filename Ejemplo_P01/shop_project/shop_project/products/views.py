from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_list(request):
    q = request.GET.get('q','')
    if q:
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products, 'q':q})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form':form})

def product_update(request, pk):
    p = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=p)
    return render(request, 'products/product_form.html', {'form':form})

def product_delete(request, pk):
    p = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        p.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product':p})
