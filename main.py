"""
Case-study 9
Developers:
Кривошапова Д. Е.:30%
Кузнецов А. Д.: 25%
Лапочкин Д. А.: 
"""
import os


def main():
    '''
    The main function that outputs the path to the current directory and the menu. Calls the command execution function.
    :return: None
    '''
    print(os.getcwd())
    function = acceptCommand()
    runCommand(function)


def acceptCommand():
    """
    Requests the command number.Commands are requested until the correct command number is entered.
    :return: the correct command number
    """
    function = int(input('''1.Промотр каталога
2.На уровень вверх
3.На уровень вниз
4.Количество файлов и каталогов
5.Размер текущего файла в байтах
6.Поиск файла
7.Выход из пргораммы
Выберите пункт меню:
'''))
    if function in (1, 2, 3, 4, 5, 6, 7):
        return function
    else:
        print('Номер команды указан некорректно ')
        acceptCommand()


def runCommand(command):
    """
    Determines by the command number which function should be executed.
    :param command: the number of command
    :return:None
    """
    if command == 1:
        all()
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown(os.getcwd())
    elif command == 4:
        path = input('Введите "." для подсчета файлов в текущем каталоге, или укажите путь к нужному каталогу: ')
        print(countFiles(path), 'файлов в каталоге.\n')
        runCommand(acceptCommand())
    elif command == 5:
        path = input('Введите "." для подсчета суммарный объемf файлов в текущем каталоге, или укажите путь к нужному каталогу: ')
        print('Общий размер файлов в каталоге составляет', countBytes(path), 'байт.\n')
        runCommand(acceptCommand())
    elif command == 6:
        target = input('Введите имя файла, который требуется найти: ')
        path = input('Введите "." для поиска файла в текущем каталоге, или укажите путь к нужному каталогу: ')
        if path == '.':
            path = os.getcwd()
        print(findFiles(target, path), '\n')
        runCommand(acceptCommand())
    elif command == 7:
        print('Спасибо за использование нашей программы')
        exit()


def all():
    path = os.getcwd()
    name_list = os.listdir(path)
    full_list = [os.path.join(path, i) for i in name_list]
    print(full_list)

def moveUp():
    """
    Makes the parent directory current.
    :return: None
    """
    currentDir = os.getcwd()
    if currentDir.rfind('\\') == 2:
        UpDir = currentDir[:currentDir.rfind('\\')+1]
    else:
        UpDir = currentDir[:currentDir.rfind('\\')]
    os.chdir(UpDir)
    print(os.getcwd())
    runCommand(acceptCommand())


def moveDown(currentDir):
    """
    Requests the name of the subdirectory. it makes the directory located in currentDir the current one.
    :param currentDir: current directory
    :return:None
    """
    name = input('Ведите имя подкаталога: ')
    new_name = currentDir + r'\\' + name
    if os.path.exists(new_name):
        os.chdir(new_name)
        print(os.getcwd())
    else:
        print('Такого файла или папки не существует.')
    runCommand(acceptCommand())


def countFiles(path):
    """
    A recursive function that counts the number of files in the specified path.
    :param path: the mame of the directory
    :return:the number of files
    """
    directory = os.listdir(path)
    files = []
    dirs = []
    for item in directory:
        if os.path.isfile(path + '\\' + item):
            files.append(item)
    for item in directory:
        if item not in files:
            dirs.append(item)
    if len(dirs) == 0:
        return len(files)
    count = 0
    for item in dirs:
        count += countFiles(path + '\\' + item)
    return count + len(files)


def countBytes(path):
    """
    A recursive function that calculates the total size (in bytes) of all files in the specified path.
    :param path: the name of tne directory
    :return: total size (in bytes) of files
    """
    total_size = os.path.getsize(path)
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += countBytes(itempath)
    return total_size


def findFiles(target, path):
    """
    A recursive function that generates a list of paths to files that contain target.
    :param target: tne name of the file
    :param path: the name of tne directory
    :return: list of paths to target
    """
    directory = os.listdir(path)
    dirs = []
    pool = []
    for item in directory:
        if os.path.isdir(path + '\\' + item):
            dirs.append(item)
    if len(dirs) == 0:
        if target in directory:
            return pool + [path + '\\' + target]
    for item in dirs:
        pool += findFiles(target, path + '\\' + item)
    if target in directory:
        return pool + [path + '\\' + target]
    if path == os.getcwd() and len(pool) == 0:
        return 'Не найдено ни одного файла с таким именем'
    return pool


if __name__ == '__main__':
    main()
