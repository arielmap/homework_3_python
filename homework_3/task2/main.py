def funk_arr2sum(arr):
    print(arr)
    sum = []
    b = len(arr)//2+1 if len(arr)%2 > 0  else len(arr)//2
    for i in range(b):
        sum.append(arr[i]*arr[-i-1])
    return sum

arr = input("введите чилса через запятую : ")
split_arr = [int(i) for i in arr.split(',')]
print(funk_arr2sum(split_arr))