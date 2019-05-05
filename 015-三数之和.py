# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 判断数组中是否有三个数之和为0
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 注意 数组中可能有重复元素，但是ans中不能出现重复结果，ans中的每个结果中可能出现相同的数
def threeSum(nums):
    nums.sort()
    n = len(nums)
    # 记录最终结果
    ans = []
    # 第一个数的起始点，最多到nums[n-3]，选取第一个数起点开始循环
    for i in range(n - 2):
        # 如果起始点的数等于前一个数，则跳过，因为会重复
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 初始化 第二个数为第一个数后面第一个数
        j = i + 1
        # 初始化 第三个数为倒数第一个数
        k = n - 1
        # 采用双指针的思想
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                ans.append([nums[i], nums[j], nums[k]])
                # 注意两者都移动，如果遇到同样的元素，不移动会导致重复
                j += 1
                k -= 1
                # 跳过第二个数重复的情况
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                # 跳过第三个数重复的情况
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            # 若和小于0，则将第二个数的指针向后移动
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
    return ans


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    ans = threeSum(nums)
    print(ans)
