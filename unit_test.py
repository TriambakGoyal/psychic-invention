import unittest
from solution import solution, findDay

class TestStringMethods(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(solution({'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':-2,'2020-01-08':-2}), {'Mon': -6, 'Tue': -2, 'Wed': 2, 'Thu': 4, 'Fri': 6, 'Sat': 8, 'Sun': 2})

    def test_finday(self):
        self.assertEqual(findDay('2020-01-01'),'Wed')
        self.assertFalse(findDay('2020-01'))

    def test_missing_day(self):
        self.assertEqual(solution({'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}), {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14})

    def test_check_days(self):
        self.assertFalse(solution({'2020-01-01':6}))

    def test_check_Monday_and_sunday(self):
        self.assertFalse(solution({'2020-01-01':6,'2020-01-04':12}))
        self.assertEqual(solution({'2020-01-05':14,'2020-01-06':2}),{'Mon': 2, 'Tue': -10, 'Wed': -22, 'Thu': -34, 'Fri': -46, 'Sat': -58, 'Sun': 14})

    def test_null(self):
        self.assertFalse(solution({}))
        
if __name__ == '__main__':
    unittest.main()