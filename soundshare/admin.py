from django.contrib import admin
from soundshare.models import UserProfile, Song, Album, Feedback

admin.site.register(UserProfile)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Feedback)
