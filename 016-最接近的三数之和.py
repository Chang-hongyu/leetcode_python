# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 最接近的三数之和
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 和上一题相似的思想
def threeSumClosest(nums, target):
    # 初始化ans为无穷大，ans代表差值的绝对值
    ans = float('inf')
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        # 双指针法 双指针不断靠近
        while j < k:
            s = nums[i] + nums[j] + nums[k] - target
            # 表示本次的和比之前的更加接近target
            if abs(s) < abs(ans):
                ans = s
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            # s为0时直接返回
            else:
                return target
    return ans + target


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    ans = threeSumClosest(nums, target)
    print(ans)
