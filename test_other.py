from other import search_sum

def test_search_sum():
    arr = [1,3,5,7,9,11,15,14,12,10,8]
    assert search_sum(arr, 4) == (0,1)
    assert search_sum(arr, 1) is None
    assert search_sum(arr, 9) == (0,10)
    # return the first of multiple possible combinations 
    assert search_sum(arr, 18) == (1,6)
