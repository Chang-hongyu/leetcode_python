# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 求出给定数组的最长上升子序列的长度
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    def lengthOfLIS(self, nums):
        # dp[i]的意义是到该位置为止的最长递增子序列 ON^2 包含此位置
        if not nums:
            return 0

        # 初始化为0
        dp = [1 for _ in range(len(nums))]
        # 第一层遍历 位置0之后的所有位置
        for i in range(1, len(nums)):
            tmax = dp[i]
            # 第二层遍历，遍历i之前的所有位置，若nums[i]>nums[j]，则更新最大递增子序列长度
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmax = max(dp[j] + 1, tmax)
            dp[i] = tmax
        return max(dp)

    def lengthOfLIS_binary(self, nums):
        if len(nums) <= 1:
            return len(nums)
        lis = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                index = self.binary_search(lis, nums[i])
                lis[index] = nums[i]
        return len(lis)

    # 找到数字插入数组的索引
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
    print(Solution().lengthOfLIS_binary(nums))
