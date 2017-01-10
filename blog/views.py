from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from . models import Post, Category
from . forms import PostForm, CommentForm, PostFormEdit, CountryForm
#Подключаем пагинатор
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'blog/base.html')


def me(request):
    return render(request, 'blog/me.html')


def post_list(request):
    all_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {"posts": all_post}
    context.update(get_categories())
    paginator = Paginator(all_post, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'post': post}, context)


def get_categories():
    all_categories = Category.objects.all()
    count = all_categories.count()
    return {'cat': all_categories, 'count': count}


# def index(request):
#     posts = Post.objects.all().order_by("-published_date")
#     context = {"posts": posts}
#     context.update(get_categories())
#     return render(request, "blog/article.html", context)


def category(request, pk=None):
    # c = get_o
    posts = Post.objects.filter(category__pk=pk).order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/post_list.html", context)


def search(request):
    print(request.method)
    print(request.POST)

    if request.method == 'POST':
        query = request.POST['query']
        posts = Post.objects.filter(title__icontains=query).order_by("-published_date")
    else:
        posts = []

    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    context.update(get_categories())
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        country_form = CountryForm()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            country_form.COUNTRY = CountryForm('UA')
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostFormEdit(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostFormEdit(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')