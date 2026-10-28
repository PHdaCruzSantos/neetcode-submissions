class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz'
        }
        res = []
        n = len(digits)

        def dfs(i, j, curr):
            if i >= n:
                res.append("".join(curr))
                return

            letters = letterMap[digits[i]]

            if j >= len(letters):
                return
            
            curr.append(letters[j])
            dfs(i + 1, 0, curr)
            curr.pop()
            dfs(i, j + 1, curr)

        if digits: 
            dfs(0,0, [])
        return res