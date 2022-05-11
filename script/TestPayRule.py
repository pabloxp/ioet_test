import unittest
import os
from PayRule import PayRule

class TestPayRule(unittest.TestCase):
    def test_loadTest(self):
        script_dir = os.path.dirname(__file__)
        path = "2091/data.txt"
        file = "tests/testpayrule.txt"
        path = os.path.join(script_dir, file)
        pR = PayRule("Rule1")
        pR.loadFromFile(path)

        self.assertEqual(len(pR.getPayRule().days), 21)


if __name__ == '__main__':
    unittest.main()
