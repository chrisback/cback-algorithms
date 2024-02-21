from search import linear_search, binary_search

def test_linear_search():
    arr = [0,1,2,3,4,5,6,7,8]
    assert linear_search(arr, 0) == 0
    assert linear_search(arr, 8) == 8
    assert linear_search(arr, 3.5) is None
    assert linear_search(arr, -1) is None
    assert linear_search(arr, 9) is None

def test_binary_search():
    arr = [0,1,2,3,4,5,6,7,8]
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 8) == 8
    assert binary_search(arr, 3.5) is None
    assert binary_search(arr, -1) is None
    assert binary_search(arr, 9) is None
