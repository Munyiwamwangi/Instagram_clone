from django.shortcuts import render
from .models import Profile, Comment
# Create your views here.


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "about.html")

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = User.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
