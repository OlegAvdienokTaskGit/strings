"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3. Циклы не использовать.
"""

index_string = 'Lorem ipsum set amet'
lis = list(index_string) # делаем из строки список, чтобы использовать del
del lis[::3] # срезом удаляем каждый 3 символ

print(''.join(lis)) #делаем из списка строку
