from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from women.models import *


def index(request):
    posts = Women.get_all_women()
    context =  {'title': 'Main page',
                'posts': posts,
                'cat_selected': 0}



    return render(request, 'women/index.html',context = context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'women/about.html',context=context)

def categories(request:HttpRequest ,cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Page about categories {cat}')

def addpage(request): pass
def contact(request): pass
def login(request): pass

def show_post(request,post_slug):
    post = get_object_or_404(Women,slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'women/post.html', context=context)

def show_category(request,category_slug):
    posts = Women.objects.filter(cat__slug=category_slug)
    # cat = get_object_or_404(Category,slug=category_slug)
    # posts = Women.objects.filter(cat=cat.pk)



    if len(posts) == 0: raise Http404

    cats = Category.get_all_categories()
    context = {'title': 'Main page',
               'posts': posts,
               'cat_selected': posts[0].slug}

    return render(request, 'women/index.html', context=context)

def pageNotFound(request,exception):
    return HttpResponseNotFound('LOL PAGE NOT FOUND')