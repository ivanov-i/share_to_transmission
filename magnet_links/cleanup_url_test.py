import unittest
from cleanup_url import cleanup_url


class cleanup_url_test(unittest.TestCase):
    def test_only_xt(self):
        input = 'magnet:?xt=haha'
        expected = input
        actual = cleanup_url(input)
        self.assertEqual(expected, actual)
        
    def test_something_else(self):
        input = 'magnet:?xt=haha&eklmn=oprst'
        expected = 'magnet:?xt=haha'
        actual = cleanup_url(input)
        self.assertEqual(expected, actual)
        
    def test_result_xt_only_hash(self):
        input = 'magnet:?xt=urn:btih:26C59A49AAFB8D92E14326DC4A2221FC3FE702E5&tr=http%3A%2F%2Fbt.t-ru.org%2Fann%3Fmagnet&dn=%5BPluralsight.com%20%2F%20Xavier%20Shay%5D%20Testing%20Ruby%20Applications%20with%20RSpec%20%5B2015%2C%20ENG%5D'
        expected = 'magnet:?xt=urn:btih:26C59A49AAFB8D92E14326DC4A2221FC3FE702E5'
        actual = cleanup_url(input)
        self.assertEqual(expected, actual)
                
if __name__ == '__main__':
    unittest.main()
