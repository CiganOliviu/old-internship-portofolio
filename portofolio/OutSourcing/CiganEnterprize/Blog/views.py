from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q

from .models import Post

def blog_posts_search_view(request):

    template_name = 'blog/blog_posts_results.html'

    query = request.GET.get('q')

    if query:
        results = Post.objects.filter(Q(title__icontains = query))
    else:
        return redirect('/blog')

    context = {

        'results' : results,
    }

    return render(request, template_name, context)

class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')

    template_name = 'blog/blog.html'

class PostDetail(generic.DetailView):

    model = Post

    template_name = 'blog/blog_details.html'
