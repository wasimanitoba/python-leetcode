"""Leetcode Medium #7
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside
     the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        if x < 0:
            result = -result
        if result > (2**31 - 1) or result < (-2**31):
            return 0
        else:
            return result
        # TODO: Remember to always add some basic testing code
