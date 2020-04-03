
def binary_search(arr, value):
    size = len(arr)
    low = 0
    high = size -1
    while low <= high:
        mid = low + (high - low) / 2
        #print("mid:", mid)
        if arr[mid] == value:
            return True
        else:
            if arr[mid] < value:
                low = mid + 1
            else:
                high = mid -1

    return False

#my_arr = [5, 8, 2, 5, 2, 1, 0, 9, 3]
my_arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(my_arr, 6))














