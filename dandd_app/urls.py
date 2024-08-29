from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('catalog/', views.product_list, name='product_list'),
    path('product/<str:sku>/', views.product_detail, name='product_detail'),
    path('search/', views.search_products, name='search_products'),
 #New authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='dandd_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing_page'), name='logout'),
    path('register/', views.register, name='register'),
]