"""
Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, 
то длина первой части должна быть на один символ больше). Переставьте эти две части местами, 
результат запишите в новую строку и выведите на экран.
При решении этой задачи не стоит пользоваться инструкцией if.
"""

index_string = 'Lorem ipsum set amet'
slice_string_1 = index_string[:11]
slice_string_2 = index_string[12:]
print(slice_string_1)
print(slice_string_2)

print(slice_string_2 + ' ' + slice_string_1) 


