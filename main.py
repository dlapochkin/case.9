import os
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
