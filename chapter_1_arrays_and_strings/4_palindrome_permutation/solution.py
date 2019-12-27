def is_palindrome_permutation(string):

    char_set = [0] * 26
    total_letter = 0
    total_odd = 0

    for char in string:
        if char >= 'A' and char <= 'Z':
            index = ord(char) + ord('A')

        elif char >= 'a' and char <= 'z':
            index = ord(char)-ord('a')

        if char is not ' ':
            total_letter += 1
            char_set[index] += 1

    if total_letter % 2 == 0:
        for i in range(26):
            if char_set[index] % 2:
                return False

    elif total_letter % 2 == 1:
        for i in range(26):
            if char_set[i] % 2 == 1:
                total_odd += 1
        if total_odd > 1:
            return False

    return True


print(is_palindrome_permutation('sskdfjs'))
print(is_palindrome_permutation('sas'))
print(is_palindrome_permutation('ssaa'))
