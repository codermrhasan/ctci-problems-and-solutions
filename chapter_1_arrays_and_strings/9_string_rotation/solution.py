def is_substring(string, substring):
    return string.find(substring) != -1
def string_rotation(string1, string2):
    if len(string1) == len(string2) != 0:
        return is_substring(string1+string1, string2)
    return False


# manual testing
print(string_rotation('waterbottle', 'erbottlewat')) # True
print(string_rotation('foo','ofo')) # True
print(string_rotation('aa', 'a')) # False
