def swap_case(s):
    ''''result = ""
    for c in s:
        if c.isupper():
            result += c.lower()
        if c.islower():
            result += c.upper()
    return result
    '''
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)