from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from forum_app.forms import CommentForm
from forum_app.models import Forum, Comment

"""Creating Forum view that have CRUD it and for comment also """


class ForumListView(ListView):
    """Forum list to display all questions that users created with paginate
     have html file that users can go next page or previous page and  is separated and included in forum.html"""
    model = Forum
    queryset = Forum.objects.order_by('-created_at')
    paginate_by = 4
    template_name = 'forums/forum.html'
    context_object_name = 'forum'


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumDetailView(DetailView):
    """Forum detail class base view that the user can check a question detail and in it can reed the answers is
    required to have registration and to be logged in to assess the page"""
    model = Forum
    template_name = 'forums/forum_detail.html'
    context_object_name = 'forum'

    def get_context_data(self, **kwargs):
        """adding Comment form to context that can pass form to forum_details.html"""
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

    def get_object(self):
        """getting user that is in specific forum details (self.object) and adding it to view_count that can count
        views ot that question"""
        obj = super().get_object()
        user = self.request.user
        obj.views_count.add(user)
        obj.save()
        return obj


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumDeleteView(DeleteView):
    """question  Delete"""
    """Deleting the question with all connected models : comments model """

    def post(self, request, *args, **kwargs):
        """taking id of forum  that we know what question is delete """
        question = Forum.objects.get(pk=kwargs['pk'])
        question.delete()
        messages.success(request, 'Successfully Deleted The Question')

        return redirect('forum')


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumUpdateView(UpdateView):
    model = Forum
    fields = ['title', 'desc']
    template_name = 'forums/forum_update_form.html'

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Successfully Edited The Question')

        return reverse_lazy('forum-detail', kwargs={'slug': self.object.slug})


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumCreate(CreateView):
    """Creating Forum class base view"""
    model = Forum
    fields = ['title', 'desc']
    context_object_name = 'form'
    template_name = 'forums/forum_create.html'

    def form_valid(self, forms):
        """checking if the form is valid and if it is save it"""
        forms.instance.user = self.request.user
        messages.success(self.request, 'Successfully Created The Question')

        return super().form_valid(forms)


@method_decorator(login_required(login_url='login user'), name='dispatch')
class CommentCreateView(CreateView):
    """class base view for creating a comment to specific question """
    model = Comment
    fields = ['desc']
    success_message = 'Comment was successfully created'

    def form_valid(self, form):
        """checking if the form is valid and taking forum id to assign user to it
        that can know how comment and in what question hi answered"""
        _forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.forum = _forum
        return super().form_valid(form)


@method_decorator(login_required(login_url='login user'), name='dispatch')
class CommentDeleteView(DeleteView):
    """Comment Delete have to me logged in"""
    """Deleting the comment """

    def post(self, request, *args, **kwargs):
        """taking the id for comment to know what comment what to delete the user. the comment have to be created by
        the user how whats to delete it """
        comm = Comment.objects.get(pk=kwargs['pk'])
        comm.delete()
        messages.success(request, 'Successfully Deleted The Comment')

        return redirect('forum-detail', comm.forum.slug)


@method_decorator(login_required(login_url='login user'), name='dispatch')
class CommentUpdateView(UpdateView):
    """ class base view for editing  the comments  that  user can edit it if he created it """
    model = Comment
    fields = ['desc']
    template_name = 'forums/forum_update_comment.html'
    context_object_name = 'form'


@login_required(login_url='login user')
def like_comment(request, pk):
    """like function view for user can add like to comment by taking id comment and user id to know how is comment
    what comment """
    comment = Comment.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    comment.likes.add(user)
    comment.save()

    return redirect('forum-detail', comment.forum.slug)


@login_required(login_url='login user')
def dislike_comment(request, pk):
    """Dislike function view for user can add dislike to comment by taking id comment and user id to know how is comment
        what comment """
    comment = Comment.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    comment.dislikes.add(user)
    comment.save()

    return redirect('forum-detail', comment.forum.slug)
