from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('Page app women')

def categories(request:HttpRequest ,cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Page about categories {cat}')

def archive(request,year):
    if int(year) < 2000 or int(year) > 2099:
        return redirect('women:home', permanent=True )

    return HttpResponse(f'Page about archive {year}')

def pageNotFound(request,exception):
    return HttpResponseNotFound('LOL PAGE NOT FOUND')