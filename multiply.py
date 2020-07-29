import math
def multiply(n, k):
    if k > n or k == 1:
        return 1
    def division(num):
        lst = [num]
        for i in range(2, 500):
            for n in lst:
                if n % (i) == 0:
                    tmp = n / (i)
                    if tmp not in lst:
                        lst.append(int(tmp))
        for k in range(len(lst)):
            if lst[0] % lst[k] == 0 and lst[0] / lst[k] not in lst:
                lst.append(int(lst[0] / lst[k]))
        return len(lst)

    count = division(n)
    if k == 2:
        return count
    else:
        return int(abs(math.factorial(count) / (math.factorial(abs(k)) * math.factorial(abs(count-k))) - 2))


print(multiply(20, 3))