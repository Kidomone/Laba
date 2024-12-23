try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
        t = file.close()
except FileNotFoundError:
    print('Файл не существует')


