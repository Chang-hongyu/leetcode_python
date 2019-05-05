# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 接雨水的最大值
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class Solution:
    def trap(self, height):
        ans = 0
        n = len(height)
        if n <= 1:
            return ans
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        # 左边的最大值
        # 使用height[i]是为了避免出现负数
        for i in range(1, n, 1):
            left_max[i] = max(left_max[i - 1], height[i])
        # 右边的最大值
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j])
        # 遍历数组 累加雨水储存量
        for k in range(n):
            ans += (min(left_max[k], right_max[k]) - height[k])
        return ans


if __name__ == "__main__":
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    ans = Solution().trap(nums)
    print(ans)