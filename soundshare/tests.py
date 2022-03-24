from django.test import TestCase
from django.urls import reverse
from django.db import models

from soundshare.models import Song, Album

class YourTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(self):
        #Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)

class CategoryViewTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.url = '/soundshare/index/'
        self.url2 = '/soundshare/index/'

# To see if the whole codes are working okay #
class SillyTestCase(TestCase):
    def test_smoke(self):
        self.assertEqual(1 + 1, 2)

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        # If no categories exist, the appropriate message should be displayed. #
        response = self.client.get('/soundshare/index/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['song'],[])

# check the index view when songs are present #
def add_category(name, views=0, likes=0):
    song = Song.objects.get_or_create(name=name)[0]
    song.views = views
    song.likes = likes
    song.save()
    return song


# check the index view when albums are present #
def add_category(name, views=0, likes=0):
    album = Album.objects.get_or_create(name=name)[0]
    album.views = views
    album.likes = likes
    album.save()
    return album

# test if the user is not logged in #
def test_redirect_if_not_logged_in(self):
    response = self.client.get('/soundshare/index/')
    # check redirect #
    self.assertEqual(response.status_code, 302)
    self.assertTrue(response.url.startswith('/soundshare/login/'))


# Accessing a non-existing category ,expecting a 404 response code #
    def test_visit_a_nonexistent_category(self):
        url = '/soundshare/index/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

# If there is no article classification, returns 200. but it indicates that there are nothing published yet! #
# The rendered template is index.html #
    def test_without_any_post(self):
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/soundshare/index/')
        self.assertContains(response, 'Nothing published for now!')

# Test if the view number is added when it is viewed #
    def test_good_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
        self.assertContains(response, self.md_post.title)
        self.assertIn('post', response.context)

