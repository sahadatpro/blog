from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from blog.forms import CommentForm


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
        'page': page,
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
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)

    # List of active comments
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # Comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create comment object but don't save to database yet.
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            new_comment.save()  # save to database

    else:
        comment_form = CommentForm()

    return render(request, 'blog/details.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })
