import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soundshare_project.settings')

import django
django.setup()
from soundshare.models import UserProfile, Song, Feedback, Comment, Album


def populate():

    def add_user(firstname, lastname, type="Listener"):
        u = UserProfile.objects.get_or_create(firstname=firstname, lastname=lastname, type=type)
        u.save()
        return u

    def add_song(likes, views, creator, average_rating, album_title, link, title):
        s = Song.objects.get_or_create(likes=likes, views=views,creator=creator, average_rating=average_rating,album_title=album_title,title=title)
        s.link = link
        s.save()
        return s

    def add_feedback(rating, user, comment, song):
        f = Feedback.objects.get_or_create(rating=rating, user=user, comment=comment, song=song)
        f.save()
        return f

    def add_comment(user, song, content, comment_time):
        c = Comment.objects.get_or_create(user=user, song=song, content=content, comment_time=comment_time)
        return c

    add_user('Colson', 'Baker', 'Creator')
    add_user('Caleb', 'Shomo', 'Creator')
    add_user('Sean', 'McCulloch')
    add_user('Kelly', 'McCulloch')
    add_user('Thomas', 'Cripple', 'Producer')
    add_user('Steve', 'Simpson', 'Producer')

    add_song(222, 10000, 'Colson', 4.5, '', 'https://www.youtube.com/watch?v=vzuY0O1L0b0', 'emo girl')
    add_song(234, 12000, 'Caleb', 3, '', 'https://www.youtube.com/watch?v=j2p_w409y-o', 'In Between')

    add_feedback(2, 'Sean','It was ok', 'emo girl')
    add_feedback(4, 'Kelly', 'I loved it', 'emo girl')

    add_comment('Sean', 'emo girl', 'It was ok', '10:33')
    add_comment('Kelly', 'emo girl', 'I loved it', '11:33')


if __name__ == '__main__':
    print('Starting SoundShare population script...')
    populate()