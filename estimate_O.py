import json
import random
import time
from sort import insertion_sort, selection_sort, merge_sort, bubble_sort

def timeit(func, size=1000, iterations=1, multiples=1):
    res = {}
    for i in range(1, multiples+1):
        n = size*i
        multiple_results = []
        for _ in range(iterations):
            arr = [random.randint(0, n) for _ in range(n)]
            start = time.time()
            func(arr)
            multiple_results.append(time.time() - start)
        res[n] = sum(multiple_results) / iterations
    return res

if __name__ == "__main__":
    results = {}
    results["insertion_sort"] = timeit(insertion_sort, 100, 5, 10)
    results["selection_sort"] = timeit(selection_sort, 100, 5, 10)
    results["bubble_sort"] = timeit(bubble_sort, 100, 5, 10)
    results["merge_sort"] = timeit(merge_sort, 1000, 5, 10)
    print(json.dumps(results, indent=2))
