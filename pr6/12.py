## #ВАРИАНТ 12##


sp = [112, 21, 5, 56, 100, 63, 50, 81, 28, 15]
m = max(sp)
for i in range(len(sp)): 
    if sp[i] % 2 != 0:  
        if m >= sp[i]: 
            m = sp[i]
print('Наименьший нечетный элемент списка:', m)

##2 часть##
a = [115, 91, 25, 85, 20, 63, 74, 81, 62, 13]   
b = [437, 12, 13, 14, 20, 54, 96, 69, 16, 67]
a, b = b, a 
print('Cписок А теперь выглядит так:', a)
print('Cписок B теперь выглядит так:', b)
