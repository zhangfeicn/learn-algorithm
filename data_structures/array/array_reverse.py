"""
function reverse(arr[])  \n
for example:
    Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
    Output : arr[] = [7, 6, 5, 4, 3, 2, 1]
"""

import array

_created = "2020-04-01"


def reverse1(arr):
    """
    Swap between i and n-i until the middle
    """
    start = 0
    end = len(arr)
    reverse_start_end(arr, start, end)


def reverse_start_end(arr, start, end):
    """
    reverse the elements from start to end \n
    swap between i and n-i until the middle
    """
    while start < end - 1:
        arr[start], arr[end - 1] = arr[end - 1], arr[start]
        start += 1
        end -= 1


def _main(reverse_method):
    print("Reverse", reverse_method.__name__, "Demonstration:")
    # initializing array with array values
    arr = array.array('i', [1, 2, 3, 4, 5, 6])

    # printing original array
    print("The new created array is : ", end="")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    print("\r")

    # reverse the arr
    reverse_method(arr)
    print("After reverse, the updated array is : ", end="")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    print("\r")


if __name__ == "__main__":
    _main(reverse1)
