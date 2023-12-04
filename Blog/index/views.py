from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Sport ,Review

# Create your views here.


def add_view(request:HttpRequest):
    if request.method == "POST":
        sport=Sport(name= request.POST["name"],description=request.POST["description"],is_published=request.POST["is_published"],published_at=request.POST["published_at"],rating=request.POST["rating"],category=request.POST["category"], image=request.FILES["image"] )
        sport.save()

        return redirect("index:home_view")
    return render(request, "index/add.html", {"categories" : Sport.categories})


def home_view (request : HttpRequest):
   
   if 'name' in request.GET:
       keyword = request.GET.get("name")
       sport = Sport.objects.filter(name__contains = keyword)
   elif "category" in request.GET:
       sport = Sport.objects.filter(category=request.GET['category'])
   else:
        sport = Sport.objects.all()
   return render(request,"index/home.html",{'sport': sport ,"categories" : Sport.categories })


def details_view(request : HttpRequest , sport_id):
    sport1 = Sport.objects.get(id =sport_id)
    reviews = Review.objects.filter(sport=sport1)
    
    return render (request,"index/details.html", {"sport1":sport1 ,"categories" : Sport.categories, "reviews" : reviews})


def update_view(request : HttpRequest , sport_id):

    sport1 = Sport.objects.get(id =sport_id)

    if request.method == "POST":
        sport1.name= request.POST["name"]
        sport1.description=request.POST["description"]
        sport1.is_published=request.POST["is_published"]
        sport1.published_at=request.POST["published_at"]
        sport1.rating = request.POST["rating"]
        sport1.category = request.POST["category"]
        image=request.FILES["image"]
        sport1.save()

        return redirect('index:details_view', sport_id=sport1.id)
    
    return render(request, "index/update.html", {"sport1":sport1, "categories"  : Sport.categories})


def delet_view(request : HttpRequest ,sport_id):

    sport1 = Sport.objects.get(id =sport_id)
    sport1.delete()

    return redirect("index:home_view")

def add_review_view(request: HttpRequest, sport_id):

    if request.method == "POST":

        sport_obj = Sport.objects.get(id=sport_id)
        new_review = Review(sport = sport_obj , full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])
        new_review.save()

        return redirect("index:details_view", sport_id=sport_obj.id)
    
    
    return render(request, "index/details.html")
        
