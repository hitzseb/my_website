from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Category, Post, Comment, Response
from .forms import CategoryForm, PostForm, CommentForm, ResponseForm

# user views

def blog(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'blog.html', {'post_list': post_list, 'category_list': category_list})

def post_by_category(request, category):
    post_list = Post.objects.filter(category__name=category)
    category_list = Category.objects.all()
    category_list = Category.objects.all()
    return render(request, 'blog.html', {'post_list': post_list, 'category_list': category_list})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    category_list = Category.objects.all()
    comment_form = CommentForm()
    response_form = ResponseForm()
    return render(request, 'post.html', {'post': post, 'category_list': category_list, 'comment_form': comment_form, 'response_form': response_form})

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post', pk=post_id)

    return render(request, 'post.html', {'post': post, 'form': form})

# admin views

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    return render(request, 'admin.html', {'category_list': category_list, 'post_list': post_list})

@user_passes_test(is_admin)
def category_form(request, pk=None):
    if pk:
        category = get_object_or_404(Category, pk=pk)
    else:
        category = None

    form = CategoryForm(request.POST or None, instance=category)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin')

    return render(request, 'category_form.html', {'form': form, 'category': category})

@user_passes_test(is_admin)
def post_form(request, pk=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
    else:
        post = None

    form = PostForm(request.POST or None, instance=post)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin')

    return render(request, 'post_form.html', {'form': form, 'post': post})

@user_passes_test(is_admin)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('admin')

@user_passes_test(is_admin)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('admin')

@user_passes_test(is_admin)
def add_response(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form = ResponseForm(request.POST or None)

    if form.is_valid():
        response = form.save(commit=False)
        response.comment = comment
        response.save()
        return redirect('post', pk=comment.post.id)

    return render(request, 'post.html', {'post': post, 'form': form})