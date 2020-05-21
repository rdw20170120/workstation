''' Project Euler Problem 2 solution elements'''

from project_euler.solution.generation import pseudo_infinite

class P002(object):
    '''Provide the solution for Project Euler Problem 2.'''
    def cache_size(self):
        '''Return the size of the cache.'''
        return len(self._cache)

    def fibonacci_term(self, index):
        '''Return "index"th term of the Fibonacci sequence.

           By definition, fibonacci_term(1) == 1 and fibonacci_term(2) = 2,
           so extend to fibonacci_term(0) == 1 for completeness.

           Recursive implementation is simple and effective, but not efficient.

           Cacheing makes recursion more feasible.
        '''
        if 0 > index:
            raise IndexError(
                "Index '{0}' is below zero, therefore invalid!".format(index)
            )
        if not index in self._cache:
            self._cache[index] = (
                self.fibonacci_term(index - 1) + self.fibonacci_term(index - 2)
            )
        return self._cache[index]

    def fibonacci(self, count=None):
        '''Return the first "count" terms of the Fibonacci sequence.
        
           If count is None, return an "infinite" Fibonacci sequence.
        '''
        if count is None:
            return (self.fibonacci_term(i) for i in pseudo_infinite(1))
        else:
            return (self.fibonacci_term(i) for i in range(1, count + 1))

    def fibonacci_below(self, limit):
        '''Return the first terms of the Fibonacci sequence below "limit".
        
           Use the non-generator algorithm.
        '''
        return (value for value in self.fibonacci() if value < limit)

    def __init__(self):
        self._cache = {0:1, 1:1}

    # def fibonacci_generator(self):
    #     '''Return the terms of the Fibonacci sequence.
    #     
    #        Use a generator to produce the infinite sequence, avoid RAM abuse.
    #     '''
    #     prv, nxt = 1, 1
    #     while 1:
    #         print "Yielding {0}...".format(prv)
    #         yield prv
    #         prv, nxt = nxt, prv + nxt

    # def fibonacci_below_via_generator(self, limit):
    #     '''Return the first terms of the Fibonacci sequence below "limit".
    #     
    #        Use the generator algorithm.
    #     '''
    #     return (value for value in fibonacci_generator() if value < limit)
