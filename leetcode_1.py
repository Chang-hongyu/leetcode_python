# -*- coding:utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        #用字典来保存键值对
        d = {}
        #num对应key,i对应value
        for i,num in enumerate(nums):
            # 若对应的差值作为键在字典中，则返回对应的索引
            if target - num in d:
                return [d[target-num], i]
            # 否则，将键值对添加入字典中
            d[num] = i
        # 若找不到则返回None
        return None

if __name__ == "__main__":
    nums = [2,7,11,15]
    ans = Solution()
    print(ans.twoSum(nums,13))