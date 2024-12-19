numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
right = numbers[:4]
left = numbers[5:]
sum_right = sum(right)
len_right = len(right)
sum_left = sum(left)
len_left = len(left)
sum_ = sum_left + sum_right
len_ = len(numbers)
numbers[4] = sum_ / len_
print("Измененный список:", numbers)
