from django.contrib import admin
from women.models import *

class WomenAdmin(admin.ModelAdmin):

    list_display = ('id','title','cat','is_published')
    list_display_links = ('id','title')
    list_editable = ('is_published',)

admin.site.register(Women,WomenAdmin)
admin.site.register(Category)