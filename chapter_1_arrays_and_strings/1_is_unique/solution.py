def is_unique(a_string):
    char_counter = [0] * 128
    unique = True
    
    if len(a_string) > 128:
        return False

    for char in a_string:
        char_counter[ord(char)] += 1
            
        if char_counter[ord(char)] > 1:
            unique = False
    
    return unique

string = input()
answer = 'unique' if is_unique(string) else 'not unique'
print(answer)
