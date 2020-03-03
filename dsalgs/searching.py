def binarysearch(arr,x,i,j):

    if len(arr)==0:
        return -1

    if i==j and arr[i]!=x:
        return -1

    if i==j and arr[i]==x:
        return i

    mid = int((i+j)/2)

    if x <= arr[mid]:
        idx = binarysearch(arr,x,i,mid)
    elif x>arr[mid]:
        idx = binarysearch(arr,x,mid+1,j)

    return idx