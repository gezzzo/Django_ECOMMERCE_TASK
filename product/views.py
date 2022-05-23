from django.shortcuts import redirect, render
from .models import category,product,order
from django.contrib.auth.decorators import login_required

def index(request):
    allproducts = product.objects.all()
    categories = category.objects.all()
    return render(request,'pages/home.html',{'products':allproducts,"categories":categories})
    
def categories(request,categoryid):
    category_on = category.objects.get(id=categoryid)
    categories = category.objects.all()
    products = product.objects.all().filter(category_id=categoryid).order_by('-id')
    return render(request,'pages/category.html',{'category':category_on,"products":products,"categories":categories})

def newproducts(request):
    categories = category.objects.all()
    products = product.objects.all().order_by('-id')
    return render(request,'pages/allproducts.html',{"products":products,"categories":categories})

def Product(request,product_Id):
    categories = category.objects.all()
    product_byId = product.objects.get(id=product_Id)
    return render(request,'pages/product.html',{'product':product_byId,"categories":categories})

def about(request):
    categories = category.objects.all()
    return render(request,'pages/about.html',{"categories":categories})

def contact(request):
    categories = category.objects.all()
    return render(request,'pages/contact.html',{"categories":categories})

@login_required(login_url='/login/')
def cart(request):
    allcategory = category.objects.all()
    products = product.objects.all()
    orders = order.objects.filter(user_id=request.user.id)
    return render(request, 'pages/cart.html',{"products":products,"orders":orders,"categories":allcategory})

@login_required(login_url='/login/')
def additem(request,product_id):
    quantity=int(order.objects.filter(productid=product_id).count())
    if quantity >= 1:
        ca=order.objects.get(productid=product_id)
        order.objects.filter(productid=product_id).update(num=int(ca.num)+1)
    else:
        id = request.user.id
        carts=order(productid=product_id,user_id=id,num=1)
        carts.save()
    return redirect("/cart/")

@login_required(login_url='/login/')
def deleteitem(request,product_id):
    item=order.objects.get(id=product_id)
    item.delete()
    return redirect("/cart/")