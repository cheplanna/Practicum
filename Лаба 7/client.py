import socket

def sending(sock, msg):
    lenght = f'{len(msg):<4}'
    sock.send(f'{lenght}{msg}'.encode())

def reciev(sock):
    recv_msg = int(sock.recv(4).decode().strip())
    data = sock.recv(recv_msg*2).decode()
    return data

sock = socket.socket()
flag = False
while not flag:
    try:
        host = input("Ваш хост:")
        if host == "":
            host = 'localhost'
        port = input("Ваш порт:")
        if port == "":
            port = 9090
        print('Соединение')
        sock.connect((host, int(port)))
        choise = input('Чтобы создать аккаунт надо нажать 1, если вы уже зарегистрированы, введите 2: ')
        sending(sock, choise)

        #Check login
        msg=input("Введите логин: ")
        sending(sock, msg)
        proverka = reciev(sock)
        while proverka == 'False':
            print("Wrong user name!")
            msg = input('Введите логин админа:')
            sending(sock, msg)
            proverka = reciev(sock)

        #check password
        password=input("Введите пароль: ")
        sending(sock, password)
        proverka = reciev(sock)
        while proverka == 'False':
            print("Неправильный пароль")
            password = input('Введите пароль: ')
            sending(sock, password)
            proverka = reciev(sock)

        request = ''
        '''print('ls (название директории)- выводит содержимое каталога\n' \
           'pwd - выводит путь текущего каталога\n' \
           'mkdir (название директории) - создает каталог\n' \
           'echo (название файла) (текст) - создает пустой файл или файл с текстом\n' \
           'rm (название файла) - удаляет файл\n' \
           'mv (название файла) (название директории или файла) - перемещает (переименовывает файл)\n' \
           'cat (название файла) - выводит содержимое файла\n' \
           'help - выводит справку по командам\n' \
           'exit - разрыв соединения с сервером')'''
              
        while request != 'exit':
            request = input('@nikita: ')
            sending(sock, request)
            response = reciev(sock)
            if request=='exit':
                print('Конец соединения')
            else:
                print(response)

        flag= True
    except KeyboardInterrupt:
        sock.close()


        