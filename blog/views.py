from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def blog(request):
    """ A view to see all published blog posts """
    all_posts = Post.objects.filter(status=1).order_by("-created_on")

    context = {
        'posts': all_posts
    }

    return render(request, 'blog/blogs.html', context)



def post_detail(request, post):
    """ A view to see a single blog post """

    post = get_object_or_404(Post, slug=post)

    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)
