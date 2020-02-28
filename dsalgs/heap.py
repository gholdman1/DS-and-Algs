from dsalgs.utilities import swap
from math import log, ceil

class Heap:
    '''
    A special ordering of an array in which index k has a left child at 2k and a right child at 2k+1
    Often used to implement a priority queue.
    '''

    def __init__(self,size ):

        self.head=None
        self.size=2**(ceil(log(size,2)))
        self.arr=[None]*self.size

    def parent(self,k):
        '''
        Index of parent of index k
        '''
        if k==0:
            return 0
        return int((k-1)/2)

    def __str__(self):

        return str(self.arr)

        strlevel=[]
        h=self.height()

        pair=lambda x,y: (' / \\ \n'+str(x)+'  '+str(y))

        for l in range(h):
            strlevel[h-l-1]

    def make_heap(self,arr,speed='slow'):

        if speed=='slow':
            for i in range(len(arr)):
                self.insert(arr[i])

    def sub_heap(self,k):
        '''
        Returns the subheap starting at index k
        '''

        pass

    def height(self):
        n=self.get_keys()

        if n==0:
            return 0

        return int(log(n,2))+1

    def get_keys(self):
        nkeys=0

        while nkeys < self.size and self.arr[nkeys] != None:
            nkeys+=1
        return nkeys

    def get_size(self):
        return self.size
        
    def insert(self,x):

        if self.get_keys() == self.size:
            print('WARNING: Overflow')
            return
        else:
            k=self.get_keys()
            self.arr[k]=x
            self.bubble_up(k)

    def bubble_up(self,k):

        if k == 0:
            return

        if self.arr[self.parent(k)] > self.arr[k]:
            self.arr=swap(self.arr,self.parent(k),k)
            self.bubble_up(self.parent(k))

    def bubble_down(self,k):
        c = 2*k # Child index
        min_idx=k

        for i in range(2):
            if (c+i) <= self.get_keys()-1: # Check still in heap
                if self.arr[min_idx] > self.arr[c+i]: # if current value larger than child
                    min_idx = c+i

        # If found one smaller
        if min_idx != k:
            self.arr=swap(self.arr,k,min_idx) # Swap them
            self.bubble_down(min_idx) # Then bubble_down same value at new index

    def extract_min(self):
        '''
        Pop largest value and restore the heap
        '''

        min_val=self.arr[0]

        self.arr[0] = self.arr[self.get_keys()-1]
        self.arr[self.get_keys()-1]=None
        self.bubble_down(0)

        return min_val
    def search(self,x):
        '''
        Returns index of value x by performing linear search
        '''
        for i in range(len(self.arr)):
            if self.arr[i] == x:
                return i