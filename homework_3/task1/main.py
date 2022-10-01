list = [2, 3, 5, 9, 3]
print(list)
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print(f'Сумма элементов, стоящих на нечётной позиции = ', sum)