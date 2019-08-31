import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        add_result = maths.add(15,16)
        self.assertEqual(31, add_result, "add function is wrong")
        base_result = maths.add(4,6,2)
        self.assertEqual(1010,base_result, "add function base test under 10 is wrong")
        new_base_result = maths.add(10,16,16)
        self.assertEqual("1A",new_base_result, "add function base test pass over 10 is wrong")
        
        
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        test_result = maths.fibonacci(5)
        self.assertEqual(5, test_result, "fibonacci function is wrong")

        
    def test_convert_base(self):
        convert_result = maths.convert_base(10, 8)
        self.assertEqual(12, convert_result, "convert_base function base under ten is wrong")
        big_result = maths.convert_base(27, 16)
        self.assertEqual("1B", big_result, "convert_base function base pass over ten is wrong")
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
