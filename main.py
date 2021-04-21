import os


def main():
    print(os.getcwd())
    function = acceptCommand()
    runCommand(function)


def acceptCommand():
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
    acceptCommand()


def runCommand(command):
    if command == 2:
        moveUp()
    elif command == 3:
        moveDown(os.getcwd())
    elif command == 4:
        path = input('Введите "." для подсчета файлов в текущем каталоге, или укажите путь к нужному каталогу: ')
        print(countFiles(path), 'файлов в каталоге.\n')
        runCommand(acceptCommand())
    elif command==5:
        path = input('Введите "." для подсчета файлов в текущем каталоге, или укажите путь к нужному каталогу: ')
        print(countBytes(path), 'размер файлов в каталоге.\n')
        runCommand(acceptCommand())
    elif command == 7:
        print('Спасибо за использование нашей программы')
        exit()


def moveUp():
    currentDir = os.getcwd()
    print(os.getcwd())
    UpDir = currentDir[:currentDir.rfind('\\')]
    os.chdir(UpDir)
    print(os.getcwd())
    runCommand(acceptCommand())


def moveDown(currentDir):
    name = input('Ведите имя подкаталога:')
    new_name = currentDir + r'\\' + name
    if os.path.exists(new_name):
        os.chdir(new_name)
        print(os.getcwd())
    else:
        print('Такого файла или папки не существует')
    runCommand(acceptCommand())


def countFiles(path):
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
    total_size = os.path.getsize(path)
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += countBytes(itempath)
    return total_size


main()
