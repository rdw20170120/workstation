import unittest
from nose.tools import assert_equal
from certtools.couchbase.utils import checks


class TestPlaylsitDelete(unittest.TestCase):

    bucket = "test_bucket"
    key = "test_key"
    response = {
        'status': 'success',
        'metrics': {'resultCount': 0}
    }

    def test_playlist_deleted(self):
        score, msg = checks.ck033(self.response, self.bucket, self.key)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_error_response(self):
        self.response['status'] = 'fatal'
        score, msg = checks.ck033(self.response, self.bucket, self.key)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_incorrect_result_count(self):
        self.response['status'] = 'success'
        self.response['metrics']['resultCount'] = 1
        score, msg = checks.ck033(self.response, self.bucket, self.key)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)


class TestUserprofileDelete(unittest.TestCase):

    bucket = "test_bucket"
    key = "test_key"
    response = {
            'status': 'success',
            'metrics': {'resultCount': 0},
    }

    def test_userprofile_deleted(self):
        score, msg = checks.ck034(self.response, self.bucket, self.key)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)

    def test_with_error_response(self):
        self.response['status'] = 'fatal'
        score, msg = checks.ck034(self.response, self.bucket, self.key)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_incorrect_result_count(self):
        self.response['status'] = 'success'
        self.response['metrics']['resultCount'] = 1
        score, msg = checks.ck034(self.response, self.bucket, self.key)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)
