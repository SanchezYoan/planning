import unittest
from main.py import *

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'planninglog.py')

class Test(unittest.TestCase):

    def setUp(self, start, end):
        self.testdata = open(TESTDATA_FILENAME).read()
    def test_len(self, start, end):
        self.assertEqual(TESTDATA_FILENAME(1,2).x, 1)
    def test_ordonnee(self, start, end):
        self.assertEqual(TESTDATA_FILENAME(1,2).y, 2)
    def test_minutes(self, start, end):
        self.assertEqual('09:20-11:00')
    def test_format(self, start, end):
        assert False == three_words("09:20-11:00Introduction")
        assert True == three_words("09:20-11:00 Introduction")
        assert False == three_words("13:3014:10 Exercises")
        assert True == three_words("13:30-14:10 Exercises")
        assert False == three_words("9:30-10:30 Lists and Tuples")
        assert True == three_words("09:30-10:30 Lists and Tuples")
    
    
    
    
    
if__name__ == "__main__":unittest.main()