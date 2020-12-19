import unittest

from DB.db import DataStore as DB

class TestDB(unittest.TestCase):
    def setUp(self):
        pass
        self.DB = DB
    
    def test_insert_in_db(self):
        res = self.DB.update_country_stat('IN', 'mobile', 10, 20)
        self.assertTrue(res == True) 
        res = self.DB.get_stat(['IN'], ['mobile'])
        req_count = list(filter(lambda x: x['key'] == 'webreq', res['metrics']))[0]['val']
        timespent = list(filter(lambda x: x['key'] == 'timespent', res['metrics']))[0]['val']
        self.assertEqual(req_count, 10)
        self.assertEqual(timespent, 20)

    def test_device_filter_in_db(self):
        res = self.DB.update_country_stat('EN', 'web', 10, 20)
        assert res == True
        res = self.DB.get_stat(["EN"], ['mobile'])
        req_count = list(filter(lambda x: x['key'] == 'webreq', res['metrics']))[0]['val']
        timespent = list(filter(lambda x: x['key'] == 'timespent', res['metrics']))[0]['val']
        self.assertEqual(req_count, 0)
        self.assertEqual(timespent, 0)

    def test_partial_device_filter(self):
        res = self.DB.update_country_stat('USA', 'web', 10, 20)
        res = self.DB.update_country_stat('USA', 'mobile', 40, 100)
        assert res == True
        res = self.DB.get_stat(["USA"], ['mobile'])
        req_count = list(filter(lambda x: x['key'] == 'webreq', res['metrics']))[0]['val']
        timespent = list(filter(lambda x: x['key'] == 'timespent', res['metrics']))[0]['val']
        self.assertEqual(req_count, 40)
        self.assertEqual(timespent, 100)

    def test_country_filter(self):
        res = self.DB.get_stat(["CA"], [])
        req_count = list(filter(lambda x: x['key'] == 'webreq', res['metrics']))[0]['val']
        timespent = list(filter(lambda x: x['key'] == 'timespent', res['metrics']))[0]['val']
        self.assertEqual(req_count, 0)
        self.assertEqual(timespent, 0)

if __name__ == '__main__':
    unittest.main()
