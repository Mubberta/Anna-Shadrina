# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 #Информационный объем дискеты
count = 100 #Количество страниц в книге
lines = 50 #Число строк на странице
symbol = 25 #Количество символов в строке
one_volume = 4 #Для хранения кода одного символа
k = 1024
transfer = volume * k * k

all_volume = count * lines * symbol * one_volume
number =  round(transfer / all_volume, 0)
print(f"Количество книг, помещающихся на дискету: {number:.0f}")
