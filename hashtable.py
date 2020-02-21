from dsalgs import linkedlist

class HashTable:

    def __init__(self,slots,collisionhandling='chaining'):
        self.slots=slots
        self.table=[None]*self.slots

        if collisionhandling=='chaining':
            self.insert=self.insertnode
            self.delete=self.deletenode
            self.search=self.searchnode

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

    # Basic information about table
    def loadfactor(self):
        return self.keys()/self.slots

    def keys(self):
        '''
        Returns number of keys
        '''
        nkeys=0
        for i in range(self.slots):
            if self.table[i]:
                nkeys+=self.table[i].size()

        return nkeys

    def hash(self,x):
        return x % self.slots


