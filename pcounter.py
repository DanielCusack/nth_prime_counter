#!/usr/bin/env python3
import math
import numpy as np


class Prime_Finder:
    '''
    Class to find the nth prime number where n is an interger
    '''
    def __init__(self, n):
        self.n = n
        self.num = 0 #To be determined
        if self.n < 6:
            self.upper_limit = 11
        else:
            #This estimate does not work for n < 6
            self.upper_limit = int(self.n*(math.log(self.n) + math.log(math.log(self.n))))
        self.range = int(math.ceil(math.sqrt(self.upper_limit))) + 1
        self.number_list = np.arange(2, self.upper_limit + 1, dtype = int)
        self.prime_mask = np.ones(self.upper_limit, dtype = int)
        self.len = len(self.number_list)
        self.find_nth_prime()

    def sieve(self):
        '''
        A sieve of Eratosthenes to find prime numbers up to self.upper_limit.
        '''
        #Mark all even numbers except 2 as not primes
        for index in range(2, self.len, 2):
            self.prime_mask[index] = 0
        for index in range(1, self.range):
            if self.prime_mask[index]:
                start = index + self.number_list[index]
                for jndex in range(start, self.len, self.number_list[index]):
                    self.prime_mask[jndex] = 0

    def get_prime(self):
        '''
        Get the self.nth prime number from self.number_list 
        '''
        prime_count = 0
        for index in range(self.len):
            if self.prime_mask[index] == 1:
                prime_count +=1
            if prime_count == self.n:
                self.num = self.number_list[index]
                break
    def find_nth_prime(self):
        self.sieve()
        self.get_prime()


if __name__ == '__main__':
    n = None
    while type(n) != int: 
        n = input('Please enter the nth prime number up to 10000000 you would like to find : ')
        try:
            n = int(n)
            if n > 10000000 or n < 1:
                n = None
                raise ValueError
        except ValueError:
            print('That is not valid input.')
    prime = Prime_Finder(int(n))
    print('Prime number {0} is {1}.'.format(n, prime.num))

