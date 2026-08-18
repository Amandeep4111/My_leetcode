from itertools import groupby

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0

        for char, group in groupby(chars):
            count = len(list(group))

            chars[write] = char
            write += 1

            if count > 1:
                for x in str(count):
                    chars[write] = x
                    write += 1

        return write