def if_one_away(string1, string2):
    if len(string1)+1 < len(string2):
        return False
    elif len(string1) > len(string2)+1:
        return False

    elif len(string1) == len(string2):
        # we need to update/change one char to see the match
        # and all else chars are same
        # otherwise return false
        edited = False
        for char1, char2 in zip(string1, string2):
            if char1 is not char2:
                if edited:
                    return False
                edited = True

    elif len(string1) + 1 == len(string2) or len(string1) == len(string2)+1:
        # we need to insert or delete one char to see the match
        # and all else chars are same
        # otherwise return false
        index1 = index2 = 0
        edited = False
        while index1 < len(string1) and index2 < len(string2):
            if string1[index1] != string2[index2]:
                if edited:
                    return False
                edited = True
                if len(string1)<len(string2):
                    index2 += 1
                else:
                    index1 += 1
            else:
                index1+=1
                index2+=2

    return True

print(if_one_away('str', 'str'))  # True
print(if_one_away('sdf', 'stjf')) # False
print(if_one_away('sdf', 'stf'))  # True
print(if_one_away('sdf', 'sfd'))  # False