from django.forms import ModelForm
from .models import Photo, Strana
from django_countries.widgets import CountrySelectWidget


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {'country': CountrySelectWidget()}


class CountryForm(ModelForm):

    class Meta:
        model = Strana
        fields = ('COUNTRY',)