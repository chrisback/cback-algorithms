def search(arr, x):
    n = len(arr)
    i = 0

    while i < n:
        if arr[i] == x:
            return i
        i += 1
    return None
