import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'soundshare_project.settings')

import django
django.setup()
from soundshare.models import UserProfile, Song


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
         'average_rating': 4.5,
         'link': 'https://www.youtube.com/watch?v=vzuY0O1L0b0',
         'title': 'emo girl'},
        {'likes': 6,
         'views': 234,
         'average_rating': 3.5,
         'link': 'https://www.youtube.com/watch?v=j2p_w409y-o',
         'title': 'In Between'}
    ]

    for c in creators:
        add_user(c['username_text'],c['email_text'], c['password_text'], c['firstname_text'], c['lastname_text'],
                 c['type'])

    for l in listeners:
        add_user(l['username_text'], l['email_text'], l['password_text'], l['firstname_text'], l['lastname_text'])

    for p in producers:
        add_user(p['username_text'],p['email_text'], p['password_text'], p['firstname_text'], p['lastname_text'],
                 p['type'])


def add_user(username, email, password, firstname, lastname, type='Listener'):
    p = UserProfile.objects.get_or_create(username_text=username, email_text=email, password_text=password,
                                          firstname_text=firstname, lastname_text=lastname, type=type)[0]
    p.save()
    return p


def add_song(title, link):
    s = Song.objects.get_or_create(title=title)[0]
    s.link = link
    s.save()
    return s


if __name__ == '__main__':
    print('Starting SoundShare population script...')
    populate()
