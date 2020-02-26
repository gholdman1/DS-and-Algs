from dsalgs import linkedlist

class HashTable:

    def __init__(self,slots,collisionhandling='chaining'):
        self.slots=slots
        self.table=[None]*self.slots

        if collisionhandling=='chaining':
            self.insert=self.insertnode
            self.delete=self.deletenode
            self.search=self.searchnode

        if collisionhandling=='openaddressing':
            self.insert=self.insertopen
        self.collisionhandling=collisionhandling
    
    def __str__(self):
        table=''
        linebreak='-----\n'
        if self.slots<15:
            for i in range(self.slots):
                entry=''
                if self.table[i]:entry=self.table[i]
                table+=linebreak
                table+=str(entry)
                table+='\n'
            table+=linebreak
        return table

    def __repr__(self):
        return self.__str__()


    # Chaining methods

    def insertnode(self,x):
        index=self.hash(x)
        if not self.table[index]:
            self.table[index]=linkedlist.LinkedList()
        self.table[index].append(x)

    def deletenode(self,x):
        '''
        Delete first occurence of x
        '''
        index=self.hash(x)
        if self.table[index]:
            self.table[index].delete(x)

    def searchnode(self,x):
        '''
        Returns position of first instance of x
        '''
        index=self.hash(x)

        if not self.table[index]:
            return (index,None)

        llindex=self.table[index].search(x)
        return (index,llindex)

    # Open Addressing Methods

    def insertopen(self,x):
        # Ensure table is not full

        if self.loadfactor()==1:
            return

        index=self.hash(x)

        while self.table[index]:
            index+=1
            if index==self.slots:
                index=0
        self.table[index]=x

    # Basic information about table
    def loadfactor(self):
        return self.get_keys()/self.slots

    def get_keys(self):
        '''
        Returns number of keys
        '''
        nkeys=0
        for i in range(self.slots):
            if self.table[i]:
                if self.collisionhandling=='chaining':
                    nkeys+=self.table[i].size()
                if self.collisionhandling=='openaddressing':
                    nkeys+=1

        return nkeys

    def hash(self,x):
        return x % self.slots

    def get_size(self):
        '''
        Returns the size of the table
        '''
        return self.slots


