''' generation tests
'''

from project_euler.solution.generation import infinite
from project_euler.solution.generation import pseudo_infinite

terms = 250000

def test_infinite_sum():
    '''Test sum of an infinite sequence (avoid RAM abuse).
    
    NOTE:  This should NOT use up RAM.
    '''
    # TODO:  Figure out how to avoid instantiating the entire list
    # TODO:  Figure out how to test RAM usage
    total = sum(value for value in infinite() if value < terms)
    message = "\nSum of infinite() of about '{0}' terms is '{1}'."
    print((message.format(terms, total)))

def test_pseudo_infinite_sum():
    '''Test sum of a pseudo-infinite sequence (avoid RAM abuse).
    
       NOTE:  This does NOT use up RAM, so it is possible to avoid that usage.
    '''
    # TODO:  Figure out how to avoid instantiating the entire list
    # TODO:  Figure out how to test RAM usage
    total = sum(value for value in pseudo_infinite() if value < terms)
    message = "\nSum of pseudo_infinite() of about '{0}' terms is '{1}'."
    print((message.format(terms, total)))

