def is_one_away(s1, s2):
    """
    Checks if strings are one edit (add, delete, replace) away

    >>> is_one_away("pale", "ale")
    True

    >>> is_one_away("pale", "ple")
    True

    >>> is_one_away("pales", "pale")
    True

    >>> is_one_away("pale", "bake")
    False

    >>> is_one_away("heart", "heartier")
    False
    """

    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) > len(s2):
        s1, s2 = [s2, s1]
    edits_needed = 0

    s1_counter = 0
    s2_counter = 0

    while (s1_counter < len(s1) and s2_counter < len(s2)):
        if edits_needed == 2: return False
        if (s1[s1_counter] == s2[s2_counter]):
            s1_counter+=1
            s2_counter+=1
        else:
            if len(s1) == len(s2):
                s1_counter+=1
            s2_counter+=1
            edits_needed+=1
    return True