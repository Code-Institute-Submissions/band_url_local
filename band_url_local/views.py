from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
#from payments.forms import MakePaymentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.conf import settings
from products.models import Product
import stripe
from .models import Post
from .forms import BlogPostForm
from django.utils import timezone



def get_index(request):
    return render(request, 'index.html')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                               ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


def get_merchandise(request):
    products = Product.objects.filter()
    return render(request, 'merchandise.html', {"products": products})





