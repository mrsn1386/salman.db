from django import forms
from django.utils.translation.template import context_re
from select import select

from posts.models import Post, PostCategory, File


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']