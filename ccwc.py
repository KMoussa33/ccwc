# Module used for parsing command-line arguments and options.
import argparse

# Provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter
import sys

# This is imported to define a dictionary type for variable annotations.
from typing import Dict

from utilities import count_bytes, count_characters, count_lines, count_words

"""The ccwc.py module is responsible for handling the user interactions"""

# lines 15-19 define the command-line argument parser using the argparse module. 'prog' specifies the program name displayed in help messages. 'usage' defines the usage message that appears in help messages, showing that the script can accept options and one or more file arguments. 'description' provides a brief description of the script's purpose.
parser = argparse.ArgumentParser(
    prog="ccwc.py",
    usage="%(prog)s [options] FILE [FILE...]",
    description="Print newline, word and byte for each file",
)

# lines 22-29 define a positional argument named 'files'. It allows hte script to accept one or more file paths as arguments. Details include: 'metavar': placeholder name used in help messages. 'default': default value for the argument, set to an empty string. 'type': expected data type for the argument (a string). 'nargs': specifies that the argument can accept multiple values (denoted by '"*"). 'help': a help message that describes the purpose of this argument.
parser.add_argument(
    "files",
    metavar="FILE",
    default="",
    type=str,
    nargs="*",
    help="take a file or a list of files",
)

# lines 32-38 define an optional argument for counting lines. "-l" and "--line" are the short and long option names, respectively. 'default=False' specifies that this option is desabled by default. 'action="store_true"' means that when this option is provided, it sets the corresponding attribute to 'True'. 'help' provides a help message describing the purpose of this option.
parser.add_argument(
    "-l",
    "--line",
    default=False,
    action="store_true",
    help="print the line counts",
)

# Similar lines define other optional arguments for counting bytes, characters, and words.

parser.add_argument(
    "-c",
    "--byte",
    default=False,
    action="store_true",
    help="print the byte counts",
)
parser.add_argument(
    "-m",
    "--char",
    default=False,
    action="store_true",
    help="print the character counts",
)
parser.add_argument(
    "-w",
    "--word",
    default=False,
    action="store_true",
    help="print the word counts",
)


# This is a function named wrapper that takes three arguments:
# func: A metric calculation function (e.g., count_bytes, count_characters).
# byteObject: A bytes object representing the text to be analyzed.
# key: A string representing the metric being calculated (e.g., "bytes," "characters").
# Inside the function:

# It uses the func to calculate the metric based on the byteObject.
# It appends the calculated metric to the message variable as a string.
# It updates a dictionary named files_metric_summary with the calculated metric, using key as the key.
def wrapper(func, byteObject: bytes, key: str) -> None:
    global message
    c_obj = func(byteObject)
    message += f"{c_obj} "
    files_metric_summary.setdefault(key, 0)
    files_metric_summary.update({key: files_metric_summary.get(key) + c_obj})


# This function generate_file_metric calculates text metrics for a given byteObject based on the command-line arguments.
# It checks if none of the metric options are specified (e.g., -l, -w, -c, -m). If none are specified, it calculates all metrics (lines, words, bytes) using the wrapper function.
# If any of the metric options are specified, it calculates only the selected metrics based on the provided options.
def generate_file_metric(byteObject: bytes):
    if not any([args.line, args.word, args.byte, args.char]):
        wrapper(count_lines, byteObject, "lines")
        wrapper(count_words, byteObject, "words")
        wrapper(count_bytes, byteObject, "bytes")
    else:
        if args.line:
            wrapper(count_lines, byteObject, "lines")

        if args.word:
            wrapper(count_words, byteObject, "words")

        if args.byte:
            wrapper(count_bytes, byteObject, "bytes")

        if args.char:
            wrapper(count_characters, byteObject, "chars")


# The if __name__ == "__main__": block is the main part of the script.
# It starts by parsing the command-line arguments using parser.parse_args() and stores the arguments in the args variable.
# It initializes two variables: message (to store the output message) and files_metric_summary (a dictionary to summarize metrics for multiple files).
# It then iterates through the input files specified in args.files. For each file:
# It opens the file in binary mode ("rb").
# It reads the file contents as a bytes object and calculates the desired metrics using the generate_file_metric function.
# It prints a message containing the filename and the calculated metrics.
# The message is reset to an empty string for the next file.
# If no files are provided (i.e., args.files is empty), it reads from standard input (sys.stdin) and calculates metrics accordingly.
if __name__ == "__main__":
    args = parser.parse_args()

    message: str = ""
    files_metric_summary: Dict[str, int] = {}

    for file in args.files:
        with open(file, "rb") as fd:
            generate_file_metric(fd.read())

        message += f"{file}"
        print(message)
        message = ""

    # If no file is passed read stdin
    if not args.files:
        generate_file_metric(sys.stdin.buffer.read())
        print(message)

    # If provided files are more than one show total
    # Finally, if more than one file is provided, it prints the total metrics across all files.
    if len(args.files) > 1:
        print(*files_metric_summary.values(), "total")