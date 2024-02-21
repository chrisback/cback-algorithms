

class BinaryHeap:
    def __init__(self, arr=None):
        self._arr = arr
        i = len(arr) - 1
        while (i >= 0):
            self._max_heapify(i)
            i -= 1

    def _left(self, i):
        left_i = ((i+1) << 1) - 1
        if left_i >= len(self._arr):
            return None
        return left_i

    def _right(self, i):
        right_i = (i+1) << 1
        if right_i >= len(self._arr):
            return None
        return right_i

    def _parent(self, i):
        if i == 0:
            return None
        return ((i+1) >> 1) - 1

    def _max_heapify(self, i):
        largest = i
        left_i = self._left(i)
        if left_i and self._arr[left_i] > self._arr[largest]:
            largest = left_i
        right_i = self._right(i)
        if right_i and self._arr[right_i] > self._arr[largest]:
            largest = right_i

        if largest != i:
            largest_v = self._arr[largest]
            self._arr[largest] = self._arr[i]
            self._arr[i] = largest_v
            self._max_heapify(largest)

    def arr(self):
        return self._arr


        