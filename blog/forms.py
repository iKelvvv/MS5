from django import forms
from products.widgets import CustomClearableFileInput
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
