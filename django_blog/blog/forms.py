from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget  # ✅ Import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # ✅ Use TagWidget for proper tag handling
        }

    def clean_tags(self):
        return [tag.strip() for tag in self.cleaned_data['tags'].split(',')]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
