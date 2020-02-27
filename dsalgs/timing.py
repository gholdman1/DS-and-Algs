from copy import deepcopy
from time import process_time_ns
from random import randint
import matplotlib.pyplot as plt
import numpy as np

class Timer:

    def __init__(self,ds):
        '''
        Initialized with a data structure to test

        ds assumed to have the following methods:
        '''
        self.ds=ds
        self.testable_methods = ['insert']
        self.test_results=dict() # Dict to store the results

        # Obtain callable methods of ds
        ds_methods = [ method for method in dir(self.ds) if callable(getattr(self.ds,method))]

        # Find intersection of ds methods and testable methods
        self.test = list(set(self.testable_methods) & set(ds_methods))

    def time_all(self):
        pass
    
    def time_insert(self):
        print('Timing insert')

        self.test_ds=deepcopy(self.ds)

        t0=process_time_ns()
        self.test_results['insert']=[]
        for i in range(1000):
            t1=process_time_ns()
            self.test_ds.insert(randint(0,9))
            t2=process_time_ns()
            self.test_results['insert'].append(t2-t1)

        t1e3=(process_time_ns()-t0)*1e-9
        print('10^3 insertions complete after %d seconds' % (t1e3))

    def view_results(self):

        for test in self.test:
            plt.loglog(self.test_results[test],label=test)

        plt.title('Operation Times')
        plt.xlabel('Keys')
        plt.legend()
        plt.show()
        
