from django.test import TestCase
from django.urls import reverse
from django.db import models
from soundshare.models import Song, Album


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """If no categories exist, the appropriate message should be displayed."""
        response = self.client.get(reverse('soundshare:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['song'],[])

"""check the index view when songs are present"""
def add_category(name, views=0, likes=0):
    song = Song.objects.get_or_create(name=name)[0]
    song.views = views
    song.likes = likes
    song.save()
    return song


"""check the index view when albums are present"""
def add_category(name, views=0, likes=0):
    album = Album.objects.get_or_create(name=name)[0]
    album.views = views
    album.likes = likes
    album.save()
    return album

