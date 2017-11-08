import unittest
import check_polindroms
class TestCheckPolindrom(unittest.TestCase):
    def test_convert_number_to_base_x(self):
    	f_result = ''
        result = check_polindroms.convert_number_to_base_x(17,2)
        for s in result:
             f_result += str(s)
        self.assertEquals(f_result, '10001')

    def test_build_the_number(self):
        result = check_polindroms.build_the_number([6,10])
        self.assertEquals(result, '6a')

    def test_check_if_number_is_polindrom(self):
        result = check_polindroms.check_if_number_is_polindrom('11')
        result1 = check_polindroms.check_if_number_is_polindrom('10011')
        self.assertEquals(result, True)
        self.assertEquals(result1, False)

    def test_check_numbers(self):
        testlist = []
        f = open("test.txt", "r")
        for l in f:
            testlist.append(l)
        f.close()
        result = check_polindroms.check_numbers()
        self.assertListEqual(result,testlist)