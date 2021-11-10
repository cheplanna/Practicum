import os 
import shutil


#Функция регистрации для пользователя
def sign_in():
    global user_input
    user_input = input('Enter your login: ')
    if not os.path.isdir(user_input):
        os.mkdir(user_input)
    os.chdir(user_input)



#Функция создает файл, принимает имя файла и возможный текст
def create_file(filename,text=False):
    with open(filename,'w',encoding='utf-8') as f:
        if text:
            f.write(text)
#Функция создает папку, первый параметр - название папки, если мы хотим перейти в какую-то дириекторию, то второй параметр - ее название
def create_folder(foldername,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.mkdir(foldername)
#Функция удаляет папку, первый параметр - название папки, если мы хотим перейти в какую-то дириекторию, то второй параметр - ее название
def remove_folder(foldername, inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.rmdir(foldername)

#Функция удаляет файл, первый параметр - название файла, если мы хотим перейти в какую-то директорию, то второй параметр - ее название  
def remove_file(filename,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.remove(filename)

#Функция меняет директорию 
def change_dir(dirname):
    os.chdir(dirname)
    
#Функция чтения файла, первый параметр - название файла, если мы хотим перейти в какую-то директорию, то второй параметр - ее название
def read_file(filename, inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    with open(filename,'r',encoding='utf-8') as f:
        print(f.read())

#Переименование файла, 1-ый параметр настоящее имя, 2-ой параметр измененное имя, 3-ий параметр название директории для перехода
def rename_file(curr_name,new_name,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.rename(curr_name,new_name)

#Перемещение файла(указывать полный путь)  
def move_file(curr_dir,new_dir):
    shutil.move(curr_dir,new_dir)

#Копируем файл из одной папки в другую, 1-ый параметр- название файла, 2-ой название папки, 3-ий если хотим перейти в другую директорию
def copy_text_file(filename,foldername,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    shutil.copy(filename,foldername)

#Функция для архивации папка и файла
def archive_item(dir):
    shutil.make_archive(dir,'zip')

#Функция разархивации
def unpack_archive_item(dir):
    shutil.unpack_archive(dir,'zip')

command_string = """create_d -- создать директорию
delete_d -- удалить директорию
change -- сменить директорию
make_f -- создать файл
write_f -- записать в файл
read_f -- прочитать из файла
remove_f -- удалить файл
copy_f -- скопировать файл
replace_f -- переместить файл
rename_f -- переименовать файл
exit -- завершить работу"""
print(command_string)
explorer = Explorer(default_folder)
while True:
    command = input((os.getcwd() + "\\").replace(default_folder, "") + ":$ ").split()

    if command[0] == "create_d":
        explorer.create_dir(command[1])
    elif command[0] == "delete_d":
        explorer.remove_dir(command[1])
    elif command[0] == "change":
        explorer.change_dir(command[1])
    elif command[0] == "make_f":
        explorer.touch(command[1])
    elif command[0] == "write_f":
        explorer.write_data(command[1])
    elif command[0] == "read_f":
        explorer.read_data(command[1])
    elif command[0] == "remove_f":
        explorer.remove_f(command[1])
    elif command[0] == "copy_f":
        explorer.copy_file(command[1], command[2])
    elif command[0] == "replace_f":
        explorer.replace_file(command[1], command[2])
    elif command[0] == "rename_f":
        explorer.rename_file(command[1], command[2])

    elif command[0] == 'exit':
        break
