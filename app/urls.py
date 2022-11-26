from django.urls import path
from .views import ProductListView, ProductCreateView
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('product', ProductListView.as_view(), name='app-product'),
    path('createproduct/', ProductCreateView.as_view(), name='app-createproduct'),
    path('update_product/<str:pk>/', views.update_product, name='app-product')
]
