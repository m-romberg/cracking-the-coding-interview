def compress_string(s):
    """
    Compress string. Return compression only if shorter than original string.

    >>> compress_string('aabb')
    'aabb'

    >>> compress_string( "aabbb")
    'a2b3'

    >>> compress_string("aabbbba")
    'a2b4a1'

    >>> compress_string("AAAaaaBBBbb")
    'A3a3B3b2'
    """

    new_string = ""

    curr_char = None
    counter = 0


    for i in range(1, len(s)):
        if curr_char is None:
            curr_char = s[0]
            counter+=1
        if curr_char == s[i]:
            counter+=1
        else:
            new_string += (curr_char + str(counter))
            curr_char = s[i]
            counter = 1
        #accounts for the last letter after the loop ends
        if i == len(s)-1:
            new_string += (curr_char + str(counter))

    return s if len(new_string) >= len(s) else new_string