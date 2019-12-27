def urlify(string, length):
    newString = ''
    counter = 0
    for char in string:
        if char == ' ':
            newString += '%20'
        else:
            newString += char
        counter += 1
        if counter == length:
            break
    return newString

string= 'Mr John Doe    '
print(urlify(string, 11))