def division(num):
    lst = [num]
    for i in range(2,500):
        for n in lst:
            if n % (i) == 0:
                tmp = n / (i)
                if tmp not in lst:
                    lst.append(int(tmp))
    for k in range(len(lst)):
        if lst[0] % lst[k] == 0 and lst[0] / lst[k] not in lst:
            lst.append(int(lst[0] / lst[k]))
    print(lst)
    return len(lst)
print(division(20))
