# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 在原地修改输入数组并在使用常数额外空间完成 函数返回新的数组长度
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 原数组已排序
def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    slow = 0
    nums[slow] = nums[0]
    for i in range(len(nums)):
        if nums[i] != nums[slow]:
            slow += 1
            nums[slow] = nums[i]
    return slow + 1


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 8]
    print(removeDuplicates(nums))
