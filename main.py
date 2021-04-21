import os, os.path

'''root_path = '/загрузки/Telegram Desktop/'

for root, dirs, files in os.walk(root_path):
   for name in files:
      print(os.path.join(root, name))


for address, dirs, files in folder:
   for file in files:
      print(address+'/'+file)


def main():
   while True:
      print(os.getcwd())
      print('MENU')
      command = acceptCommand()
      runCommand(command)
      if command == QUIT:
         print('Работа программы завершена.')
         break
folder = []
for i in os.walk('test'):
   folder.append(i)
print(folder)
#print (len(['PycharmProjects' for 'PycharmProjects' in os.listdir('.') if os.path.isfile('PycharmProjects')]))
list = os.listdir(os.getcwd())
number_files = len(list)
print (number_files)
print(os.getcwd())
#print(os.listdir())

pdir = 'C:/Users/gaga7/PycharmProjects/case.9'
contdir = []
end_list= []
for i in os.walk(pdir):
   contdir.append(i)
for i in contdir:
   i = str(i)
   end_list.append(i[i.find(',')+1:-1])
print(end_list)


def folder_size(path='.'):
   total = 0
   for entry in os.scandir(path):
      if entry.is_file():
         total += entry.stat().st_size
      elif entry.is_dir():
         total += folder_size(entry.path)
   return total

#считает колчество байт
def countBytes(folder):
    print(os.getcwd())
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        #print(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += countBytes(itempath)
    return total_size
print(countBytes('.'))

#print (str(countBytes(".git")))

def countFiles(folder):
   total_file = os.path.getsize(folder)

   for item in os.listdir(folder):
      itempath = os.path.join(folder, item)
      if os.path.isfile(itempath):
         total_file += os.path.getsize(itempath)
      elif os.path.isdir(itempath):
         total_file += countFiles(itempath)
         print(countFiles(itempath))
   return total_file


for root, directories, files in os.walk(r"os.getcwd()"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)'''


def main():
    print(os.getcwd())
    function = acceptCommand()
    runCommand(function)


def acceptCommand():
    function = int(input('''1.Промотр каталога 2.На уровень вверх 3.На уровень вниз 4.Количество файлов и каталогов 5.Размер текущего файла в байтах 6.Поиск файла 7.Выход из пргораммы Выберите пункт меню:'''))
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
    elif command==7:
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

#main()
pdir = 'C:/Users/gaga7/PycharmProjects/case.9'
contdir = []
end_list= []
for i in os.walk(pdir):
   contdir.append(i)
for i in contdir:
   i = str(i)
   end_list.append(i[i.find(',')+1:-1])
print(end_list)