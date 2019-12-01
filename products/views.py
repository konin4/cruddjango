from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductForm
from django.contrib import messages


def index(request):
    return render(request,'index.html')


def cadastro(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/listar')
    else:
        form = ProductForm()
    return render(request, 'cadastro.html', {'form': form})

def listar(request):
    products = Product.objects.all()
    return render(request, 'listar.html', {'products': products})



def editar(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)

    if form.is_valid():
        form.save()
        return redirect('/listar')

    #else:

    return render(request, 'editar.html', {'product': product})


def deletar(request, id):
    form = Product.objects.get(id=id)  
    form.delete()  
    return redirect("/listar")
    # form = Product.objects.get(id=id)

    # if request.method == "POST":
    #     form.delete()
    #     messages.success(request,'Deletado')
    #     return redirect('/listar')
        

    # else:
    #     form = ProductForm(instance=form)
    # return render(request, 'deletar.html', {'form': form})
    
# Create your views here.
