from django.shortcuts import render
from .models import Profile, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "about.html")

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    logged_user =request.user.id
    if request.method == 'POST':
        form = getProfile(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.infor = logged_user
            edit.save()
        return redirect('welcome')
    else:
        form = getProfile()

    return render(request,'Profile.html',{'form':form})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = User.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
