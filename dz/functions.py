import os

cur_path = os.getcwd()

def picture_path(name):
    return os.path.join(cur_path, f'pictures\{name}.png')