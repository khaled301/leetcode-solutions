The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000


# Optimal Solution:

### Explanation:

#### Initialization:

rows = ["" for _ in range(numRows)]: Creates an empty list of strings with length numRows, representing the rows of the zigzag pattern.
direction = 1: Sets the initial direction of movement (downwards).
row = 0: Initializes the current row index.

#####  Ensure that numRows is appropriately handled, especially when it is greater than or equal to the length of the string

#### Iterating through the String:

for char in s:: Loop through each character in the input string s.
rows[row] += char: Appends the current character to the string at the corresponding row index.
Direction Change Logic:
if row == numRows - 1: direction = -1: If we reach the bottom row, change the direction to go upwards.
elif row == 0: direction = 1: If we reach the top row, change the direction to go downwards.
row += direction: Updates the row index based on the current direction.

#### Joining the Rows:

return "".join(rows): Concatenates all the strings in the rows list into a single string, effectively reconstructing the zigzag pattern.

#### Time Complexity: 
O(n), where n is the length of the input string. We iterate through the string once to build the zigzag pattern.

#### Space Complexity: 
O(n), where n is the length of the input string. In the worst case, the rows list can hold the entire input string.
```