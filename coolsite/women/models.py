from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='_title_')
    slug = models.SlugField(max_length=255,unique=True,verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Lol:
        ordering = ['title']
    class Meta:
        verbose_name = 'Famous woman'
        verbose_name_plural = 'Famous women'
        ordering = ['-pk']

    def __str__(self):
        return f'{self.pk} -> {self.title}'


    @classmethod
    def get_all_women(cls):
        return list(Women.objects.all())

    @classmethod
    def get_by_id(cls,id):
        try:
            woman = Women.objects.get(pk=id);
        except:
            woman = None

        return woman

    def get_absolute_url(self):
        return reverse('women:post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='category')
    slug = models.SlugField(max_length=255,unique=True,verbose_name='URL')

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.name
    @classmethod
    def get_all_categories(cls):
        return list(Category.objects.all())

    @classmethod
    def get_by_id(cls,id):
        try:
            cat = Category.objects.get(pk=id)
        except:
            cat = None

        return cat
    def get_absolute_url(self):
        return reverse('women:category', kwargs={'category_slug':self.slug})


