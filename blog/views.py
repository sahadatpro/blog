from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView


"""
functional views
"""
def index(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer delivery the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range delivery last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'page' : page,
        'posts': posts
    }
    return render(request, 'blog/list.html', context)

"""
class base views
"""
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = 'blog/list.html'

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status = 'published', publish__year=year, publish__month=month, publish__day=day)
   
    context = {
        'post' : post
    }
    return render(request, 'blog/details.html', context)