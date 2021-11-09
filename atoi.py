"""
Leetcode medium #8: 8. String to Integer (atoi)
Implement the myAtoi(string s) function,
 which converts a string to a 32-bit signed integer
 (similar to C/C++'s atoi function).
"""


# TODO: Can this be more "pythonic"? It's probably too complex, as well.
class Solution:
    def join(self, output: list) -> int:
        result = int("".join(output))
        if result > (2 ** 31 - 1):
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31
        else:
            return result

    def myAtoi(self, string: str) -> int:
        output = ['+0']
        firstNonWhiteSpace = False
        firstInt = False
        for letter in string:
            if letter == " ":
                if firstInt is True or firstNonWhiteSpace is True:
                    """ if we reach whitespace AFTER integers,
                     we immediately return"""
                    return self.join(output)
                continue
            elif letter == "+" or letter == "-":
                if firstInt is False:
                    if firstNonWhiteSpace is False:
                        output[0] = str(letter) + "0"
                        firstNonWhiteSpace = True
                    else:
                        return 0
                else:
                    return self.join(output)
            elif ord(letter) < 48 or ord(letter) > 57:
                firstNonWhiteSpace = True
                if firstInt is True:
                    """if we have already found numbers and reach a letter,
                     we immediately return"""
                    return self.join(output)
                else:
                    return 0
            elif ord(letter) > 47 and ord(letter) < 58:
                firstInt = True
                output.append(letter)
        return self.join(output)
