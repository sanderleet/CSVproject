import unittest

from CSV_Reader import *


test_matrix = [['state', 'name', 'FIPS', 'pop2010', 'pop2000'],
               ['Alabama', 'Autauga County', '1001', '54571', '43671'],
               ['Alabama', 'Baldwin County', '1003', '182265', '140415'],
               ['Alabama', 'Barbour County', '1005', '27457', '29038'],
               ['Alabama', 'Bibb County', '1007', '22915', '20826'],
               ['Alabama', 'Blount County', '1009', '57322', '51024']]

test_matrix2 = [['state', 'name', 'FIPS', 'pop2010', 'pop2000'],
               ['Alabama', 'Autauga County', '1001', '54571', '43671'],
               ['Alabama', 'Baldwin County', '1003', '182265', '140415'],
               ['Alabama', 'Barbour County', '1005', '27457', '29038'],
               ['Alabama', 'Bibb County', '1007', '22915', '20826'],
               ['Alabama', 'Blount County', '1009', '57322', '51024']]

test_column = ['state','Alabama','Alabama','Alabama','Alabama','Alabama']

class CSV_Reader_tests(unittest.TestCase):

    def test_return_matrix_from_csv(self):
        tester = return_matrix_from_csv("simpleEX1.csv")
        returned = test_matrix2
        self.assertEqual(tester, returned)


    def test_append_column_into_matrix(self):
        tester = append_column_into_matrix(test_matrix, test_column)
        returned = [['state', 'name', 'FIPS', 'pop2010', 'pop2000', 'state'],
               ['Alabama', 'Autauga County', '1001', '54571', '43671', 'Alabama'],
               ['Alabama', 'Baldwin County', '1003', '182265', '140415', 'Alabama'],
               ['Alabama', 'Barbour County', '1005', '27457', '29038', 'Alabama'],
               ['Alabama', 'Bibb County', '1007', '22915', '20826', 'Alabama'],
               ['Alabama', 'Blount County', '1009', '57322', '51024', 'Alabama']]
        self.assertEqual(tester, returned)

    def test_return_column_from_matrix_as_array(self):
        tester = return_column_from_matrix_as_array(test_matrix, "state")
        returned = ['state','Alabama','Alabama','Alabama','Alabama','Alabama']
        self.assertEqual(tester, returned)

if __name__ == "__main__":
    unittest.main()