import token

import django
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from django.db.models.query_utils import Q
from forum_app.models import Forum
from users.forms import RegisterUserForm, ProfileUserForm, LoginUserForm
from django.shortcuts import render, redirect

# Create your views here.
from users.models import ProfileUser
from users.token import account_activation_token


class RegisterUser(CreateView):
    """
    Creating user and profile and sending email activation
    """

    # get method to view user and profile fields
    def get(self, request, *args, **kwargs):
        """passing register form and profile form to register.html"""
        user_form = RegisterUserForm()
        profile_form = ProfileUserForm()
        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })

    """post method to verified fields if they are correctly if it is register the user with profile and send
     email for activation"""

    def post(self, request, *args, **kwargs):
        """getting post request to check if is valid the data"""
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileUserForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            """turning is_active of to be activated when the user click to link activation"""
            user.is_active = False
            user.save()
            profile.user = user
            profile.save()

            # Send email
            subject = "Activate your account from email"

            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            }
                                       )
            to_email = profile_form.cleaned_data.get('email')
            email = EmailMessage(
                subject, message, to=[to_email]
            )
            email.send()
            messages.success(request,
                             'Please confirm your email address to complete the registration')

            return redirect('forum')
        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })


def activate(request, uidb64, token):
    """activating the account of the user when clicked the link that is sent to him """
    uid = django.utils.http.urlsafe_base64_decode(uidb64)
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        """turning user is_active on """
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login user')


class LoginUser(FormView):
    """Log in the user"""

    # get method view login fields
    def get(self, request, *args, **kwargs):
        login_form = LoginUserForm()
        return render(request, 'login.html', {'form': login_form})

    # post method verified user if exist
    def post(self, request, *args, **kwargs):
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Successfully Logged in')
                return redirect('forum')
            else:
                error = 'user or password is not valid!'
                return render(request, 'login.html', {'form': login_form, 'error': error})
        return render(request, 'login.html', {'form': login_form})


# logging out the user
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('index')


class ProfileView(DetailView):
    """Getting selected Profile of the user and all his Question"""

    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        forum = Forum.objects.filter(user=kwargs['pk'])

        return render(request, 'profile.html',
                      {'pk': request.user.id, 'user_profile': user, 'forum': forum})


class EditProfile(UpdateView):
    """Editing the profile user"""

    # get method to view current profile data in the forms fields to change it
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = ProfileUser.objects.get(pk=request.user.id)
        form = ProfileUserForm(instance=profile)
        return render(request, 'common/edit.html', {'form': form})

    # post method to verified edited profile form field and save it
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = ProfileUser.objects.get(pk=user.profile.pk)
        form = ProfileUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            messages.success(request, 'Successfully Edited Your Profile')

            form.save()
            return redirect('profile', kwargs['pk'])


def change_password(request):
    """crating view function for changing password of user"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('forum')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password/change_password.html', {'form': form})


def password_reset_request(request):
    """crating password reset view function when the user forget the password by sending him email with link for
    pass reset """
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(profile__email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    message = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, message)

                    try:
                        send_mail(subject, email, 'admin@example.com', [user.profile.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("forum")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


class DeleteProfile(DeleteView):
    """Deleting user and all user desc_min"""

    # get method tho view html page delete
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        return render(request, 'delete_profile.html')

    # post method to delete user
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        user.delete()
        messages.success(request, 'Successfully Deleted Your Profile')

        return redirect('index')
