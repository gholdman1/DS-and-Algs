from copy import deepcopy
from time import process_time
from random import randint
import matplotlib.pyplot as plt

class Timer:

    def __init__(self,ds):
        '''
        Initialized with a data structure to test

        ds assumed to have the following methods:
        '''
        self.ds=ds
        self.testable_methods = ['insert']

        # Obtain callable methods of ds
        ds_methods = [ method for method in dir(self.ds) if callable(getattr(self.ds,method))]

        # Find intersection of ds methods and testable methods
        self.test = list(set(self.testable_methods) & set(ds_methods))

    def test_all(self):
        pass
    
    def test_insert(self):

        self.test_ds=deepcopy(self.ds)

        t=[]
        for i in range(20000):
            t1=process_time()
            self.test_ds.insert(randint(0,9))
            t2=process_time()
            t.append(t2-t1)

        plt.plot(t)
        plt.show()

    def results(self):

        pass
