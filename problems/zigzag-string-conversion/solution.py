class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        str_arr = list(s)
        array_2d_str = [[] for _ in range(numRows)]

        while 0 < len(str_arr):
            for i in range(numRows):
                if len(str_arr) == 0:
                    break

                popped_str = str_arr.pop(0)
                array_2d_str[i].append(popped_str)

            for i in range(numRows - 2, 0, -1):
                if len(str_arr) == 0:
                    break
                popped_str = str_arr.pop(0)
                array_2d_str[i].append(popped_str)

            if len(str_arr) == 0:
                break

        if len(array_2d_str) > 0:
            return ''.join([''.join(row) for row in array_2d_str])

        return ''
