###############################
# SORTING ALGORITHMS
# Algorithms sorted by time complexity
# (dictionary sorting of (WORST, AVE, BEST))
############################

## Imports

from dsalgs.utilities import swap, merge, partition
from dsalgs.heap import Heap

# Selection Sort

def selectionsort(arr):
    '''
    Partition array into an unsorted and sorted portion.
    Find smallest value in unsorted portion and place at end of sorted.

    Time complexity:    O(n^2), for all cases
                        O(n^2)
                        O(n^2)
    Space complexity:   O(1)

    Use case:           n<100 since it's slow but simple.
                        Probably would use insertionsort instead though.
    '''
    n=len(arr)

    for i in range(n):
        # Find index of minimum
        minidx=i
        for j in range(i+1,n):
            if arr[j]<arr[minidx]:
                minidx=j

        arr=swap(arr,minidx,i)

    return arr

# Insertion Sort

def insertionsort(arr):
    '''
    Partition array into an unsorted and sorted portion.
    Take first value in unsorted portion,and move it to lower indices
    until it is smaller than the value above it.

    Time complexity:    O(n^2), array is reversed
                        O(n^2),
                        O(n)  , array is in order
    Space complexity:   O(1)

    Use case:           n<100 since it's slow but simple
    '''
    n = len(arr)

    for i in range(1,n):
        j=i

        while j>0 and arr[j]<arr[j-1]:
            swap(arr,j,j-1)
            j-=1

    return arr

# Bubble Sort

def bubblesort(arr):
    '''
    Time complexity:    O(n^2) Backwards, so every key is compared to every other key.
                        O(n^2) On average, 50/50 chance of two elements being out of order
                        O(n), already sorted
    Space complexity:   O(1), only reading two values at a time
    '''
    n=len(arr)
    for i in range(n):
        swapped=False

        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:
                arr=swap(arr,j,j+1)
                swapped=True

        # Stop sorting if nothing was swapped
        if swapped==False:
            break

    return arr


# Quicksort

def quicksort(arr):
    '''


    Time complexity:    O(n^2), if 
                        O(n log(n)) on average
                        O(n log(n)) at best
    '''

    if len(arr)>1:
        arr, i = partition(arr)

        if i == 0:
            arr1=[]
        else:
            arr1=quicksort(arr[:i])
        if i == len(arr)-1:
            arr2=[]
        else:
            arr2=quicksort(arr[i+1:])
        arr=arr1+[arr[i]]+arr2

    return arr

# Merge sort

def mergesort(arr):
    '''
    Split the array in half and perform mergesort on each half.
    Then merge the two sorted halves together.

    Time complexity:    O(n log(n)), merging takes O(n) comparisons
                        while we have roughly O(log n) merges. Linear
                        work is done at each level.

    Note that mergesort is Omega(n log(n)).
    '''

    if len(arr)>1:
        m = int( len(arr)/2 )

        L = arr[0:m]
        R = arr[m:len(arr)]

        L=mergesort(L)
        R=mergesort(R)

        arr=merge(L,R)

    return arr


def heapsort(arr):
    '''
    An improved version of selectionsort. Utilizes a heap to find largest element
    '''
    n=len(arr)
    h=Heap(n)

    h.make_heap(arr)

    for i in range(n):
        arr[i]=h.extract_min()

    return arr

def timsort(arr):
    '''
    Based upon insertionsort and mergesort
    '''

    pass

def pigeonholesort(arr):
    '''
    

    Reference:
        https://en.wikipedia.org/wiki/Pigeonhole_sort
    '''

    mi = min(arr) # Minimum value of arr
    ma = max(arr)

    size=ma-mi+1

    buckets=[0]*size

    # Count number of each possible key
    for i in range(len(arr)):
        x=arr[i]
        buckets[x-mi]+=1

    i=0
    # Iterate over buckets
    for j in range(size):
        # Place all keys in this bucket back into arr
        while buckets[j]>0:
            buckets[j]-=1
            arr[i]=j+mi
            i+=1

    return arr