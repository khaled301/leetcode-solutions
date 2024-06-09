Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


# Optimal Solution Approach

## Explanation:

### Handle Empty Input: 
If the input list strs is empty, return an empty string (no common prefix).

### Initialize Prefix: 
Start with the first string in the list as the initial prefix.

### Iterate through Strings: 
Loop through each string in the list (starting from the second string).

### Character Comparison: 
For each string, compare characters in the prefix with the current string. Stop when you reach the end of the prefix, the end of the current string, or when you find a mismatch.

### Trim Prefix: 
If a mismatch is found, update the prefix by taking characters up to the mismatch point.

### Return the Final Prefix: 
After comparing all strings, the prefix variable will hold the longest common prefix.

## Time and Space Complexity Analysis:

### Time Complexity: 
O(m*n)

m is the length of the shortest string in the list.
n is the number of strings in the list.
In the worst case, the inner while loop might iterate up to m times for each of the n strings.

## Space Complexity: 
O(1)

The algorithm uses a constant amount of extra space (mainly for variables like prefix, i, and j). The space used doesn't grow significantly with the input size.
Key Points:

## Optimization: 
This solution is efficient because it doesn't unnecessarily compare characters beyond the point of a mismatch.

## Space Efficiency: 
It modifies the prefix in place, avoiding creating new strings in memory.