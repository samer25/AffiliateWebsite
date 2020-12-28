from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView

from forum_app.forms import RegisterUserForm, ProfileUserForm, LoginUserForm
from forum_app.models import ProfileUser


def forum(request):
    return render(request, 'forum.html')


class RegisterUser(CreateView):
    """
    Creating user and profile
    """

    # get method to view user and profile fields
    def get(self, request, *args, **kwargs):
        user_form = RegisterUserForm()
        profile_form = ProfileUserForm()
        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })

    # post method to verified fields if they are correctly if it is register the user with profile
    def post(self, request, *args, **kwargs):
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileUserForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, 'Successfully Registered')

            return redirect('forum')
        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })


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
    """Getting selected Profile of the user and his posts"""

    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])

        return render(request, 'profile.html',
                      {'pk': request.user.id, 'user_profile': user})


class EditProfile(UpdateView):
    """Editing the profile user"""

    # get method to view current profile data in the forms fields to change it
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = ProfileUser.objects.get(pk=user.profile.pk)
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


class DeleteProfile(DeleteView):
    """Deleting user and all user content"""

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
