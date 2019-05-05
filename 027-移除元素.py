# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 原址移除等于指定值的元素 常数空间
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 返回新的数组长度
def removeElement(nums, val):
    slow = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        else:
            nums[slow] = nums[i]
            slow += 1
    return slow


if __name__ == "__main__":
    nums = [1, 3, 2, 1, 4, 3, 2, 3, 5, 1]
    print(removeElement(nums, 3))
