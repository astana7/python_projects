print('Здраствуй , я могу сложить и вычесть! Введи что ты хочешь!')
a = str(input('- '))
if a == 'сложить':
    print('Введи числа!')
    b = int(input())
    c = int(input())
    print(b+c)
elif a == 'вычесть':
    print('Введи числа!')
    d = int(input())
    f = int(input())
    print(d - f)
elif a == 'умножить':
    print('Введи числа!')
    g = int(input())
    h = int(input())
    print(g * h)
elif a == 'разделить':
    print('Введи числа!')
    q = int(input())
    w = int(input())
    print(q/w)
else:
    print('Ты ввел что-то не то!')