print('Здравствуй , это мини-калькулятор')
print('Введи 2 числа!')
b = int(input())
c = int(input())

print('1 - сложить, 2 - отнять, 3 - умножить, 4 - делить')
a = int(input())
if a == 1:
    print(b + c)
elif a == 2:
    print(b - c)
elif a == 3:
    print(b * c)
elif a == 4:
    print(b / c)
else:
    print('Ты ввел что-то не то!')