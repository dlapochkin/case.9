import os
def main():
    print(os.getcwd())
    function=input('''1.Промотр каталога
    2.На уровень вверх
    3.На уровень вниз
    4.Количество файлов и каталогов
    5.Размер текущего файла в байтах
    6.Поиск файла
    7.Выход из пргораммы
    Выбирете пункт меню:
    ''')
def moveUp():
    currentDir=os.getcwd()
    print(os.getcwd())
    UpDir= currentDir[:currentDir.rfind('\\')]
    os.chdir(UpDir)
    print(os.getcwd())
def moveDown(currentDir):
    name=input()
    new_name=currentDir+r'\\'+ name
    if os.path.exists(new_name):
        os.chdir(new_name)
        print(os.getcwd())
    else:
        print('Такого файла или папки не существует')
