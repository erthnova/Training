def alphabet_position(text):
    import string
    text = text.lower()
    textform = ''
    for letter in text:
        if letter.isalpha() == True:
            textform += str(string.ascii_lowercase.find(letter) + 1) + ' '
    return textform[0:-1]
print(alphabet_position("The sunset sets at twelve o' clock."))