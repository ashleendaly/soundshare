from django import forms
from soundshare.models import UserProfile, Song
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname', 'type', 'image', )


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'link', 'musician_name', 'album_title', )


class SearchForm(forms.ModelForm):
    search_music_musician = forms.CharField()

    class Meta:
        model = Song
        fields = ('title', 'musician_name', )

