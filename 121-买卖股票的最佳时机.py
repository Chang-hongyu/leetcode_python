# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 买卖股票的最佳时机
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 允许买卖一次，先买后卖股票的最大利润

class Solution:
    def maxProfit(self, nums):
        # 记录之前的最小值
        pre_min = nums[0]
        # 结果初始化为0
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - pre_min)
            pre_min = min(pre_min, nums[i])
        return ans


if __name__ == "__main__":
    nums = [2, 1, 4, 3, 2, 6, 5, 4]
    ans = Solution().maxProfit(nums)
    print(ans)
