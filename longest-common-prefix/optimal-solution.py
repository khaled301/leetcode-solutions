class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        common_prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0

            while j < len(common_prefix) and j < len(strs[i]) and common_prefix[j] == strs[i][j]:
                j += 1

            common_prefix = common_prefix[:j]

        return common_prefix