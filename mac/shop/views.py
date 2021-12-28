from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.

def index(request):
    #product=Product.objects.all()
    catprod=Product.objects.values('category')

    cats={item['category'] for item in catprod}
    allproduct=[]
    for cat in cats:
        product=Product.objects.filter(category=cat)
        n=len(product)
        nSlides=ceil(n/4)
        allproduct.append([product,nSlides,range(1,nSlides)])
    param={'products':allproduct}

    return render(request,'shop/index.html',param)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc= request.POST.get('desc', '')
        if name or email or phone or desc:
            contact=Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            return render(request, 'shop/contact.html', {'contact': contact})
        return render(request, 'shop/contact.html')
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return HttpResponse('search')

def productview(request,id):
    product = Product.objects.filter(id=id)
    return render(request,'shop/product.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')