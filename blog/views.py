from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all()
    string = ' , '.join([post.title for post in posts])
    blog = '<html><head><title>ali komijani</title></head><body><h1>{}</h1></body></html>'.format(
        string)
    return HttpResponse(blog)


def single(request, pk):
    try:
        post = Post.objects.get(slug=pk)
    except Post.DoesNotExist:
        raise Http404('post not found')
    link = reverse('posts_archive')
    blog = '<html><head><title>ali komijani</title></head><body><h1>{}</h1><p>{}<p> <a href="{}">posts</a></body></html>'.format(
        post.title,
        post.content, link)
    return HttpResponse(blog)
