from django import forms

from forum_app.models import Forum

"""creating class form for comments and forum that user can create a question and with comment the another users can 
answer that question """


class CommentForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'desc']
