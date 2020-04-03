

def rotate_array(arr, k):
    n = len(arr)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)
    reverse_array(arr, 0, n - 1)

def reverse_array(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    #print("arr:", arr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
rotate_array(arr, 6)
print(arr)








