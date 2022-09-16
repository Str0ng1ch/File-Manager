import os
import shutil
from Configuration import configuration

running = True
path, user_path = configuration(), configuration().replace(os.path.abspath(os.curdir) + '/', '')


def create_folder():
    os.mkdir(path + input('Введите название папки: '))


def delete_folder():
    shutil.rmtree(path + input('Введите название папки: '))


def between_folders():
    global path, user_path
    print('Введите путь: ', user_path, end='')
    move = input().split('/')[0]
    if move == '..' and len(' '.join(user_path.split('/')).split()) > 1:
        path = '/'.join(path.split('/')[:-2]) + '/'
    elif move == '..' and len(' '.join(user_path.split('/')).split()) == 1:
        print()
        print('Вы уже находитесь в корневой директории!')
    else:
        if os.path.exists(path + move):
            path += move + '/'
        else:
            print()
            print('Такой директории не существует!')
    user_path = path.replace(os.path.abspath(os.curdir) + '/', '')


def create_file():
    open(path + input('Введите название файла: '), "x")


def write_in_file():
    file = open(path + input('Введите название файла: '), "w")
    file.write(input('Введите текст: '))


def read_file():
    file = open(path + input('Введите название файла: '), "r")
    print(file.read())


def delete_file():
    os.remove(path + input('Введите название файла: '))


def copy_file():
    shutil.copy(path + input('Введите название копируемого файла: '), path + input('Введите имя нового файла: '))


def move_file():
    os.replace(path + input('Введите старое расположение файла: '), path + input('Введите новое расположение файла: '))


def rename_file():
    os.rename(path + input('Введите старое название файла: '), path + input('Введите новое название файла: '))


def end_program():
    global running
    running = False


def main():
    global user_path

    all_actions = [('Создание папки', create_folder), ('Удаление папки', delete_folder),
                   ('Перемещение между папками', between_folders), ('Создание пустых файлов', create_file),
                   ('Запись текста в файл', write_in_file), ('Просмотр содержимого текстового файла', read_file),
                   ('Удаление файла', delete_file), ('Копирование файла', copy_file), ('Перемещение файла', move_file),
                   ('Переименование файла', rename_file),
                   ('Выход из программы', end_program)]
    while running:
        print('Вы находитесь в директории', user_path)
        for i in range(len(all_actions)):
            print(i + 1, ') ', all_actions[i][0], sep='')
        action = input('Ваше решение: ')

        try:
            if action.isdigit():
                all_actions[int(action) - 1][1]()
            elif action in [str(item[1]).split()[1] for item in all_actions]:
                all_actions[[str(item[1]).split()[1] for item in all_actions].index(action)][1]()
        except FileExistsError:
            print('Такой файл уже существует!')
        except FileNotFoundError:
            print('Такого файла не существует!')
        except OSError:
            print('Некорректный путь!')
        print()


if __name__ == '__main__':
    main()
