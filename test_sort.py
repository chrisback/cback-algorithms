from sort import insertion_sort, selection_sort, merge_sort

def test_insertion_sort():
    arr = [2, 5, 7, 3, 20, 1, 0]
    assert insertion_sort(arr) == [0, 1, 2, 3, 5, 7, 20]
    assert arr == [2, 5, 7, 3, 20, 1, 0]

def test_insertion_sort_in_place():
    arr = [2, 5, 7, 3, 20, 1, 0]
    assert insertion_sort(arr, in_place=True) == [0, 1, 2, 3, 5, 7, 20]
    assert arr == [0, 1, 2, 3, 5, 7, 20]

def test_insertion_sort_0_1_length():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]

def test_selection_sort():
    arr = [2, 5, 7, 3, 20, 1, 0]
    assert selection_sort(arr) == [0, 1, 2, 3, 5, 7, 20]
    assert arr == [2, 5, 7, 3, 20, 1, 0]

def test_selection_sort_in_place():
    arr = [2, 5, 7, 3, 20, 1, 0]
    assert selection_sort(arr, in_place=True) == [0, 1, 2, 3, 5, 7, 20]
    assert arr == [0, 1, 2, 3, 5, 7, 20]

def test_selection_sort_0_1_length():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]

def test_merge_sort():
    arr = [2, 5, 7, 3, 20, 1, 0]
    assert merge_sort(arr) == [0, 1, 2, 3, 5, 7, 20]
    assert arr == [2, 5, 7, 3, 20, 1, 0]
