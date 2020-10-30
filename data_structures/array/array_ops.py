"""
An array is a collection of items stored at contiguous memory locations.
The idea is to store multiple items of the same type together.
This makes it easier to calculate the position of each element by simply
adding an offset to a base value

Array can be handled in python by module named "array".
    1. array.array(type, value) - create an array with data type and value list
    2. array.append(item) -  add the value at the end of the array.
    3. array.insert(pos, item) -  add the value at the position
    4. array.pop(pos) - remove the item at the position and return it
    5. array.remove(item) - remove the first occurrence
    6. array.index(item) - return the index of the first occurrence
    7. array.reverse() - reverse the array
Reference: https://docs.python.org/3/library/array.html#module-array
"""


import array

_created = "2020-03-30"

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

# using append() to insert new value at end
arr.append(4)

# printing appended array
print("The appended array is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")
print("\r")

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

# printing array after insertion
print("The array after insertion is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")
print("\r")

# using pop() to remove element at 2nd position
print("The popped element is : ", end="")
print(arr.pop(2))

# printing array after popping
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")
print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

# using index() to print index of 1st occurrenece of 2
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(3))

# using reverse() to reverse the array
arr.reverse()

# printing array after reversing
print("The array after reversing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

# using typecode to print datatype of array
print("The datatype of array is : ", end="")
print(arr.typecode)

# using itemsize to print itemsize of single array element
print("The itemsize of array is : ", end="")
print(arr.itemsize)

# using buffer_info() to print buffer info. of array
# address in which array is stored and number of elements in it.
print("The buffer info. of array is : ", end="")
print(arr.buffer_info())

# initializing array 2 with array values
# initializes array with signed integers
arr2 = array.array('i', [1, 2, 3])

# using extend() to add array 2 elements to array 1
arr.extend(arr2)

# printing array after extending
print("The modified array is : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print('\r')

# using count() to count occurrences of 1 in array
print("The occurrences of 2 in array is : ", end="")
print(arr.count(2))

# initializing list
li = [5, 6, 7]

# using fromlist() to append list at end of array
arr.fromlist(li)

# printing the modified array
print("The modified array is : ", end="")
for i in range(0, 9):
    print(arr[i], end=" ")
print("\r")

# using tolist() to convert array into list
li2 = arr.tolist()

# printing the new list
print("The new list created is : ", end="")
for i in range(0, len(li2)):
    print(li2[i], end=" ")
