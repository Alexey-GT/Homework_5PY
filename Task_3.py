#Создайте программу для игры в ""Крестики-нолики"".

import random
def win_x(pole):
    if pole[0][0] == 'X' and pole [1][1] == 'X' and pole [2][2] == 'X':
        print('Вы победили!!!')
        return True
    elif pole[2][0] == 'X' and pole [1][1] == 'X' and pole [0][2] == 'X':
        print('Вы победили!!!')
        return True
    elif pole[0][0] == 'X' and pole [0][1] == 'X' and pole [0][2] == 'X':
        print('Вы победили!!!')
        return True
    elif pole[0][0] == 'X' and pole [1][0] == 'X' and pole [2][0] == 'X':
        print('Вы победили!!!')
        return True
    elif pole[2][0] == 'X' and pole [2][1] == 'X' and pole [2][2] == 'X':
        print('Вы победили!!!')
        return True
    elif pole[0][2] == 'X' and pole [1][2] == 'X' and pole [2][2] == 'X':
        print('Вы победили!!!')
        return True
    else:
        return False

def win_o(pole):
    if pole[0][0] == '0' and pole [1][1] == '0' and pole [2][2] == '0':
        print('Бот победил!!!')
        return True
    elif pole[2][0] == '0' and pole [1][1] == '0' and pole [0][2] == '0':
        print('Бот победил!!!')
        return True
    elif pole[0][0] == '0' and pole [0][1] == '0' and pole [0][2] == '0':
        print('Бот победил!!!')
        return True
    elif pole[0][0] == '0' and pole [1][0] == '0' and pole [2][0] == '0':
        print('Бот победил!!!')
        return True
    elif pole[2][0] == '0' and pole [2][1] == '0' and pole [2][2] == '0':
        print('Бот победил!!!')
        return True
    elif pole[0][2] == '0' and pole [1][2] == '0' and pole [2][2] == '0':
        print('Бот победил!!!')
        return True
    else:
        return False



pole = [['__','__','__'],
        ['__','__','__'],
        ['__','__','__']]
for i in pole:
    print(i)

while not win_x(pole) and not win_o(pole):
    a, b = int(input('Введите координату a: ')), int(input('Введите координату b: ')) #вводим координаты пользователем
    pole[a][b] = 'X'
    for i in pole:
        print(i)
    print('Ход компьютера')
    while True: # что - бы не поставил где X
        c, d = random.randint(0,2), random.randint(0,2)
        if pole[c][d] == '__':
            break
    pole[c][d] = '0'
    for i in pole:
            print(i)