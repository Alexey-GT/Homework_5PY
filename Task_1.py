#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст ').split()
del_text = 'абв'
res_text = ''.join(list(filter(lambda x: del_text not in x, text)))
print(res_text)


