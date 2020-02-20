class HashTable:

    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size

    def __str__(self):
        table=''
        if self.size<15:
            for i in range(self.size):
                entry=''
                if self.table[i]:entry=self.table[i]
                table+='----\n'
                table+=str(entry)
                table+='\n'
            table+='----'
        return table

    def __repr__(self):
        return self.__str__()

    def insert(self,x):
        index=self.hash(x)
        self.table[index]=x
    
    def hash(self,x):
        return x % self.size
