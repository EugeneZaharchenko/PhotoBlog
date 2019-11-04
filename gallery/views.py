from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

# def gallery(request):
#     photos = Photo.objects.all()
#     return render(request, "galler_y/gallery.html", {"photos": photos})


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

# class MyFormView(View):
# form_class = MyForm
# initial = {'key': 'value'}
# template_name = 'form_template.html'
# def get(self, request, * args, ** kwargs):
# form = self.form_class(initial=self.initial)
# return render(request, self.template_name, {'form': form})
# def post(self, request, * args, ** kwargs):
# form = self.form_class(request.POST)
# if form.is_valid():
# # <process form cleaned data>
# return HttpResponseRedirect('/success/')
# return render(request, self.template_name, {'form': form})

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
