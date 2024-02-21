'''
Other algorithm implementations from text
'''

def search_sum(arr, s):
    '''
    Determines whether two members of arr sum to exactly s.
    '''
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == s:
                return (i, j)
            j += 1
        i += 1
    return None
