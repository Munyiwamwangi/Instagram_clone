from django.shortcuts import render, redirect
from .models import Image, Profile, Comments
from django.contrib.auth.decorators import login_required
from .forms import getProfile, uploadPhoto, Comment

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    prof = Profile.objects.filter(infor=request.user.id)[0:1]
    return render(request, 'home.html', {"images": images, 'prof': prof})


def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = (request.GET.get("image")).name()
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any image name"
        return render(request, 'search.html', {"message": message})


def index(request):
    title = "Index Page"
    return render(request, 'index.html', {"title": title})


@login_required(login_url='/accounts/login/')
def edit_profile_info(request):
    logged_user = request.user.id
    if request.method == 'POST':
        form = getProfile(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.infor = logged_user
            edit.save()
        return redirect('welcome')
    else:
        form = getProfile()

    return render(request, 'profile.html', {'form': form})


@login_required(login_url='/accounts/login/')
def Photo(request):
    logged_user = request.user.id
    if request.method == 'POST':
        form = uploadPhoto(request.POST, request.FILES)
        if form.is_valid():
            Photo = form.save(commit=False)
            Photo.profile = logged_user
            Photo.save()
            return redirect('welcome')
    else:
        form = uploadPhoto()

    return render(request, 'upload.html', {'form': form})


@login_required(login_url='/accounts/login/')
def comment(request, image_id):

    image = Image.objects.get(id=image_id)

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

    comments = Comments.objects.filter(picture=image_id).all

    return render(request, "comment.html", {'form': form, "image": image, "comments": comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    users = request.user.id

    try:
        profile = Profile.objects.filter(infor=users).first()
        all_images = Image.objects.filter(infor=request.user.id).all()

    except ObjectDoesNotExist:
        return redirect('welcome')
    return render(request, "pofile_image.html", {"profile": profile, "all_images": all_images})