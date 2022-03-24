from django.shortcuts import render, redirect
from django.http import HttpResponse
from soundshare.models import User, UserProfile, Song, Album, Feedback
from soundshare.forms import UserForm, UserProfileForm, SongForm, SearchForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {}
    try:
        most_views_music = Song.objects.order_by('-views')[:8]
        most_likes_music = Song.objects.order_by('-likes')[:8]
        all_creators = UserProfile.objects.filter(type="Creator")
        context_dict = {'most_views_music': most_views_music, "most_likes_music": most_likes_music, "all_creators": all_creators}
        return render(request, 'soundshare/index.html', context=context_dict)
    except Song.DoesNotExist:
        print("No song exists!")
        return render(request, 'soundshare/index.html', context=context_dict)


def add_like(request, music_title):
    context_dict = {}
    if request.method == 'POST':
        music_info = Song.objects.get(title=music_title)
        music_info.likes += 1
        music_info.save()
        context_dict = {'music_info': music_info}
        return render(request, 'soundshare/music.html', context=context_dict)
    else:
        return render(request, 'soundshare/music.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
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


def user_logout(request):
    logout(request)
    return render(request, 'soundshare/login.html')


def forget_password(request):
    return render(request, 'soundshare/login.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.image = profile_form.cleaned_data['image']
            profile.user = user
            profile.save()
            return redirect(reverse('login'))
        else:
            print(f'Invalid signup details: user form error: {user_form.errors}, profile form error: {profile_form.errors}')
            return HttpResponse('Invalid signup details supplied! '
                                'Invalid signup details: user form error: '+ str(user_form.errors) +
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


def music_all(request):
    context_dict = {}
    try:
        all_music = Song.objects.all()
        context_dict = {'all_music': all_music}
        return render(request, 'soundshare/music.html', context=context_dict)
    except Song.DoesNotExist:
        print("The song is not exist!")
        return render(request, 'soundshare/music.html', context=context_dict)


def music_search(request):
    context_dict = {}
    if request.method == 'POST':
        search_music_musician = request.POST.get('search_music_musician')
        print(f'search_music_musician is {search_music_musician}')
        try:
            all_music = Song.objects.all()
            selected_music = []
            for music in all_music:
                if music.title == search_music_musician or music.musician_name == search_music_musician:
                    selected_music.append(music)

            context_dict = {'selected_music': selected_music}
            return render(request, 'soundshare/music.html', context=context_dict)
        except Song.DoesNotExist:
            print("The song is not exist!")
            return render(request, 'soundshare/music.html', context=context_dict)

    context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
    return render(request, 'soundshare/music.html', context=context_dict)


def music_upload(request):
    if request.method == 'POST':
        song_form = SongForm(request.POST, request.FILES)
        if song_form.is_valid():
            song = song_form.save(commit=False)
            # song.creator = request.user
            song.save()
            return redirect(reverse('index'))
        else:
            print(f'Invalid signup details: song form error: {song_form.errors}')
            return HttpResponse('Invalid signup details supplied! Invalid signup details: user form error: '+ str(song_form.errors))
    else:
        song_form = SongForm()
        context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
        return render(request, 'soundshare/upload.html', context=context_dict)

