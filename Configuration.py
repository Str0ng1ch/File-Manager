import os
import shutil


def configuration():
    path = os.path.abspath(os.curdir) + '\\Home\\'
    if os.path.exists(path):
        shutil.rmtree('Home')
    os.mkdir('Home')
    os.mkdir('Home/User')
    os.mkdir('Home/System')
    os.mkdir('Home/Program Files')
    return path
