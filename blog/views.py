from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post
from .forms import CommentForm

def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_list': category_list})

def post_list(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'post_list.html', {'post_list': post_list, 'category_list': category_list})

def post_by_category(request, category):
    post_list = Post.objects.filter(category__name=category)
    category_list = Category.objects.all()
    category_list = Category.objects.all()
    return render(request, 'post_list.html', {'post_list': post_list, 'category_list': category_list})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    category_list = Category.objects.all()
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'category_list': category_list, 'comment_form': comment_form})

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_detail', pk=post_id)

    return render(request, 'post_detail.html', {'post': post, 'form': form})