import unittest
import requests
from transmission import Transmission

class Transmission_test(unittest.TestCase):
    def test_nothing_works(self):
        self.assertEqual(1,1)
        t = Transmission()
        print(t.request(requests.get).__dict__)

                
if __name__ == '__main__':
    unittest.main()
