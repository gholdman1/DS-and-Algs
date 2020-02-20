# Sorting algorithms

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
