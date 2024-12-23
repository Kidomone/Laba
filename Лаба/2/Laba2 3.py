def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        print('True')
    else:
        print('False')
is_prime(int(input('Введите число: ')))



