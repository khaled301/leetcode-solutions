class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
    
        comb_dict_strings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 1:
            return list(comb_dict_strings[digits])

        def recursive_back_track(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else: 
                for char in comb_dict_strings[next_digits[0]]:
                    recursive_back_track(combination + char, next_digits[1:])

        recursive_back_track("", digits)
        return result