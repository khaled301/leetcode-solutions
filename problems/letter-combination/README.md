Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


# Optimal Solution:

-   The function letterCombinations takes a string digits as input, which represents a sequence of digits from 2 to 9 inclusive.

-   It first checks if the input string digits is empty. If it is, it returns an empty list, as there are no combinations to generate.

-   It defines a dictionary mapping that maps each digit to the corresponding letters on a telephone keypad.

-   The function defines a nested helper function called backtrack which generates all possible combinations recursively. This function takes two parameters: combination, which represents the current combination being constructed, and next_digits, which represents the remaining digits to be processed.

-   If there are no more digits to process (i.e., the length of next_digits is zero), the current combination is added to the output list.

-   Otherwise, for each letter corresponding to the first digit in next_digits, the function recursively calls backtrack with the updated combination and the remaining digits (next_digits[1:]).


#   Time Complexity:
### Backtracking: 
The main work in this function is done by the backtrack function, which performs a depth-first search (DFS) traversal of all possible combinations of letters. In the worst-case scenario, each digit could correspond to up to 4 letters (for digits 7 and 9). Therefore, the time complexity of generating all combinations is O(4^N), where N is the length of the input string digits.

### Appending to Output List: 
Each valid combination is appended to the output list, which requires O(1) time.
So, the overall time complexity of the letterCombinations function is O(4^N).


#   Space Complexity:
### Output List: 
The output list stores all the valid combinations. In the worst-case scenario, when every digit corresponds to 4 letters, there can be a total of 4^N combinations. Therefore, the space complexity of the output list is O(4^N).

### Recursion: 
The space used by the recursive calls to the backtrack function depends on the maximum depth of the recursion, which is equal to the length of the input string digits. Therefore, the space complexity due to recursion is O(N).
Other Variables: The space complexity of other variables used in the function, such as the mapping dictionary and the parameters of the backtrack function, is negligible compared to the space used by the output list and the recursion.