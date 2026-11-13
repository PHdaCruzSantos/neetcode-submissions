class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cache = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                cache[5] += 1
            elif bill == 10:
                if cache[5] < 1:
                    return False
                cache[5] -= 1
                cache[10] += 1
            else:
                if cache[10] >= 1 and cache[5] >= 1:
                    cache[10] -= 1
                    cache[5] -= 1
                elif cache[5] >= 3:
                    cache[5] -=3
                else: return False
        return True