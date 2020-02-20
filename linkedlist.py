class Node:
    '''
    A node in a LinkedList
    '''

    def __init__(self,x):
        self.x=x
        self.next=None

    def __str__(self):
        return str(self.x)+' -> '

    def verbosestr(self):
        node='+-----+\n'
        node+='|  '+str(self.x)+'  |\n'
        node+='+-----+\n'
        node+='   |\n   |\n   V\n'

        return node

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return  'EMPTY LINKED LIST'
        if self.size()<10:
            ll=''
            node=self.head
            while node:
                ll+=str(node)
                node=node.next
        return ll

    def insert(self,x,i):
        '''
        Insert value x at position i
        '''
        
        if i > self.size():
            print('ERROR: position %d is longer then list length %d' % (i, self.size()))
        if i==self.size():
            self.append(x)
        elif i==0:
            self.prepend(x)
        else:
            pos=0
            node=self.head
            while pos<i-1:
                pos+=1
                node=node.next
            newnode=Node(x)
            newnode.next=node.next
            node.next=newnode

    def prepend(self,x):
        newhead=Node(x)
        newhead.next=self.head
        self.head=newhead

    def append(self,x):
        if self.head==None:
            self.head=Node(x)
            return
        node=self.head
        while node.next:
            node=node.next
        newnode=Node(x)
        node.next=newnode
        return

    def delete(self,x):
        '''
        Deletes first occurence of x
        '''

        if self.head.x==x:
            self.head=self.head.next
            return
        
        node=self.head
        while node.next.x != x:
            node=node.next
        node.next=node.next.next

    def size(self):
        '''
        Traversal to get size?
        '''
        size=0
        
        if self.head:
            size+=1
            node=self.head
            while node.next:
                size+=1
                node=node.next
        return size

