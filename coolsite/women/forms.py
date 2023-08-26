from django import forms
from django.core.exceptions import ValidationError

from women.models import *

## Unrelated forms with model this we just duplicate fields from Women
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,
#                             label='Top title',
#                             widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label='URL')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     is_published = forms.BooleanField(label='published?',
#                                       initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                  label='Category',
#                                  empty_label='Category is not chosen')

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category is not chosen'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length exceed 200 symbols')

        return title

    def clean_slug(self):
        title: str = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Title has not been shown')
        slug = title.lower().replace(' ','-')


        return slug



    class Meta:
        model = Women
        exclude = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols':60, 'rows': 10})
        }