'''Blood Testing Problem
Chapter 15 of Nahin "Will You Be Alive..."
What's the optimum number (k) in a group of
patients tested for a disease to minimize the
number of tests needed?
July 13, 2018'''

import random

p = 0.01 #probability of infection
POPN = 10000 #total population of Patients
#k = 3 #grouping amount

class Patient(object):
    def __init__(self):
        if random.random() <= p:
            self.infected = True
        else:
            self.infected = False

class Test(object):
    def __init__(self,k):
        '''groups Patients into groups of k each'''
        self.groups = []
        self.k = k
        num = 0
        while num < POPN:
            self.groups.append([Patient().infected for i in range(self.k)])
            num += self.k

    def round(self):
        '''Round of tests
        returns the number of tests needed
        for a given k'''
        #k = 3
        
        tests = 0
        for group in self.groups:
            tests += 1 #you had to test this group
            if True in group:
                tests += self.k
        return tests

for k in range(2,31):
    testing = [Test(k).round() for i in range(5000)]
    print("k:",k,sum(testing)/len(testing))
    
    

#print(mytest.groups)
#print("Total tests:",tests)

    
