from django.shortcuts import render

def error(request):
    return render(request, 'products/404.html')

def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')


def contact(request):
    return render(request, 'products/contact.html')

def index(request):
    return render(request, 'products/index.html')

def shopdetail(request):
    return render(request, 'products/shop-detail.html')

def shop(request):
    return render(request, 'products/shop.html')

def testimonial(request):
    return render(request, 'products/testimonial.html')
