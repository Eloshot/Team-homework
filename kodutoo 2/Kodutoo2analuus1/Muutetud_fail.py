
def twoSum(self, nums, target):
        num_index = {}
        ans = []
        for i, num in enumerate(nums):
            answer = target - num
            if answer in num_index:
                ans.append(num_index[answer])
                ans.append(i)
                return ans
            num_index[num] = i
        return ans