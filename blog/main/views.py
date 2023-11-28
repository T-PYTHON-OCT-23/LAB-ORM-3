from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm
from django.urls import reverse

def post_list(request):
    # try:
        if "search" in request.GET:
            posts = Post.objects.filter(title__contains=request.GET["search"])
        elif "category" in request.GET:
            posts = Post.objects.filter(category=request.GET["category"])
        else:
            posts = Post.objects.all()
        
        comments = Comment.objects.all().order_by("-created_at")[0:5]

        return render(request, 'blog/post_list.html', {'posts': posts, "comments":comments})
    # except Exception as e:
    #     return render(request, 'blog/error.html')

def post_detail(request, pk):
    # try:
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        return render(request, 'blog/post_detail.html', {'post': post, "comments":comments})
    # except Exception as e:
    #     return render(request, 'blog/error.html')

def post_create(request):
    try:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                if post.is_published:
                    post.published_at = timezone.now()
                post.save()
                return redirect(reverse('main:post_detail', kwargs={'pk': post.pk}))
        else:
            form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})
    except Exception as e:
        return render(request, 'blog/error.html')

def post_update(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            action = request.POST.get('action')

            if form.is_valid():
                post = form.save(commit=False)
                if post.is_published:
                    post.published_at = timezone.now()
                
                if action == 'edit':
                    post.save()
                    return redirect('main:post_detail', pk=post.pk)
                elif action == 'delete':
                    post.delete()
                    return redirect('main:post_list')

                post.save()
                return redirect('main:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)

        return render(request, 'blog/post_update.html', {'form': form, 'post': post})
    except Exception as e:
        return render(request, 'blog/error.html')

def add_comment(request, pk):
    post_=get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment=Comment(post=post_,text=request.POST["text"])
        comment.save()
    return  redirect(reverse('main:post_detail', kwargs={'pk': pk}))