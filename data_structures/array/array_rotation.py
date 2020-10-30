"""
reference: https://www.geeksforgeeks.org/array-rotation/  \n
function rotate(arr[], d, n) that rotates arr[] of size n by d elements. \n
for example:
    Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
             d = 2
    Output : arr[] = [3, 4, 5, 6, 7, 1, 2]
"""

import array
import math
from array_reverse import reverse_start_end

_created = "2020-03-31"


def left_rotate1(arr, d):
    """
    Function to left rotate arr[] of size n by d \n
    Algorithm: Using temp arrry to store the rotated values. \n
    Time complexity: O(n)
    """
    # init temp array
    temp = array.array(arr.typecode)
    n = len(arr)
    # move the rotate elements to the temp array
    for i in range(d):
        temp.append(arr[i])
    # shift the rest of the arr
    for i in range(n - d):
        arr[i] = arr[i + d]
    # store back the d elements to arr
    for i in range(d):
        arr[n+i-d] = temp[i]


def left_rotate2(arr, d):
    """
    Function to left rotate arr[] of size n by d \n
    Algorithm: Using temp arrry to store the rotated values. \n
    Time complexity: O(n)
    """
    # init temp array
    temp = array.array(arr.typecode)

    # pop the value from original array
    for i in range(d):
        temp.append(arr.pop(0))

    # extend the temp array to the original array
    arr.extend(temp)


def left_rotate3(arr, d):
    """
    Function to left rotate arr[] of size n by d \n
    Algorithm: Rotate one by one.  Repeat the steps. \n
    Time complexity: O(n*d)
    """
    n = len(arr)
    for i in range(d):
        _left_rotate_by_one(arr, n)


def left_rotate4(arr, d):
    """
    Function to left rotate arr[] of size n by d \n
    Algorithm: Enhancing moving one by one. Divide the array in different sets
    where number of sets is equal to GCD of n and d. Move the elememnts within
    sets.  \n
    Example: arr[] = [1, 2, 3, 4, 5, 6]
                => [3, 2, 5, 4, 1, 6]
                => [3, 4, 5, 6, 1, 2]
    Time complexity: O(n)
    """
    n = len(arr)
    g_c_d = math.gcd(n, d)
    for i in range(g_c_d):
        # moving i-th values of blocks
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def left_rotate5(arr, d):
    """
    Function to left rotate arr[] of size n by d \n
    Algorithm:
        reverse(arr, 0, d)
        reverse(arr, d, n)
        reverse(arr, 0, n)
    Time complexity: O(n)
    """
    n = len(arr)
    reverse_start_end(arr, 0, d)
    reverse_start_end(arr, d, n)
    reverse_start_end(arr, 0, n)


def left_rotate6(arr, d):
    """
    Function to left rotate arr[] of size n by d \n
    Algorithm:   \n
    Initialize A = arr[0..d-1] and B = arr[d..n-1]
    1) Do following until size of A is equal to size of B
        a) If A is shorter, divide B into Bl and Br such that Br is of same
            length as A. Swap A and Br to change ABlBr into BrBlA. Now A
            is at its final place, so recur on pieces of B.
        b) If A is longer, divide A into Al and Ar such that Al is of same
            length as B Swap Al and B to change AlArB into BArAl. Now B
            is at its final place, so recur on pieces of A.
    2) Finally when A and B are of equal size, block swap them.
    Time complexity: O(n)
    """
    pass


def _left_rotate_by_one(arr, n):
    """
    Store arr[0] in a temporary variable temp. \n
    Move arr[i] to arr[i-1], and finally temp to arr[n-1]. \n
    Example: arr[] = [1, 2, 3, 4] => [2, 3, 4, 1]
    """
    temp = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n-1] = temp


def _main(rotate_method):
    print("Rotate", rotate_method.__name__, "Demonstration:")
    # initializing array with array values
    arr = array.array('i', [1, 2, 3, 4, 5, 6])

    # printing original array
    print("The new created array is : ", end="")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    print("\r")

    # rotate the arr
    rotate_method(arr, 4)
    print("After rotate 4, the rotated array is : ", end="")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    print("\r")


if __name__ == "__main__":
    _main(left_rotate1)
    _main(left_rotate2)
    _main(left_rotate3)
    _main(left_rotate4)
    _main(left_rotate5)
