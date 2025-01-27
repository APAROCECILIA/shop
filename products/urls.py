from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Home page
    path('error/', views.error, name='404'),     
    path('cart/', views.cart, name='cart'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('contact/', views.contact, name='contact'), 
    path('shopdetail/', views.shopdetail, name='shopdetail'), 
    path('shop/', views.shop, name='shop'), 
    path('testimonial/', views.testimonial, name='testimonial'), 
]

