# -*- coding:utf-8 -*-
# Author: Chang-hongyu
# @Function: 求不出现重复的字符串的最大长度
# @Version : 1.0"
# @Contact : 582246340@sjtu.edu.cn"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #滑动窗口方法
        max_len = 0
        start = 0
        d = {}
        for i, tmp in enumerate(s):
            # 若出现重复，则以上一次开始的下一个位置，和start之间的最大值作为开始
            if tmp in d:
                start = max(start, d[tmp]+1)
            # 若未出现重复，则记录这个字符对应的位置索引
            d[tmp] = i
            # 更新最大长度
            max_len = max(max_len, i-start+1)
        return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)