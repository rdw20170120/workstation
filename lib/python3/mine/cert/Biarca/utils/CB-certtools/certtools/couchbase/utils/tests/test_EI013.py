import unittest
from requests.models import Response
from nose.tools import assert_equal
from certtools.couchbase.utils import checks


class TestForUserprofile(unittest.TestCase):
    bucket_name = 'test'
    old_key = 'aahingheadwaiter24314'
    result = [{"test": {"username": "aahingheadwaiter24314"}}]

    def test_with_empty_list(self):
        score, msg = checks.ck032([], self.bucket_name, self.old_key)
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))

    def test_with_empty_dict(self):
        score, msg = checks.ck032({}, self.bucket_name, self.old_key)
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))

    def test_for_userprofile(self):
        score, msg = checks.ck032(self.result, self.bucket_name, self.old_key)
        assert_equal(score, 1)
        print('Check score: {0}'.format(score))

    def test_with_wrong_bucket(self):
        score, msg = checks.ck032(self.result, 'wrong_bucket', self.old_key)
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))

    def test_with_wrong_oldkey(self):
        score, msg = checks.ck032(self.result, self.bucket_name,
                                  'aahingheadwaiter')
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))


class TestForUserprofileInsert(unittest.TestCase):
    bucket_name = 'test'
    new_key = 'aanewkey'
    old_key = 'aahingeffeteness42037'
    result = '{"results": [{"test": {"username": "aahingeffeteness42037"}}],"status": "success"}'
    resp_obj = Response()

    def setUp(self):
        self.resp_obj.status_code = 200
        self.resp_obj._content = self.result

    def test_userprofile_insert(self):
        score, msg = checks.ck037(self.resp_obj, self.new_key,
                                  self.old_key, self.bucket_name)
        assert_equal(score, 1)
        print('Check score: {0}'.format(score))

    def test_userprofile_wrong_old_key(self):
        score, msg = checks.ck037(self.resp_obj, self.new_key, 'wrongkey',
                                  self.bucket_name)
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))

    def test_userprofile_wrong_bucket(self):
        score, msg = checks.ck037(self.resp_obj, self.new_key, self.old_key,
                                  'wrongbucket')
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))


class TestForUserprofileUpdate(unittest.TestCase):
    new_resp = Response()
    old_resp = Response()
    new_key = 'aanewkey'
    expected_new = '{"metrics": {"resultCount": 4}}'
    expected_old = '{"metrics": {"resultCount": 0}}'

    def setUp(self):
        self.new_resp.status_code = 200
        self.new_resp._content = self.expected_new
        self.old_resp.status_code = 200
        self.old_resp._content = self.expected_old

    def test_userprofile_update(self):
        score, msg = checks.ck039(self.old_resp, self.new_resp, self.new_key)
        assert_equal(score, 1)
        print('Check score: {0}'.format(score))


class TestForUserprofileDelete(unittest.TestCase):
    response = Response()
    wrong_resultcount = Response()
    wrong_status = Response()
    old_key = 'aahingheadwaiter24314'
    expected_resp = '{"status": "success","metrics": {"resultSize": 0}}'
    wrong_rescount = '{"status": "success","metrics": {"resultSize": 1}}'
    wrong_sts = '{"status": "fatal","metrics": {"resultSize": 0}}'

    def setUp(self):
        self.response.status_code = 200
        self.response._content = self.expected_resp
        self.wrong_resultcount.status_code = 200
        self.wrong_resultcount._content = self.wrong_rescount
        self.wrong_status.status_code = 200
        self.wrong_status._content = self.wrong_sts

    def test_userprofile_delete(self):
        score, msg = checks.ck038(self.response, self.old_key)
        assert_equal(score, 1)
        print('Check score: {0}'.format(score))

    def test_userprofile_delete_wrong_resultcount(self):
        score, msg = checks.ck038(self.wrong_resultcount, self.old_key)
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))

    def test_userprofile_delete_wrong_status(self):
        score, msg = checks.ck038(self.wrong_status, self.old_key)
        assert_equal(score, 0)
        print('Check score: {0}'.format(score))
