# Sorting algorithms



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
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

    return arr

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

def bubblesort(arr):
    n=len(arr)
    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:
                arr=swap(arr,j,j+1)

    return arr
