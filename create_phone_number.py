def create_phone_number(n):
#    n = str(n)
    number = '('
    for i in range(len(n)):
        if i == 2:
            number += str(n[i]) + ') '
        elif i == 5:
            number += str(n[i]) + '-'
        else:
            number += str(n[i])
    return number
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))