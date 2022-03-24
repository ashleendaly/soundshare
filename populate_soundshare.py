import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soundshare_project.settings')

import django
django.setup()
from soundshare.models import User, UserProfile, Song, Feedback, Comment, Album


def populate():

    def add_user(firstname, lastname, image, type="Listener"):
        u = User.objects.get_or_create(username=firstname+lastname, password="abc@123")
        u.save()
        up = UserProfile.objects.get_or_create(firstname=firstname, lastname=lastname, image=image, type=type)
        up.user = u
        up.save()
        return u

    def add_song(likes, views, creator, average_rating, musician_name, album_title, link, title, image):
        s = Song.objects.get_or_create(likes=likes, views=views, average_rating=average_rating,
                                       musician_name=musician_name, album_title=album_title,title=title, image=image)
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

    # add_user('Colson', 'Baker', '/static/image/user_photo_default.png', 'Creator')
    # add_user('Caleb', 'Shomo', '/static/image/user_photo_default.png', 'Creator')
    # add_user('Sean', 'McCulloch', '/static/image/user_photo_default.png',)
    # add_user('Kelly', 'McCulloch', '/static/image/user_photo_default.png',)
    # add_user('Thomas', 'Cripple','/static/image/user_photo_default.png', 'Producer')
    # add_user('Steve', 'Simpson', '/static/image/user_photo_default.png', 'Producer')

    add_song(222, 10000, 0, 4.5, '', 'Colson', 'https://www.youtube.com/embed/2JyW4yAyTl0', 'emo girl', '/static/image/song_photo_default.png')
    add_song(234, 12000, 1, 3, '', 'Caleb', 'https://www.youtube.com/embed/tgbNymZ7vqY', 'In Between', '/static/image/song_photo_default.png')
    add_song(234, 12000, 2, 3, '', 'Caleb', 'https://www.youtube.com/embed/B4yV3AO7G6E', 'In Between', '/static/image/song_photo_default.png')

    add_feedback(2, 'Sean','It was ok', 'emo girl')
    add_feedback(4, 'Kelly', 'I loved it', 'emo girl')

    add_comment('Sean', 'emo girl', 'It was ok', '10:33')
    add_comment('Kelly', 'emo girl', 'I loved it', '11:33')


if __name__ == '__main__':
    print('Starting SoundShare population script...')
    populate()
