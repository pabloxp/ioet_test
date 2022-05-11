import os
from PayRoll import PayRoll
from PayRule import PayRule
from Operations import Operations
import argparse

def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='Payroll Files')
    parser.add_argument('--payrule', type=str, required=True,
                        default='./test/testpayrule.txt',
                        help='PayRule File')
    parser.add_argument('--payroll', type=str, required=True,
                        default='./test/testpayroll.txt',
                        help='PayRoll File')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    script_dir = os.path.dirname(__file__)
    filepayroll = args.payroll
    pathpayroll = os.path.join(script_dir, filepayroll)
    payRoll = PayRoll()
    payRoll.loadFromFile(pathpayroll)


    filepayrule = args.payrule
    pathpayrule = os.path.join(script_dir, filepayrule)
    payRule = PayRule("Rule1")
    payRule.loadFromFile(pathpayrule)

    operations = Operations(payRoll, payRule)
    operations.getPaid()
