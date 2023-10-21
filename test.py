# subprocess module allows you to run external shell commands from within your Python script.
import subprocess 

# unittest provides a testing framework for creating and running unit tests.
import unittest

# custom module containing utility functions (utilities.py)
import utilities

# Class containing a set of test methods to verify the functionality of the 'ccwc.py' program
class TestCCWC(unittest.TestCase):
    # The setUp method is part of the test class. It's used to set up any initial conditions required for the test methods. It sets the 'self.path' attribute to a list containing 'test.txt'
    def setUp(self) -> None:
        self.path = ["test.txt"]

    # This is the first method responsible for testing various metrics of the 'ccwc.py' program when run with a file.
    def test_all_file_metric(self):
        # line 19-23 uses the subprocess.run function to execute the ccwc.py program with the argument test.txt and capture its standard output. It stores the result in the ccwc_process variable.
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        # line 25-27 uses a similar process as above and stores the result in the cat_process variable.
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        # Line 29 extracts and processes the output from ccwc_process. It splits the output on spaces and converts the values into integers, storing them in the metric list. The [:-1] at the end is used to exclude the last value, which is assumed to be a newline character.
        metric = [int(v) for v in ccwc_process.stdout.split(" ")[:-1]]

        # The self.assertEqual method is used to compare the number of lines obtained from the cat process's output and the number of lines from the ccwc process. If they are not equal, a test failure is reported.
        self.assertEqual(
            utilities.count_lines(cat_process.stdout),
            metric[0],
            "number of lines",
        )
        # Similarly, this line compares the number of words from the cat process's output with the number of words from the ccwc process.
        self.assertEqual(
            utilities.count_words(cat_process.stdout),
            metric[1],
            "number of words",
        )
        self.assertEqual(
            utilities.count_bytes(cat_process.stdout),
            metric[2],
            "number of bytes",
        )

    # lines 50-108 are structured similarly to the test_all_file_metric method but focus on different metrics (lines, words, bytes, and characters).
    def test_number_of_lines(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-l", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_lines = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_lines(cat_process.stdout), number_of_lines
        )

    def test_number_of_words(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-w", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_words = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_words(cat_process.stdout), number_of_words
        )

    def test_number_of_bytes(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-c", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_bytes = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_bytes(cat_process.stdout), number_of_bytes
        )

    def test_number_of_characters(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-m", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_chars = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_characters(cat_process.stdout), number_of_chars
        )

# This class follows the same structure and logic but tests the ccwc.py program when run without any arguments.
class TestCCWCWithoutArguments(unittest.TestCase):
    def setUp(self) -> None:
        self.path = ["test.txt"]

    def test_all_file_metric(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        metric = [int(v) for v in ccwc_process.stdout.split(" ")[:-1]]

        self.assertEqual(
            utilities.count_lines(cat_process.stdout),
            metric[0],
            "number of lines",
        )
        self.assertEqual(
            utilities.count_words(cat_process.stdout),
            metric[1],
            "number of words",
        )
        self.assertEqual(
            utilities.count_bytes(cat_process.stdout),
            metric[2],
            "number of bytes",
        )

    def test_number_of_lines(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-l"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_lines = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_lines(cat_process.stdout), number_of_lines
        )

    def test_number_of_words(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-w"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_words = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_words(cat_process.stdout), number_of_words
        )

    def test_number_of_bytes(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-c"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_bytes = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_bytes(cat_process.stdout), number_of_bytes
        )

    def test_number_of_characters(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-m"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_chars = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_characters(cat_process.stdout), number_of_chars
        )


if __name__ == "__main__":
    unittest.main()