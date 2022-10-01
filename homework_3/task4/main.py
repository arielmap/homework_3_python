
def task(n):
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n//=2
    return num

n = int(input("Введите число "))
print(task(n))