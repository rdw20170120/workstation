import os
import unittest
from nose.tools import assert_equal
from certtools.couchbase.utils import checks


class TestFileExists(unittest.TestCase):
    def setUp(self):
        print '==========================================='
        print 'Test Case-1 : Testing for existence of file'
        print '==========================================='
        self.test_file = os.path.join(
            os.getenv("HOME"), "test_EI000.txt"
        )
        with open(self.test_file, "w") as file_ob:
            file_ob.write('EI000')
            print 'Test file created in setup - {0}'.format(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            print 'Test file deleted in teardown - {0}'.format(self.test_file)
            print

    def test_file_exist(self):
        score, msg = checks.ck000(self.test_file)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)


class TestFileNotExists(unittest.TestCase):
    def setUp(self):
        print
        print '==============================================='
        print 'Test Case-2 : Testing for non-existence of file'
        print '==============================================='
        self.test_file = os.path.join(
             os.getenv("HOME"), "test_EI000.txt"
        )

    def tearDown(self):
        pass

    def test_file_not_exist(self):
        score, msg = checks.ck000(self.test_file)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)
        print
