'''
Search functions
'''

def linear_search(arr, x):
    '''
    O(n)
    '''
    n = len(arr)
    i = 0

    while i < n:
        if arr[i] == x:
            return i
        i += 1
    return None

def binary_search(arr, x, s=0, e=None):
    '''
    O(ln(n))
    '''
    # if e is not defined, set it to the length of arr
    if e is None:
        e = len(arr)

    if s == (e - 1):
        if x == arr[s]:
            return s
        return None

    # find the midpoint between indexes i and j
    i = (s + e)//2

    if x == arr[i]:
        return i

    if x < arr[i]:
        return binary_search(arr, x, s=s, e=i) 

    return binary_search(arr, x, s=i+1, e=e)
