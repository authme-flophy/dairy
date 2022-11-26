from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import Product, Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm, CustomerForm, ProductUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.contrib import messages

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "app/product.html"
    context_object_name = "products"


def createproduct(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/createproduct')
    context = {
        'form': form
    }
    return render(request, 'app/createproduct.html', context)


def product(request):
    header = 'List of Products'
    queryset = Product.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
    }
    return render(request, 'app/product.html', context)


def update_product(request, pk):
    queryset = Product.objects.all()
    form = ProductUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/product')

    context = {
        'form': form
    }
    return render(request, 'app/product.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['customer', 'description', 'gender']
    template_name = "app/createproduct.html"
    success_url = "/"


def home(request):
    context = {
        'posts': Customer.objects.all(),
    }
    return render(request, 'app/home.html', context)


def about(request):
    return render(request, 'app/about.html', {'title': 'About Dairy'})
