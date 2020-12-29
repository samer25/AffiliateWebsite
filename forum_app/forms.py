from django import forms

from forum_app.models import Forum


class CommentForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'desc']
