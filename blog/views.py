import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from . models import Post, Category, Tag
from . forms import PostForm, CommentForm, PostFormEdit
#Подключаем пагинатор
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail


def base(request):
    # сегодняшняя дата
    today = datetime.date.today()
    # выбираем юзеров по текущей дате
    new_users = User.objects.filter(date_joined__contains=today)
    return render(request, 'blog/base.html', {"new_users": new_users})


def post_list(request):
    val = {}
    val['all_tags'] = Tag.objects.all()
    all_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(all_post, 4)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {"posts": post}
    context.update(get_categories())
    context.update(val)
    return render(request, 'blog/post_list.html', context)


def get_categories():
    all_categories = Category.objects.all()
    count = all_categories.count()
    return {'cat': all_categories, 'count': count}


def category(request, id=None):
    posts = Post.objects.filter(category__id=id).order_by("-published_date")
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {"posts": post}
    context.update(get_categories())
    return render(request, "blog/post_list.html", context)


def tag (request, id):
    val = {}
    val['all_tags']=Tag.objects.all()
    val['posts'] = Post.objects.filter(tag__id=id).order_by("-published_date")
    paginator = Paginator(val['posts'], 4)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {"posts": post}
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
    val = {}
    val['all_tags'] = Tag.objects.all()
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    context.update(get_categories())
    context.update(val)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
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
        comm = request.POST.get('text')
        auth = request.POST.get('author')
        mail = request.POST.get('mail')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            send_mail('Комментарий', 'Автором: ' + str(auth) + ' был добавлен комментарий: ' + str(comm) + '. Электронный адрес автора: ' + str(mail), mail, ['romanuks@ukr.net'])
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')