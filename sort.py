'''
Sort functions
'''

def bubble_sort(arr: list, in_place=False) -> list:

    if in_place:
        res = arr
    else:
        res = arr.copy()

    i = 0
    while i < len(res):
        j = len(res)-1
        while j > i:
            a = res[j-1]
            b = res[j]
            if a > b:
                res[j] = a
                res[j-1] = b
            j -= 1
        i += 1
    return res

def insertion_sort(arr: list, in_place=False) -> list:
    '''
    O(n^2)
    '''
    if in_place:
        res = arr
    else:
        res = arr.copy()
    n = len(res)
    if n <= 1:
        return res
    
    for i in range(1, n):
        current = res[i]
        j = i - 1
        while j >= 0 and res[j] > current:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = current
    return res

def selection_sort(arr, in_place=False):
    '''
    O(n^2)
    '''
    if in_place:
        res = arr
    else:
        res = arr.copy()
    n = len(res)
    if n <= 1:
        return res
    
    for i in range(0, n-1):
        # find the index of the smallest value in the array between index i and n-1
        s = i
        for j in range(i+1, n):
            if res[j] < res[s]:
                s = j
        
        if s != i:
            v = res[s]
            res[s] = res[i]
            res[i] = v 
    return res

def merge_sort(arr: list) -> list:
    '''
    O(n lg(n))
    '''
    n = len(arr)
    if n == 1:
        return arr.copy()
    
    # From testing, insertion sort performas better than
    # merge sort on arrays ~< 70
    #if n <= 70:
    #    return insertion_sort(arr)
    
    x = merge_sort(arr[0:n//2])
    y = merge_sort(arr[n//2:n])
    z = []

    while len(x) > 0 and len(y) > 0:
        if x[0] < y[0]:
            z.append(x.pop(0))
        else:
            z.append(y.pop(0))
    while len(x) > 0:
        z.append(x.pop(0))
    while len(y) > 0:
        z.append(y.pop(0))
    return z
