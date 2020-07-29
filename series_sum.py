def series_sum(n):
    if n == 0:
        return 0
    else:
        i = 1
        summ = 1.00
        s = 1
        while i <n:
            s += 3
            summ += 1 / s
            i += 1
        return ("%.2f" %summ)
series_sum(0)