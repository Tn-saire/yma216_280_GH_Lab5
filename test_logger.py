import unittest     # Import the Python unit testing framework
import maths  
from logger import Logger

class Target:
    def _target(self,text):
        self.target = text

class loggerTest(unittest.TestCase):      
    def test_info(self):
        target = Target()
        log = Logger(target._target)
        log.info("msg")
        self.assertEqual("[INFO] msg", target.target, "logger info function is wrong")
        
    def test_error(self):
        target = Target()
        log = Logger(target._target)
        log.error("msg")
        self.assertEqual("[WARNING] msg", target.target, "logger error function is wrong")
        
if __name__ == '__main__':
    unittest.main()
