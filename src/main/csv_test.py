import unittest

from CSV_Reader import *


test_matrix = [['state', 'name', 'FIPS', 'pop2010', 'pop2000'],
               ['Alabama', 'Autauga County', '1001', '54571', '43671'],
               ['Alabama', 'Baldwin County', '1003', '182265', '140415'],
               ['Alabama', 'Barbour County', '1005', '27457', '29038'],
               ['Alabama', 'Bibb County', '1007', '22915', '20826'],
               ['Alabama', 'Blount County', '1009', '57322', '51024']]


class CSV_Reader_tests(unittest.TestCase):
    def test_checks_min_length(self):
        tester = return_column_from_matrix_as_array(test_matrix, "state")
        returned = ['state','Alabama','Alabama','Alabama','Alabama','Alabama']
        self.assertEqual(tester, returned)


if __name__ == "__main__":
    unittest.main()