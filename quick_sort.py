# 1. The partition function takes the last element as the pivot and places the pivot element at its correct position in the sorted array. All the elements are re-arranged based on the pivot element.
# 2. The partition function returns the index of the pivot element in the array.
# 3. The quick_sort function calls itself recursively twice to sort the two halves of the array.
# 4. The low and high variables are used to keep track of the start and end of the array.
# 5. The pivot element is placed at its correct position in the array.
# 6. The array is sorted recursively twice.

# Time Complexity: O(n^2)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low == high:
        return 1

    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


x = [12, 43, 2, 9, 32, 87, 43, 21, 27, 1, 39]
quick_sort(x, 0, len(x)-1)

for z in range(len(x)):
    print("{}, ".format(x[z]), end='')
