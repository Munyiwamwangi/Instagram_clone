from django.shortcuts import render, redirect
from .models import Profile, Comment, Posts
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


@login_required(login_url='/accounts/login/')
def comment(request, image_id):

    post = Posts.objects.get(id=image_id)

    if request.method == 'POST':
        current_user = request.user
        form = Comment(request.POST)
        if form.is_valid:
            comments = form.save(commit=False)
            comments.user = current_user
            comments.picture = image.id
            comments.save()

            return redirect('welcome')
    else:
        form = Comment()

    comments = Comment.objects.filter(picture=image_id).all

    return render(request, "comment.html", {'form': form, "image": image, "comments": comments})



def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = User.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
