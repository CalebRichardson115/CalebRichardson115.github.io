#Returns all subsets of a given array.
class Solution(object):
    def generateSubsets(self, result, subset, index, original):
        result.append(subset[:])
        for i in range(index, len(original)):
            subset.append(original[i])
            self.generateSubsets(result, subset, i+1, original)
            subset.pop()
    def subsets(self, nums):
        result = []
        startSubset = []
        #starts at index 0
        self.generateSubsets(result, startSubset, 0, nums)
        return result