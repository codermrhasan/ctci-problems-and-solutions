def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    char_set = [0] * 128
    
    for char in string1:
        char_set[ord(char)] += 1
    
    for char in string2:
        char_set[ord(char)] -= 1
        if char_set[ord(char)] < 0:
            return False

    return True

str1 = input()
str2 = input()

answer = 'is permutation' if check_permutation(str1, str2) else 'not permutation'
print(answer)