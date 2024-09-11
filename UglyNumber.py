'''
An ugly number is a number whose prime factors are only 2,3, or 5. 
This program returns the nth ugly number provided.
'''
#Helper function that divides a number a by b until it can no longer be divided in such a way.

class Solution(object):
    def divideFull(self, a, b):
        while a % b == 0:
            a = a/b
        return a

#checkForUgliness is used to check if a given number is ugly and can run independently of nthUglyNumber

    def checkForUgliness(self, n):
        n = self.divideFull(n,2)
        n = self.divideFull(n,3)
        n = self.divideFull(n,5)
        return 1 if n == 1 else 0
    
#nthUglyNumber takes a number n and returns its corresponding ugly number in the ugly number sequence.
       
    def nthUglyNumber(self, n):
        i, count = 1, 1
        while n > count:
            i += 1
            if self.checkForUgliness(i):
                count += 1
        return i