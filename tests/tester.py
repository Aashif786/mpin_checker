from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import run_checker

# Each test case now has inputs for two cycles (MPIN + 3 dates + continue flag)
test_cases = [
    # cycle 1 inputs + cycle 2 inputs (with 'n' to stop)
    [
        ["1234"], "01/01/1990", "02/02/1992", "03/03/1993", "y",
        ["1990"], "01-01-1990", "02-02-1992", "03-03-1993", "n"
    ],
    [
        ["0202"], "01/01/1990", "02/02/1992", "03/03/1993", "y",
        ["134823"], "01/01/1990", "02/02/1992", "03/03/1993", "n"
    ],
    [
        ["3112"], "31/12/2000", "01/01/1991", "02/02/1992", "y",
        ["9999"], "01/01/1980", "01/01/1981", "01/01/1982", "n"
    ],
    [
        ["123456"], "12/03/2000", "01/02/1995", "02/02/1992", "y",
        ["3002"], "30/02/2000", "01/01/1991", "01/01/1992", "n"
    ],
    [
        ["5678"], "12/12/2012", "13/12/2012", "14/12/2012", "y",
        ["3197"], "10/10/2010", "01/01/1991", "01/01/1992", "n"
    ],
    [
        ["2000"], "01/01/2000", "01/01/2001", "01/01/2002", "y",
        ["010101"], "01/01/1991", "01/01/1992", "01/01/1993", "n"
    ],
    [
        ["8888"], "01/08/1988", "01/01/1990", "01/01/1992", "y",
        ["8934"], "01/01/1990", "01/01/1991", "01/01/1992", "n"
    ],
    [
        ["011990"], "01/01/1990", "02/02/1992", "03/03/1993", "y",
        ["0101"], "01/01/1990", "02/02/1992", "03/03/1993", "n"
    ],
    [
        [["01021991", "1429"]], "1923", "01/01/1990", "01/01/1991", "03/03/1993", "y",
        ["011991"], "01/01/1990", "01/01/1991", "03/03/1993", "n"
    ],
    [
        ["098423"], "01/01/1990", "02/02/1992", "03/03/1993", "y",
        ["01011990"], "0192", "01/01/1990", "02/02/1992", "03/03/1993", "n"
    ],
    [
        ["010119"], "01/01/1990", "02/02/1992", "03/03/1993", "y",
        ["999"], "1999", "01/01/1990", "02/02/1992", "03/03/1993", "n"
    ],
    [
        ["1990"], "01/01/1990", "02/02/1992", "03/03/1993", "n"
    ],
]

class TestInput:
    def __init__(self, *args):
        self.inputs = []
        for arg in args:
            if isinstance(arg, list):
                self.inputs.extend(arg)
            else:
                self.inputs.append(arg)
        self.index = 0

    def __call__(self, prompt=""):
        if self.index >= len(self.inputs):
            print(f"DEBUG: Index {self.index} out of range for inputs length {len(self.inputs)}")
            raise IndexError("Ran out of test inputs")
        value = self.inputs[self.index]
        print(f"DEBUG: Returning input[{self.index}] = {value}")
        self.index += 1
        return value

class TestOutput:
    def __init__(self):
        self.buffer = StringIO()

    def __call__(self, msg=""):
        print(msg, file=self.buffer)

    def get_output(self):
        return self.buffer.getvalue()

for i, test in enumerate(test_cases, start=1):
    test_input = TestInput(*test)
    test_output = TestOutput()

    print(f"Running Test Case {i}:")
    run_checker(input_fn=test_input, output_fn=test_output)
    print(test_output.get_output())
    print("=" * 60)
