numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
num1 = numbers[0:4]
num2 = numbers[5:22]
l = num1 + num2
s_umm = sum(l)
l_en = len(numbers)
None_new = s_umm/l_en
numbers [4] = None_new
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:",numbers )



