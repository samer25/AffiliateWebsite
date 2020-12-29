from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from forum_app.forms import CommentForm, ForumForm
from forum_app.models import Forum, Comment


def forum(request):
    return render(request, 'forums/forum.html')


class ForumListView(ListView):
    model = Forum
    queryset = Forum.objects.order_by('-created_at')
    paginate_by = 2
    template_name = 'forums/forum.html'
    context_object_name = 'forum'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ForumForm()
    #     return context


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forums/forum_detail.html'
    context_object_name = 'forum'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        obj.views_count.add(user)
        obj.save()
        return obj


@method_decorator(login_required(login_url='login user'), name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    fields = ['desc']
    success_message = 'Forum was successfully created'

    def form_valid(self, form):
        _forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.forum = _forum
        return super().form_valid(form)


@method_decorator(login_required(login_url='login user'), name='dispatch')
class CommentDeleteView(DeleteView):
    """Post Delete"""
    """Deleting the post with all connected models : comments model """

    def post(self, request, *args, **kwargs):
        comm = Comment.objects.get(pk=kwargs['pk'])
        comm.delete()
        messages.success(request, 'Successfully Deleted The Comment')

        return redirect('forum-detail', comm.forum.slug)


@method_decorator(login_required(login_url='login user'), name='dispatch')
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['desc']
    template_name = 'forums/forum_update_comment.html'
    context_object_name = 'form'


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumDeleteView(DeleteView):
    """Post Delete"""
    """Deleting the post with all connected models : comments model """

    def post(self, request, *args, **kwargs):
        question = Forum.objects.get(pk=kwargs['pk'])
        question.delete()
        messages.success(request, 'Successfully Deleted The Form')

        return redirect('forum')


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumUpdateView(UpdateView):
    model = Forum
    fields = ['title', 'desc']
    template_name = 'forums/forum_update_form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('forum-detail', kwargs={'slug': self.object.slug})


@method_decorator(login_required(login_url='login user'), name='dispatch')
class ForumCreate(CreateView):
    model = Forum
    fields = ['title', 'desc']
    context_object_name = 'form'
    template_name = 'forums/forum_create.html'

    def form_valid(self, forms):
        forms.instance.user = self.request.user
        return super().form_valid(forms)


@method_decorator(login_required(login_url='login user'), name='dispatch')
def like_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    comment.likes.add(user)
    comment.save()

    return redirect('forum')


@method_decorator(login_required(login_url='login user'), name='dispatch')
def dislike_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    comment.dislikes.add(user)
    comment.save()

    return redirect('forum')

# @method_decorator(login_required, name='dispatch')
# class ForumCreate(CreateView):
#     """User Creating posts view that required to be login using method_decorator"""
#
#     # get method viewing forms for creating posts
#     @method_decorator(login_required(login_url='login user'))
#     def get(self, request, *args, **kwargs):
#         form = ForumForm()
#         return render(request, 'forums/forum_create.html', {'form': form})
#
#     # post method verified forms fields if they valid if they are save it
#     @method_decorator(login_required(login_url='login user'))
#     def post(self, request, *args, **kwargs):
#         user = User.objects.get(pk=request.user.pk)
#         form = ForumForm(request.POST, request.FILES)
#         if form.is_valid():
#             forms = form.save(commit=False)
#             forms.created_by = user
#             forms.save()
#             messages.success(request, 'Successfully Created Post')
#
#             return redirect('forum')
#         return render(request, 'forums/forum_create.html', {'form': form})
