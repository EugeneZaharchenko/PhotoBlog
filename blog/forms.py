from django import forms
from .models import Post, Comment, Category, Tag


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag', 'img')
        exclude = ('published_date', 'author')


class PostFormEdit(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
        exclude = ('published_date', 'author',)



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',  'created_date', 'mail', 'gender')