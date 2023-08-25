from django.contrib import admin
from women.models import *

TEXT_MAIN = 'In this section You might set up title and content fields'
TEXT_PHOTO = 'In this section You might set up photo field'
class WomenAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main section', {
            'fields': ('title', 'content','slug'),
            'description': f'{TEXT_MAIN}'
        }),
        ('Photo section', {
            'fields': ('photo',),
            'description': f'{TEXT_PHOTO}'

        }),
        ('Other section', {
            'fields': (('cat','is_published'),),
            'classes': ('collapse','wide '),
        })
    )
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Women,WomenAdmin)
admin.site.register(Category,CategoryAdmin)