import os
import shutil


def configuration():
    if os.path.exists('D:\\Study\\All_python\\everything\\Home'):
        shutil.rmtree('Home')
    os.mkdir('Home')
    os.mkdir('Home/User')
    os.mkdir('Home/System')
    os.mkdir('Home/Program Files')
    path = os.path.abspath(os.curdir) + '\\Home\\'
    return path
