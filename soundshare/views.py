from django.shortcuts import render, redirect
from django.http import HttpResponse
from soundshare.models import UserProfile, Song
from soundshare.forms import UserForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {}
    try:
        all_music = Song.objects.all()
        context_dict = {'all_music': all_music}
        return render(request, 'soundshare/index.html', context=context_dict)
    except Song.DoesNotExist:
        print("No song exists!")
        return render(request, 'soundshare/index.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse('The soundshare account ' + username + 'is disabled!')
        else:
            print(f'Invalid login details: username: {username}, password: {password}')
            return HttpResponse('Invalid login details supplied! ' +
                                'username: ' + username + ' password ' + password)
    else:
        context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
        return render(request, 'soundshare/login.html', context=context_dict)


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect(reverse('login'))
        else:
            print(f'Invalid signup details: user fomr error: {user_form.errors}, profile form error: {profile_form.errors}')
            return HttpResponse('Invalid signup details supplied! '
                                'Invalid signup details: user fomr error: '+ str(user_form.errors) +
                                ', profile form error: ' + str(profile_form.errors))
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
        return render(request, 'soundshare/signup.html', context=context_dict)


def music(request, music_title):
    context_dict = {}
    try:
        music_info = Song.objects.get(title=music_title)
        context_dict = {'music_info': music_info}
        return render(request, 'soundshare/music.html', context=context_dict)
    except Song.DoesNotExist:
        print("The song is not exist!")
        return render(request, 'soundshare/music.html', context=context_dict)



def upload(request):
    context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
    return render(request, 'soundshare/upload.html', context=context_dict)

