from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Strana
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required


def gallery(request):
    photos = Photo.objects.all()
    return render(request, "gallery/base.html", {"photos": photos})


@login_required()
def upload(request):
    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo_form.save()
            return redirect("gallery")
    form = PhotoForm()
    return render(request, "gallery/upload.html", {"form": form})


# def certain_photo(request, pk):
#     photo = get_object_or_404(Photo, pk=pk)
#     return render(request, 'gallery/index.html', {"photos": photo})


def get_countries():
    all_countries = Strana.objects.all()
    count = all_countries.count()
    return {'countries': all_countries, 'count': count}


def country(request, id=None):
    photos = Photo.objects.filter(country_id=id)
    context = {"photos": photos}
    context.update(get_countries())
    return render(request, "gallery/base.html", context)
