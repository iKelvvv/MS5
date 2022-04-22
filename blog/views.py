from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def blog(request):

    all_posts = Post.objects.filter(status=1).order_by("-created_on")

    context = {
        'posts': all_posts
    }

    return render(request, 'blog/blogs.html', context)
