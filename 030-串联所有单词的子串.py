# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 串联所有单词的子串
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 给定一个字符串s和一些长度相同的单词words。找出s中恰好可以由words中所有单词串联形成的子串的起始位置。

# 注意子串要与words中的单词完全匹配，中间不能有其他字符，但不需要考虑words中单词串联的顺序。
class Solution:
    def findSubstring(self, s, words):
        if not s or len(words) == 0:
            return []
        lenstr = len(s)
        lenword = len(words[0])
        allwords = lenword * len(words)
        word_dic = {}
        for word in words:
            word_dic[word] = word_dic.get(word, 0) + 1
        ans = []
        for i in range(min(lenword, lenstr - allwords + 1)):
            self.findStart(i, lenstr, lenword, allwords, s, word_dic, ans)
        return ans

    def findStart(self, strstart, lenstr, lenword, allwords, s, word_dic, ans):
        wordstart = strstart
        curr = {}
        while strstart + allwords <= lenstr:
            word = s[wordstart:wordstart + lenword]
            wordstart += lenword
            if word not in word_dic:
                strstart = wordstart
                curr.clear()
                continue
            else:
                curr[word] = curr.get(word, 0) + 1
                while curr[word] > word_dic[word]:
                    curr[s[strstart:strstart + lenword]] -= 1
                    strstart += lenword
                if wordstart - strstart == allwords:
                    ans.append(strstart)


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    ans = Solution().findSubstring(
        s, words)
    print(ans)
