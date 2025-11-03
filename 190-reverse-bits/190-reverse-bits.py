class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f'{n:032b}'
        reverse = binary[::-1]
        return int(reverse, 2)