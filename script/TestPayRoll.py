import unittest
import os
from PayRoll import PayRoll

class TestPayRoll(unittest.TestCase):
    def test_loadTest(self):
        script_dir = os.path.dirname(__file__)
        file = "tests/testpayroll.txt"
        path = os.path.join(script_dir, file)
        pR = PayRoll()
        pR.loadFromFile(path)
        #for f in pR.employees:
        #    print(f.name)
            #for d in f:
                #print(d.name,d.start,d.end)
        self.assertEqual(len(pR.getPayRoll().employees), 3)


if __name__ == '__main__':
    unittest.main()
