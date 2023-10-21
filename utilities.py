import re

# This function takes a bytes object as input and returns the number of bytes in that object.
# It uses the len() function to calculate the length of the bytes object, which effectively gives you the count of bytes.
def count_bytes(byteObject: bytes) -> int:
    return len(byteObject)

# This function takes a bytes object as input and returns the number of words in that object.
# It first decodes the bytes object to a string using .decode().
# It uses a regular expression and the re.split() function to split the decoded string into a list of words based on whitespace characters (space, tab, newline). It then filters out any empty strings from the list of words using a list comprehension. The length of the filtered list represents the count of words in the test.
def count_words(byteObject: bytes) -> int:
    return len(
        [word for word in re.split("\s", byteObject.decode()) if word != ""]
    )

# This function takes a bytes object and an optional integer 'i' as input and returns the number of lines in that object. It assumes that the byteObject represents text with newline characters('\n') to separate lines. It iterates over each character in the decoded string and increments 'i' each time it encounters a newline character. The final value of 'i' represents the count of lines in the text.
def count_lines(byteObject: bytes, i: int = 0) -> int:
    for ch in byteObject.decode():
        if ch == "\n":
            i += 1
    return i

# This function takes a bytes object as input and returns the number of characters in that object. It decodes the bytes object to a string using .decode(). It calculates the length of the decoded string using the len() function, giving you the count of characters.
def count_characters(byteObject: bytes) -> int:
    return len(byteObject.decode())