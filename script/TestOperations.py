import unittest
import os
from PayRoll import PayRoll
from PayRule import PayRule
from Operations import Operations

class TestOperations(unittest.TestCase):
    def test_loadTest(self):
        script_dir = os.path.dirname(__file__)
        filepayroll = "tests/testpayroll.txt"
        pathpayroll = os.path.join(script_dir, filepayroll)
        payRoll = PayRoll()
        payRoll.loadFromFile(pathpayroll)


        filepayrule = "tests/testpayrule.txt"
        pathpayrule = os.path.join(script_dir, filepayrule)
        payRule = PayRule("Rule1")
        payRule.loadFromFile(pathpayrule)

        operations = Operations(payRoll, payRule)
        operations.getPaidbyName("ASTRID")
        operations.getPaid()
