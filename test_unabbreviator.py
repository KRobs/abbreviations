import unittest
import csv
from unabbreviator import Unabbreviator

class UnabbreviatorTestCase(unittest.TestCase):
    def setUp(self):
        self.unabbreviator = Unabbreviator('abbreviation_definitions.csv')

    def test_with_file(self):
        with open('test_file.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                test_string = row[0]
                answer_string = row[1]
                self.assertEqual(self.unabbreviator.unabbreviate(test_string),
                                 answer_string)

if __name__ == '__main__':
    unittest.main()
