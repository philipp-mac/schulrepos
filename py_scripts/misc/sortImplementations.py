import time

array = [10, 15, 11, 5, 70, 3, 16, 2, 1, 10, 15, 11, 5, 70, 3, 16, 2, 1, 7]
array2 = [10, 15, 11, 5, 70, 3, 16, 2, 1, 10, 15, 11, 5, 70, 3, 16, 2, 1, 7]

def swap(arr, indexA, indexB):
    temp = arr[indexB]
    arr[indexB] = arr[indexA]
    arr[indexA] = temp

def bubbleSort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if (array[i] < array[i - 1]):
                swap(array, i, i - 1)
                swapped = True 
                
                
def insertionSort(array):
    newArray = []
    lengthToReach = len(array)
    while len(newArray) != lengthToReach:
        min = array[0]
        for i in range(len(array)):
            if (array[i] < min):
                min = array[i]
        newArray.append(min)
        array.remove(min)
    
    return newArray
            
        
print("starting bubble sort on" , array)
bubbleSortTime = time.perf_counter()
bubbleSort(array)
bubbleSortEnd = time.perf_counter()
bubbleSortDuration = bubbleSortTime - bubbleSortEnd
print(array)

print("starting insertion sort on ", array2)
insertionSortTime = time.perf_counter()
print(insertionSort(array2))
insertionSortEnd = time.perf_counter()
insertionSortDuration = insertionSortTime - insertionSortEnd


print("bubble sort = ", bubbleSortTime, " insertion sort = ", insertionSortTime)