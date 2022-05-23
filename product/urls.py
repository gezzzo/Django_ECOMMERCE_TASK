from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('newproducts', views.newproducts, name='newproducts'),
    path('category/<int:categoryid>/', views.categories, name='category'),
    path('product/<int:product_Id>/', views.Product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('additem/<int:product_id>/', views.additem, name='additem'),
    path('deleteitem/<int:product_id>/', views.deleteitem, name='deleteitem'),
]
