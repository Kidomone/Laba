#Чтение всего файла
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    t = file.close()

#Построчное чтение
with open('example.txt', 'r') as file:
    for line in file:
        print(line)



