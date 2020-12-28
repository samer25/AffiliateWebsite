from django.urls import path

from forum_app.views import forum, RegisterUser, LoginUser, logout_user, ProfileView, EditProfile, DeleteProfile

urlpatterns = [
    path('', forum, name='forum'),
    path('register/', RegisterUser.as_view(), name='user register'),
    path('login/', LoginUser.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>', EditProfile.as_view(), name='edit profile'),
    path('delete_profile/<int:pk>', DeleteProfile.as_view(), name='delete profile'),

]
