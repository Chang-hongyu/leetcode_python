# -*- coding:utf-8 -*-
# Author: Chang-hongyu
# @Function: 寻找两个有序数组的中位数
# @Version : 1.0"
# @Contact : 582246340@sjtu.edu.cn"


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m, n = len(nums1), len(nums2)
        if n < m:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            # i太小，需要增大
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            # i太大，需要减小
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
    a = [1, 2, 4, 7, 8, 15, 43, 56]
    b = [2, 3, 7, 12, 32]
    ans = Solution().findMedianSortedArrays(a, b)
    print(ans)
