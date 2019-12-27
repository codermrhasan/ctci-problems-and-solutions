def string_compression(string):
    pre_index = 0
    newString = ''
    counter = 1 if len(string)==1 else 0
    for index in range(len(string)):
        if string[index] is not string[pre_index]:
            newString += string[pre_index] + str(counter)
            pre_index = index
            counter = 0
            
        if len(string) == index + 1:
            if len(string) > 1:
                counter += 1
            newString += string[pre_index] + str(counter)
        else:
            if string[index] == string[pre_index]:
                counter += 1
    return newString if len(newString)<len(string) else string

print(string_compression('ab'))  # ans: ab
print(string_compression('a'))   # ans: a
print(string_compression('aaabbbccc'))  # ans: a3b3c3
print(string_compression('aaaab'))  # ans: a4b1