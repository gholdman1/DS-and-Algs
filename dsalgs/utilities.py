## Useful functions
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

    return arr

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

def partition(arr):
    
    pivot=arr[-1]

    i=-1
    for j in range(len(arr)-1):
        if arr[j]<=pivot:
            i+=1 # Found another smaller than pivot
            arr=swap(arr,i,j)
    arr=swap(arr,i+1,len(arr)-1)
    
    return arr, i+1