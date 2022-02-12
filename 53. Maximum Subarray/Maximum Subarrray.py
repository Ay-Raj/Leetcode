class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        m = -99999

        currsum = 0

        for n in nums:

            if currsum < 0:
                currsum = 0

            currsum += n
            m = max(m, currsum)

        return m
