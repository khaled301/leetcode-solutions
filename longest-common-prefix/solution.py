# This is a brute force solution that comes in to mind first for this problem.
# Please consider the solution from the Optimal Solution file 
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        if len(strs) == 0:
            return ""

        result = ""
        common_prefix = ""
        count = 0

        while count < len(strs):
            if count + 1 < len(strs) and count == 0:
                common_prefix = self.get_common_prefix(strs[count], strs[count + 1])
                count += 2
            else:
                common_prefix = self.get_common_prefix(common_prefix, strs[count])
                count += 1
                
            if len(common_prefix) != result:
                result = common_prefix

        return result

    def get_common_prefix(self, str1: str, str2: str):
        temp_prefix = ""

        for i in range(len(str1)):
            if i < len(str2) and str1[i] == str2[i]:
                temp_prefix += str1[i]
            else: 
                break

        return temp_prefix