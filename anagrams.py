def anagrams(my_string1, my_string2):
    if sorted(my_string1.lower()) == sorted(my_string2.lower()):
        return True
    else:
        return False
