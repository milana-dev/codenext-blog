from django.forms import forms

from blogs.models import Blog


class BlogFrom(forms.Form):
    class Meta:
        model = Blog
        fields = '__all__'


