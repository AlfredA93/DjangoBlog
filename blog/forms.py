"libs"
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    "Comments"
    class Meta:
        "data model"
        model = Comment
        fields = ('body',)
