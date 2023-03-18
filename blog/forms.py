from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """add placeholder text to comment section"""
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Add comment...'


class RecipeForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        """Form fields"""
        model = Post
        fields = [
            'title',
            'description',
            'preparation_time',
            'ingredients',
            'featured_image',
        ]
