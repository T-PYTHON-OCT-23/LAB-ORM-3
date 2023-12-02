from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Product,Comment

def home_page(request:HttpRequest):
    comments=Comment.objects.all().order_by('-date')[0:5]
    return render(request,'main/home.html',{'comments':comments})

def add_page(request:HttpRequest):
    if not request.user.is_staff:
        return render(request,'main/not_authorized.html',status=401)
    if request.method=='POST':
        product=Product(name=request.POST['name'],description=request.POST['description'],price=request.POST['price'],quantity=request.POST['quantity'],brand=request.POST['brand'],image=request.FILES['image'],category=request.POST['category'])
        product.save()
        return redirect('main:browse_page')
    return render(request,'main/add.html',{'categories':Product.categories})

def browse_page(request : HttpRequest):
    product=Product.objects.all()
    return render(request, "main/browse.html", {"products" : product})

def detail_page(request : HttpRequest,product_id):
    try:
        product=Product.objects.get(id=product_id)
        if request.method=='POST':
            if not request.user.is_authenticated:
                return render(request, "main/not_authorized.html", status=401)
            new_comment=Comment(product=product,name=request.POST['name'],content=request.POST['content'],rating=request.POST['rating'])
            new_comment.save()
        comments=Comment.objects.filter(product=product)
        return render(request,'main/detail_page.html',{'product':product,'comments':comments})
    except Exception:
        return render(request,'main/not_exist.html')
def delete_product(request : HttpRequest,product_id):
    if not request.user.is_staff:
        return render(request,'main/not_authorized.html',status=401)
    product=Product.objects.get(id=product_id)
    product.delete()
    return redirect('main:browse_page')

def update_page(request : HttpRequest,product_id):
    if not request.user.is_staff:
        return render(request,'main/not_authorized.html',status=401)
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        product.name=request.POST['name']
        product.description=request.POST['description']
        product.price=request.POST['price']
        product.quantity=request.POST['quantity']
        product.brand=request.POST['brand']
        if 'image' in request.FILES:
            product.image=request.FILES['image']
        product.category=request.POST['category']
        product.save()
        return redirect('main:detail_page',product_id=product.id)
    return render(request,'main/update.html',{'product':product,'categories':Product.categories})

def not_exist(request : HttpRequest):
    return render(request,'main/not_exist.html')

def search_page(request : HttpRequest):
    if 'search' in request.GET:
        search_term=request.GET['search']
        product=Product.objects.filter(name__contains=search_term)
    else:
       product=Product.objects.all()
    return render(request,'main/search.html',{'products':product})

def category_view(request : HttpRequest,cat):
    product=Product.objects.filter(category=cat)
    return render(request,'main/search.html',{'products':product})



# Create your views here.
