from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from women.models import *

menu = [{'title': 'About site', 'url_name': 'women:about'},
        {'title': 'Add article', 'url_name': 'women:add_page'},
        {'title': 'Feedback', 'url_name': 'women:contact'},
        {'title': 'Log in', 'url_name': 'women:login'}]

def index(request):
    posts = Women.get_all_women()
    cats = Category.get_all_categories()
    context =  {'title': 'Main page',
                'posts': posts,
                'menu': menu,
                'cats': cats,
                'cat_selected': 0}



    return render(request, 'women/index.html',context = context)

def about(request):
    context = {'title': 'About', 'menu': menu}
    return render(request, 'women/about.html',context=context)

def categories(request:HttpRequest ,cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Page about categories {cat}')

def addpage(request): pass
def contact(request): pass
def login(request): pass

def show_post(request,post_id):
    woman = Women.get_by_id(post_id)
    return HttpResponse(woman)

def show_category(request,category_id):
    posts = Women.objects.filter(cat=category_id)

    if(len(posts) == 0): raise Http404()

    cats = Category.get_all_categories()
    context = {'title': 'Main page',
               'posts': posts,
               'menu': menu,
               'cats': cats,
               'cat_selected': Category.get_by_id(category_id)}

    return render(request, 'women/index.html', context=context)

def pageNotFound(request,exception):
    return HttpResponseNotFound('LOL PAGE NOT FOUND')