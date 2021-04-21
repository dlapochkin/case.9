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


main()
