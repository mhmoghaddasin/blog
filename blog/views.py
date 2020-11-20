from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Post, Category


# Create your views here.

def home(request):
    posts = Post.objects.all()
    links = ''.join(
        '<li><a href={}>{}</a></li>'.format(reverse('post_single', kwargs={'pk': post.slug}), post.title) for post in
        posts)
    blog = '<html><head><title>post archive</title></head><ul>{}</ul></body></html>'.format(links)
    return HttpResponse(blog)


def single(request, pk):
    try:
        post = Post.objects.get(slug=pk)
    except Post.DoesNotExist:
        raise Http404('post not found')
    link = reverse('posts_archive')
    post_details = '<h1>{}</h1>'.format(post.title)
    post_details += '<h5><a href={}>{}</a></h5>'.format(reverse('category_single', args=[post.category.slug]),
                                                        post.category.title)

    post_details += '<p>{}</p>'.format(post.content)
    blog = '<html><head><title>ali komijani</title></head>' \
           '<body>{}<a href="{}">posts</a></body></html>'.format(
        post_details, link)
    return HttpResponse(blog)


def category_single(request, pk):
    try:
        category = Category.objects.get(slug=pk)
    except Category.DoesNotExist:
        raise Http404('Category not found')
    posts = Post.objects.filter(category=category)
    links = ''.join(
        '<li><a href={}>{}</a></li>'.format(reverse('post_single', args=[post.slug]), post.title) for post in posts)
    blog = '<html><head><title>post archive</title></head>{}<a href={}>all categories</a></body></html>'.format(
        '<ul>{}</ul>'.format(links), reverse('categories_archive'))
    return HttpResponse(blog)


def categories_archive(request):
    categories = Category.objects.all()
    links = ''.join(
        '<li><a href={}>{}</a></li>'.format(reverse('category_single', args=[category.slug]), category.title) for
        category in categories)
    blog = '<html><head><title>post archive</title></head>{}</body></html>'.format(
        '<ul>{}</ul>'.format(links))
    return HttpResponse(blog)
