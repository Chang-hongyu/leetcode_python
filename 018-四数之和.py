# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 判断nums是否存在四个数之和为target
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    ans = []
    # 初始化第一个数
    for i in range(n - 3):
        # 若前后相同则跳过 避免重复
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 初始化第二个数
        for j in range(i + 1, n - 2):
            # 前后相同则跳过 避免重复
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # 初始化第三个数
            k = j + 1
            # 初始化第四个数
            l = n - 1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l] - target
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k - 1] == nums[k]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif s < 0:
                    k += 1
                else:
                    l -= 1
    return ans


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ans = fourSum(nums, target)
    print(ans)
