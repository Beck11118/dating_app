from django.shortcuts import render, redirect
from .models import UserProfile, Match, Message
from django.contrib.auth.decorators import login_required
from .forms import MessageForm, UserProfileForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def index(request):
    return  render(request, 'index.html')


@login_required
def profile_edit(request):
    """Edit user profile."""
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_view', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile_edit.html', {'form': form})



def profile_view(request, username=None):
    # If username is not provided in the URL, use the logged-in user's username
    if username is None and request.user.is_authenticated:
        username = request.user.username

    # Retrieve the user object based on the username
    user = get_object_or_404(User, username=username)
    
    return render(request, 'profile/profile.html', {'user': user})


@login_required
def match_view(request):
    user_profile = request.user.userprofile
    matches = Match.objects.filter(user1=user_profile)
    return render(request, 'matches/match_list.html', {'matches': matches})


@login_required
def message_view(request, receiver_username):
    sender_profile = request.user.userprofile
    receiver_profile = UserProfile.objects.get(user__username=receiver_username)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(sender=sender_profile, receiver=receiver_profile, content=content)
            return redirect('message_success')  # Redirect to a success page
    else:
        form = MessageForm()

    return render(request, 'messages/message_form.html', {'form': form, 'receiver_profile': receiver_profile})



