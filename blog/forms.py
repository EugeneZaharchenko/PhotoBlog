from django import forms
from .models import Post, Comment, Strana, Category
from django_countries.widgets import CountrySelectWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'country', 'category')
        exclude = ('published_date', 'author')
        widgets = {'country': CountrySelectWidget()}


class PostFormEdit(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
        exclude = ('published_date', 'author', 'country')
        widgets = {'country': CountrySelectWidget()}


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)


class CountryForm(forms.ModelForm):

    class Meta:
        model = Strana
        fields = ('COUNTRY',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',  'created_date', 'mail', 'gender')