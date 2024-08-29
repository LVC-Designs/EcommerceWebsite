from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Product, Category
from django.db.models import Q 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def landing_page(request):
    return render(request, 'dandd_app/landing_page.html')

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        all_products = Product.objects.filter(category_id=category_id).order_by('product_name')
    else:
        all_products = Product.objects.all().order_by('product_name')
    
    total_products = all_products.count()
    paginator = Paginator(all_products, 24)  # Show 24 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'total_products': total_products,
        'selected_category': category_id
    }
    return render(request, 'dandd_app/product_list.html', context)

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    return render(request, 'dandd_app/product_detail.html', {'product': product})



def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(english_description__icontains=query)
        ).distinct()
    else:
        products = Product.objects.none()

    context = {
        'products': products,
        'query': query
    }
    return render(request, 'dandd_app/search_results.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'dandd_app/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'dandd_app/register.html', {'form': form})