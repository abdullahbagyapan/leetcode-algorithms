class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setList = sorted(set(nums))

        nums[:] = setList

        return len(setList)