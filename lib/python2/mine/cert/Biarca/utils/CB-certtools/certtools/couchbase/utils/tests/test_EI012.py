import unittest
from nose.tools import assert_equal
from certtools.couchbase.utils import checks


class TestForUserprofileWithEmail(unittest.TestCase):

    bucket_name = 'test'
    type = 'lookup_by_email'
    username = 'aahingeffeteness42037'
    result = [{bucket_name: {"type": type, "username": username}}]

    def test_with_empty_list(self):
        score, msg = checks.ck043(
            [], self.bucket_name, self.type, self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_empty_dict(self):
        score, msg = checks.ck043(
            {}, self.bucket_name, self.type, self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_for_userprofile(self):
        score, msg = checks.ck043(
            self.result, self.bucket_name, self.type, self.username)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_bucket(self):
        score, msg = checks.ck043(
            self.result, 'wrong_bucket', self.type, self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_type(self):
        score, msg = checks.ck043(
            self.result, self.bucket_name, 'dummy_type', self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_username(self):
        score, msg = checks.ck043(
            self.result, self.bucket_name, self.type, 'dummy_user')
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)


class TestForDocumentResultCountIncludeEmail(unittest.TestCase):

    def test_with_correct_result_count(self):
        score, msg = checks.ck035(1)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_result_count(self):
        score, msg = checks.ck035(2)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)


class TestForUserprofileWithPhone(unittest.TestCase):

    bucket_name = 'test'
    type = 'lookup_by_phone'
    username = 'aahingeffeteness42037'
    result = [{bucket_name: {"type": type, "username": username}}]

    def test_with_empty_list(self):
        score, msg = checks.ck044(
            [], self.bucket_name, self.type, self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_empty_dict(self):
        score, msg = checks.ck044(
            {}, self.bucket_name, self.type, self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_for_userprofile(self):
        score, msg = checks.ck044(
            self.result, self.bucket_name, self.type, self.username)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_bucket(self):
        score, msg = checks.ck044(
            self.result, 'wrong_bucket', self.type, self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_type(self):
        score, msg = checks.ck044(
            self.result, self.bucket_name, 'dummy_type', self.username)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_username(self):
        score, msg = checks.ck044(
            self.result, self.bucket_name, self.type, 'dummy_user')
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)


class TestForDocumentResultCountIncludePhone(unittest.TestCase):

    def test_with_correct_result_count(self):
        score, msg = checks.ck040(1)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_result_count(self):
        score, msg = checks.ck040(2)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)


class TestForDocumentResultCountIncludeAllEmail(unittest.TestCase):

    def test_with_correct_result_count(self):
        score, msg = checks.ck041(49850)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_result_count(self):
        score, msg = checks.ck041(49848)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)


class TestForDocumentResultCountIncludeAllPhone(unittest.TestCase):

    def test_with_correct_result_count(self):
        score, msg = checks.ck042(66618)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_result_count(self):
        score, msg = checks.ck042(66616)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)
