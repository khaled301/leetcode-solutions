class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows >= len(s) or numRows <= 1:
            return s
        
        str_rows = ['' for _ in range(numRows)]
        traverse_direction = 1
        current_row = 0

        for char in s:
            str_rows[current_row] += char

            if current_row == numRows - 1:
                traverse_direction = -1
            elif current_row == 0:
                traverse_direction = 1

            current_row += traverse_direction

        return ''.join(str_rows)