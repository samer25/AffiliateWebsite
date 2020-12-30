from django.urls import path

from users.views import RegisterUser, LoginUser, logout_user, ProfileView, EditProfile, DeleteProfile, \
    activate, change_password, password_reset_request
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='user register'),
    path('login/', LoginUser.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>', EditProfile.as_view(), name='edit profile'),
    path('password_change/', change_password, name='change-password'),
    path('delete_profile/<int:pk>', DeleteProfile.as_view(), name='delete profile'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),
         name='password_reset_complete'),
]
