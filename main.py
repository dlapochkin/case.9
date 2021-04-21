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
print(folder)'''
#print (len(['PycharmProjects' for 'PycharmProjects' in os.listdir('.') if os.path.isfile('PycharmProjects')]))
list = os.listdir(os.getcwd())
number_files = len(list)
print (number_files)
print(os.getcwd())
print(os.listdir())

pdir = 'C:/Users/gaga7/PycharmProjects/case.9'
contdir = []
end_list= []
for i in os.walk(pdir):
   contdir.append(i)
for i in contdir:
   i = str(i)
   end_list.append(i[i.find(',')+1:-1])
print(end_list)
