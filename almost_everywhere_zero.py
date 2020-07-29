def almost_everywhere_zero(n, k):
    lst = []
    for i in range(n+1):
        if count_not_zero(i) == k:
            lst.append(i)
    return lst
def count_not_zero(num):
    num = str(num)
    count = 0
    for i in num:
        if i != "0" :
            count += 1
    return count
print(almost_everywhere_zero(100,1))