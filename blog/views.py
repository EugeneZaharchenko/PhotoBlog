from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from . models import Post, Category
# from taggit.models import Tag
from . forms import PostForm, CommentForm, PostFormEdit
# #Подключаем пагинатор
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


from PIL import Image, ImageDraw, ImageFont


# _default_font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf', 24)
#
#
# def add_text_overlay(image, text, font=_default_font):
#     rgba_image = image.convert('RGBA')
#     text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
#     image_draw = ImageDraw.Draw(text_overlay)
#     text_size_x, text_size_y = image_draw.textsize(text, font=font)
#     text_xy = ((rgba_image.size[0] / 2) - (text_size_x / 2), (rgba_image.size[1] / 2) - (text_size_y / 2))
#     image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 128))
#     image_with_text_overlay = Image.alpha_composite(rgba_image, text_overlay)
#
#     return image_with_text_overlay


def get_categories():
    all_categories = Category.objects.all()
    count = all_categories.count()
    return {'categories': all_categories, 'categories_count': count}


# def get_tags():
#     all_tags = Tag.objects.all()
#     return {'tags': all_tags}


class BaseView(TemplateView):
    template_name = 'blog/base.html'


# class PostListView(ListView):
#     template_name = 'blog/post_list.html'
#     model = Post
#     context_object_name = 'posts'
#     paginate_by = 2
#
#     def get(self, request, tag_slug=None):
#         posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#         if request.user.is_authenticated:
#             ctx = {"posts": posts}
#             tag = None
#
#             if tag_slug:
#                 tag = get_object_or_404(Tag, slug=tag_slug)
#             queryset = posts.filter(tags__in=[tag])
#             tags = {'tag': tag}
#
#             ctx.update(get_categories())
#             ctx.update(tags)
#
#             return render(request, self.template_name, ctx)
#         else:
#             return render(request, self.template_name, {})


def post_list(request):
    posts = Post.objects.all()
    tag = None

    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    # posts_list = posts.filter(tags__in=[tag])

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)  # 3 posts in each page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'page': page,
               'posts': posts,
               'tag': tag}
    context.update(get_categories())
    return render(request, 'blog/post_list.html', context)
#     val = {}
#     val['all_tags'] = Tag.objects.all()
#     all_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     paginator = Paginator(all_post, 3)
#     page = request.GET.get('page')
#     try:
#         post = paginator.page(page)
#     except PageNotAnInteger:
#         post = paginator.page(1)
#     except EmptyPage:
#         post = paginator.page(paginator.num_pages)
#     context = {"posts": post}
#     context.update(get_categories())
#     context.update(val)
#     return render(request, 'blog/post_list.html', context)


def category(request, pk=None):
    posts = Post.objects.filter(category__id=pk).order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/post_list.html", context)


# def tag(request, tag_slug=None):
#
#
#     val = dict()
#     val['all_tags'] = Tag.objects.all()
#     val['tags'] = Tag.objects.get(id=pk)
#     # val['all_post'] = Post.objects.filter(tag__name__icontains=val['tags'])
#     posts = Post.objects.filter(tag__name__icontains=val['tags'])
#     return render(request, "blog/post_list.html", val)


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
    # val = {}
    # val['all_tags'] = Tag.objects.all()
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    context.update(get_categories())
    # context.update(val)
    return render(request, 'blog/post_detail.html', context)


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
            send_mail('Комментарий', 'Автором: ' + str(auth) + ' был добавлен комментарий: ' + str(comm)
                      + '. Электронный адрес автора: ' + str(mail), mail, ['romanuks@ukr.net'])
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts_list')
