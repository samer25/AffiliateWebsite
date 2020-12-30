from django.urls import path

from forum_app.views import ForumListView, ForumDetailView, CommentCreateView, CommentDeleteView, ForumDeleteView, \
    CommentUpdateView, ForumUpdateView, ForumCreate, like_comment, dislike_comment

urlpatterns = [
    path('add/', ForumCreate.as_view(), name='forum-add'),
    path('like/<int:pk>', like_comment, name='like comment'),
    path('dislike/<int:pk>', dislike_comment, name='dislike comment'),
    path('', ForumListView.as_view(), name='forum'),
    path('<slug:slug>/', ForumDetailView.as_view(), name='forum-detail'),
    path('edit/<int:pk>', ForumUpdateView.as_view(), name='forum-edit'),
    path('delete-forum/<int:pk>', ForumDeleteView.as_view(), name='delete-forum'),
    path('add-comment/<int:pk>', CommentCreateView.as_view(), name='add-comment'),
    path('edit-comment/<int:pk>', CommentUpdateView.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>', CommentDeleteView.as_view(), name='delete-comment'),

]
