#LeetCode 1431
#Difficulty: Easy
#RunT: O(n) , where n = number of elements in candies
#SpaceComplexity: O(n), where n = # of elements in our boolean List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        boolean = []
        for c in candies:
            if c+extraCandies >= maxi:
                boolean.append(True)
            else:
                boolean.append(False)
        return boolean