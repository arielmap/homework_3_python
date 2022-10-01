def funk_febonachi(n):
    ans_arr = [0]
    j = 1
    for i in range(1,n+1):
        if i%2 == 0:
            ans_arr.insert(0,-j)
        else:
            ans_arr.insert(0,j)
        ans_arr.append(j)
        j += ans_arr[-2]
    return ans_arr

n = int(input("Введите число: "))
print(funk_febonachi(n))