import unittest
from nose.tools import assert_equal
from certtools.couchbase.utils import checks


class TestTroubleShoot(unittest.TestCase):

    def test_with_empty_list(self):
        score, msg = checks.ck036([], 'DummyFile.txt')
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_empty_dict(self):
        score, msg = checks.ck036({}, 'DummyFile.txt')
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_error_code(self):
        result = [{'code': 4000}]
        score, msg = checks.ck036(result, 'DummyFile.txt')
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_error_message(self):
        result = [{'msg': 'No index available on keyspace'}]
        score, msg = checks.ck036(result, 'DummyFile.txt')
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_correct_content(self):
        result = [{'code': 4000, 'msg': 'No index available on keyspace'}]
        score, msg = checks.ck036(result, 'DummyFile.txt')
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)


class TestPrimaryIndexCreation(unittest.TestCase):

    bucket = 'test_bucket'
    primary_index = 'test_index'

    def test_with_empty_list(self):
        score, msg = checks.ck045(self.bucket, self.primary_index, [])
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_default_name(self):
        indexes = [
            {
                "definition": "CREATE PRIMARY INDEX `#primary` ON `{0}`"
                .format(self.bucket),
                "bucket": self.bucket, "index": "#primary"
            }
        ]
        score, msg = checks.ck045(self.bucket, self.primary_index, indexes)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_secondary_index(self):
        indexes = [
            {
                "definition": "CREATE INDEX `{0}` ON `{1}`(`type`)"
                .format(self.primary_index, self.bucket),
                "bucket": self.bucket, "index": self.primary_index
            }
        ]
        score, msg = checks.ck045(self.bucket, self.primary_index, indexes)
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_primary_index_with_name(self):
        indexes = [
            {
                "definition": "CREATE PRIMARY INDEX `{0}` ON `{1}`"
                .format(self.primary_index, self.bucket),
                "bucket": self.bucket, "index": self.primary_index
            }
        ]
        score, msg = checks.ck045(self.bucket, self.primary_index, indexes)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)


class TestSelectWithExplain(unittest.TestCase):

    bucket = 'test_bucket'
    primary_index = 'test_index'
    test_file = "testfile.txt"
    result = [
        {
            "plan": {
                "#operator": 'PrimaryScan',
                "index": primary_index,
                "keyspace": bucket,
                "namespace": "default",
                "using": "gsi"
            }
        }
    ]

    def test_with_empty_list(self):
        score, msg = checks.ck046(
            self.test_file, [], self.bucket, self.primary_index
        )
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_wrong_bucket(self):
        score, msg = checks.ck046(
            self.test_file, self.result, "wrong_bucket", self.primary_index
        )
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_secondary_index_result(self):
        self.result[0]['plan']['#operator'] = 'IndexScan'
        score, msg = checks.ck046(
            self.test_file, self.result, self.bucket, self.primary_index
        )
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)
        self.result[0]['plan']['#operator'] = 'PrimaryScan'

    def test_with_primary_index_result(self):
        score, msg = checks.ck046(
            self.test_file, self.result, self.bucket, self.primary_index
        )
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)


class TestSelectDocumetns(unittest.TestCase):

    result = [
        {"countDocuments": 258, "type": "country"},
        {"countDocuments": 132844, "type": "playlist"},
        {"countDocuments": 23, "type": "sub-region"},
        {"countDocuments": 97216, "type": "track"},
        {"countDocuments": 49981, "type": "userprofile"}
    ]
    file_name = 'test_file.txt'

    def test_with_empty_list(self):
        score, msg = checks.ck047(self.file_name, [])
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_empty_dict(self):
        score, msg = checks.ck047(self.file_name, {})
        assert_equal(score, 0)
        print 'Check score: {0}'.format(score)

    def test_with_correct_result(self):
        score, msg = checks.ck047(self.file_name, self.result)
        assert_equal(score, 1)
        print 'Check score: {0}'.format(score)
