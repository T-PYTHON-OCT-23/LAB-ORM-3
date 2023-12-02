from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def post_list(request):
    try:
        if "search" in request.GET:
            posts = Post.objects.filter(title__contains=request.GET["search"])
        elif "category" in request.GET:
            posts = Post.objects.filter(category=request.GET["category"])
        else:
            posts = Post.objects.all()
        
        comments = Comment.objects.all().order_by("-created_at")[0:5]

        return render(request, 'blog/post_list.html', {'posts': posts, "comments":comments})
    except Exception as e:
        return render(request, 'blog/error.html')

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


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:post_list')  # Redirect to your desired page
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('main:user_login')  # Redirect to your desired page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('main:post_list')  # Redirect to your desired page after logout