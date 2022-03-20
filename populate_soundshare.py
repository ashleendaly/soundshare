import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soundshare_project.settings')

import django
django.setup()
from soundshare.models import User, UserProfile, Song


def populate():
    creators = [
        {'username_text': 'machinegunkelly',
         'email_text': 'mgk@gmail.com',
         'password_text': 'emosongs11',
         'firstname_text': 'Colson',
         'lastname_text': 'Baker',
         'type': 'Creator'},
        {'username_text': 'beartooth',
         'email_text': 'beartooth@basement.com',
         'password_text': 'angrysongs22',
         'firstname_text': 'Caleb',
         'lastname_text': 'Shomo',
         'type': 'Creator'}]

    listeners = [
        {'username_text': 'sean88',
         'email_text': 'sean@yahoo.com',
         'password_text': 'ilovemusic',
         'firstname_text': 'Sean',
         'lastname_text': 'McCulloch'},
        {'username_text': 'kelly',
         'email_text': 'kelly11@outlook.co.uk',
         'password_text': '1dforever',
         'firstname_text': 'Kelly',
         'lastname_text': 'McCulloch'}]

    producers = [
        {'username_text': 'bigman99',
         'email_text': 'thomas@recordlabela.com',
         'password_text': 'ilovebear',
         'firstname_text': 'Thomas',
         'lastname_text': 'Cripple',
         'type': 'Producer'},
        {'username_text': 'weeman11',
         'email_text': 'steve@recordlabelb.co.uk',
         'password_text': 'thegreatreset',
         'firstname_text': 'Steve',
         'lastname_text': 'Simpson',
         'type': 'Producer'}]

    songs = [
        {'likes': 222,
         'views': 100000,
         'creator': 0,
         'average_rating': 4.5,
         'album_title': '',
         'link': 'https://www.youtube.com/embed/2JyW4yAyTl0',
         'title': 'emo girl'},
        {'likes': 6,
         'views': 234,
         'creator': 1,
         'average_rating': 3.5,
         'album_title': '',
         'link': 'https://www.youtube.com/embed/2JyW4yAyTl0',
         'title': 'In Between'}
    ]

    # for c in creators:
    #     add_user(c['username_text'],c['email_text'], c['password_text'], c['firstname_text'], c['lastname_text'], c['type'])
    #
    # for l in listeners:
    #     add_user(l['username_text'], l['email_text'], l['password_text'], l['firstname_text'], l['lastname_text'])
    #
    # for p in producers:
    #     add_user(p['username_text'],p['email_text'], p['password_text'], p['firstname_text'], p['lastname_text'], p['type'])

    for s in songs:
        add_song(views=s['views'], likes=s['likes'], creator=s['creator'], average_rating=s['average_rating'],
                 album_title=s['album_title'], title=s['title'], link=s['link'])


def add_user(username, email, password, firstname, lastname, type='Listener'):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    u.save()

    # user = User.objects.get(username=username)
    # print(user)
    # p = UserProfile.objects.get_or_create(user=user, firstname_text=firstname, lastname_text=lastname, type=type)[0]
    # p.save()
    return u


def add_song(likes, views, creator, average_rating, album_title, link, title):
    # s = Song.objects.get_or_create(likes=likes, views=views, creator=creator, average_rating=average_rating,
    #                                album_title=album_title, link=link, title=title)[0]
    s = Song.objects.get_or_create(likes=likes, views=views, average_rating=average_rating,
                                   album_title=album_title, link=link, title=title)[0]
    # s = Song.objects.get_or_create(title=title)[0]
    # s.link = link
    s.save()
    return s


if __name__ == '__main__':
    print('Starting SoundShare population script...')
    populate()
