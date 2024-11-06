from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def producto_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})
#Listar productos
def producto_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html',{'products': products})
#leer detalle
def producto_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/product_detail.html', {'product': product})

#Actualizar

def producto_update(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            form = ProductForm(instance=product)
        return render(request, 'products/product_form.html', {'form': form})

#eliminar

def producto_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

