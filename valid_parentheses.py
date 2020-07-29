def valid_parentheses(s):
    count = 0
    for i in range(len(s)):
        if count < 0:
            return False
        elif s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
    if count != 0:
        return False
    else:
        return True
a = '()(()'
print(valid_parentheses(a))