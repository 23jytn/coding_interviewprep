# A program to do a binary search of an element in array

array = [2,3,6,8,9,11,14,17,23,26,27,29,39,48,49,51,54,59,60,66,77,89]
x = 14
def binary_search(array,x):
    start = 0
    end = len(array)-1
    while ( start <= end ):
        mid = ( start + end ) // 2
        if array[mid] == x :
            return mid
        elif array[mid] < x :
            start = mid + 1
        else :
            end = mid - 1
    return -1

print binary_search(array,x)
print array.index(x)
