# Bubble Sort

def bubbleSort(array):
    i = 0 # iterator
    j = 0 # iterator
    size = len(array) - 1
    for i in range(size): # outer
        for j in range(size - i): # inner
            if array[j] > array[j+1]: # condition
                array[j], array[j+1] = array[j+1], array[j]


arr = [23,43,1,56,34,65,43,99,102,21,19,31,12] # arrray

print("Array before sorting: ")
print(arr)

bubbleSort(arr) # call function

print("Array after sorting")
print(arr)