# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定一个数组 表示各个容器高度 求可以盛最多水
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

def maxArea(nums):
    if len(nums) <= 1:
        return 0
    ans = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        ans = max(ans, (right - left) * min(nums[left], nums[right]))
        if nums[left] <= nums[right]:
            left += 1
        else:
            right -= 1
    return ans


if __name__ == "__main__":
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = maxArea(nums)
    print(ans)
