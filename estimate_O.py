import json
import random
import time
from sort import insertion_sort, selection_sort, merge_sort

def timeit(func, size=1000, iterations=1, multiples=1):
    results = {}
    for i in range(1, multiples+1):
        n = size*i
        multiple_results = []
        for _ in range(iterations):
            arr = [random.randint(0, n) for _ in range(n)]
            start = time.time()
            func(arr)
            multiple_results.append(time.time() - start)
        results[n] = sum(multiple_results) / iterations
    return results

if __name__ == "__main__":
    results = {}
    #results["insertion_sort"] = timeit(insertion_sort, 10, 5, 10)
    #results["selection_sort"] = timeit(selection_sort, 10, 5, 10)
    results["merge_sort"] = timeit(merge_sort, 10000, 5, 10)
    print(json.dumps(results, indent=2))
