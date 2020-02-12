class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        nums.sort()
        for i in nums:
            if not i in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        inverted_dict = dict([[v,k] for k,v in dictionary.items()])
        return inverted_dict[1]