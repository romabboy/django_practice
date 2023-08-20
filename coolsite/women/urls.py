from django.urls import path, re_path
from women.views import *

app_name = 'women'

urlpatterns = [
    path('',index),
    path('cats/<slug:cat>/', categories,name='home'),
    re_path(r'^archive/(?P<year>\d{4})/',archive)

]
