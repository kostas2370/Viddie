import os
from random import randint
from ..models import Music


def generate_directory(name, x=0):
    while True:

        dir_name = (name + (' ' + str(x) if x is not 0 else '')).strip()
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            os.mkdir(f'{dir_name}\\dialogues')

            return dir_name
        else:
            x += 1


def select_music(category=None):
    if category is None:
        raise Exception('You need to add a category')

    music = Music.objects.filter(category = category)
    return music[randint(0, music.count() - 1)]