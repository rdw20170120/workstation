import nose.tools

'''
def setup_func():
    print 'setup...'

def teardown_func():
    print 'teardown...'

# TODO: FIX: why is 'with_setup" raising a NameError?
#@with_setup(setup_func, teardown_func)
def check_even(a, b):
    assert a % 2 == 0 or b % 2 == 0

# TODO: FIX: why is 'with_setup" raising a NameError?
#@with_setup(setup_func, teardown_func)
def test_as_function():
    pass

def test_evens():
    for i in range(0, 5):
        yield check_even, i, i * 3
'''

class TestNose(object):
    def test_nothing(self):
        pass

    def test_assert_almost_equal(self):
        #assert_almost_equal(first, second, places, msg)
        pass

    def test_assert_almost_equals(self):
        #assert_almost_equals(first, second, places, msg)
        pass

    def test_assert_equal(self):
        #assert_equal(first, second, msg)
        pass

    def test_assert_equals(self):
        #assert_equals(first, second, msg)
        pass

    def test_assert_false(self):
        #assert_false(expr, msg)
        pass

    def test_assert_not_almost_equal(self):
        #assert_not_almost_equal(first, second, places, msg)
        pass

    def test_assert_not_almost_equals(self):
        #assert_not_almost_equals(first, second, places, msg)
        pass

    def test_assert_not_equal(self):
        #assert_not_equal(first, second, msg)
        pass

    def test_assert_not_equals(self):
        #assert_not_equals(first, second, msg)
        pass

    def test_assert_true(self):
        #assert_true(expr, msg)
        pass

    def test_eq_(self):
        #eq_(first, second, msg)
        pass

    def test_ok_(self):
        #ok_(expr, msg=None)
        pass

'''
nose.tools stuff to try:

assert_raises(excClass, callableObj, *args, **kwargs)
@istest
@make_decorator(func)
@nottest
@raises(*exceptions)
set_trace()
@timed(limit)
'''
