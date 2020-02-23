###############################
# SORTING ALGORITHMS
# Algorithms sorted by time complexity
# (dictionary sorting of (WORST, AVE, BEST))
############################

## Useful functions
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

    return arr

## O(n^2)

# Selection Sort

def selectionsort(arr):
    '''
    Partition array into an unsorted and sorted portion.
    Find smallest value in unsorted portion and place at end of sorted.

    Time complexity:    
    '''
    n=len(arr)
    for i in range(n):
        # Find index of minimum
        minidx=i
        for j in range(i,n):
            if arr[j]<arr[minidx]:
                minidx=j

        swap(arr,minidx,i)

    return arr
    
# Bubble Sort

def bubblesort(arr):
    '''
    Time complexity:    O(n^2) Backwards, so every key is compared to every other key.
                        O(n^2) On average, ???
    Space complexity:   O(1)
                        ???
    '''
    n=len(arr)
    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:
                arr=swap(arr,j,j+1)

    return arr

# Insertion Sort


## O(n log(n))


# Merge sort
def merge(L,R):

    i=0
    j=0

    arr=[]
    while i < len(L) and j < len(R):
        if L[i]<=R[j]:
            arr.append(L[i])
            i+=1
        else:
            arr.append(R[j])
            j+=1
   
    while i < len(L):
        arr.append(L[i])
        i+=1
    while j < len(R):
        arr.append(R[j])
        j+=1

    return arr

def mergesort(arr):

    if len(arr)>1:
        m = int( len(arr)/2 )

        L = arr[0:m]
        R = arr[m:len(arr)]

        L=mergesort(L)
        R=mergesort(R)

        arr=merge(L,R)

    return arr

# Quicksort

def partition(arr):
    
    pivot=arr[-1]

    i=-1
    for j in range(len(arr)-1):
        if arr[j]<=pivot:
            i+=1
            arr=swap(arr,i,j)
    arr=swap(arr,i+1,len(arr)-1)
    
    return arr, i+1

def quicksort(arr):

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

def insertionsort(arr):

    pass

def timsort(arr):
    '''
    Based upon insertionsort and mergesort
    '''

    pass

def selectionsort(arr):
    '''
    Similar to insertionsort.
    '''

    pass

def heapsort(arr):
    '''
    An improved version of selectionsort. Utilizes a heap to find largest element
    '''
    pass
