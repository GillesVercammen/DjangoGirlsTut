from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # QuerySet
    # Example:   Post.objects.all()
    #           User.objects.get(username='ola')
    #           Post.objects.filter(title__contains='title')
    #           Post.objects.order_by('-created_date')
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})