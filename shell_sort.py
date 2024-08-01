def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
            print(array)
        interval //= 2
data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
size = len(data)
shellSort(data, size)
print(data)
# https://www.programiz.com/dsa/shell-sort
# sorting subarrays of elements at specific intervals
# as it progresses the intervals decrease, its then partially sorted
# At some point a final pass with an interval of 1 results in a fully sorted array 