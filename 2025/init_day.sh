mkdir -p day$1/input
mkdir -p day$1/test
touch day$1/input/input.txt
touch day$1/test/__init__.py
touch day$1/test/test_puzzle1.py
touch day$1/test/test_puzzle2.py
touch day$1/__init__.py
touch day$1/puzzle1.py
touch day$1/puzzle2.py

echo "
import os.path as osp


if __name__ == \"__main__\":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', \"input.txt\")

    with open(input_path, \"r\") as f:
        lines = f.readlines()" | tee day$1/puzzle1.py day$1/puzzle2.py


echo "import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day${1}.puzzle1 as puzzle1

class Day${1}Puzzle1Test(unittest.TestCase):
    def test(self):
        pass" >> day$1/test/test_puzzle1.py

echo "import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day${1}.puzzle2 as puzzle2

class Day${1}Puzzle2Test(unittest.TestCase):
    def test(self):
        pass" >> day$1/test/test_puzzle2.py