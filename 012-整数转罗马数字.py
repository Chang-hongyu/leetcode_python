# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定整数 将其转换为罗马数字表示的字符串形式
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

def intToRoman(num):
    ans = ""
    query = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    symbol = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    for i in [0, 2, 4]:
        # 0对应千位，2对应百位，4对应十位
        # 计算对应位上的整数数值，并计入ans中
        k = num // query[symbol[i]]
        ans += k * symbol[i]

        # 记录对应位的下一位上的数字，注意分情况讨论
        residual = (num % query[symbol[i]]) // query[symbol[i + 2]]
        if residual == 9:
            ans += (symbol[i + 2] + symbol[i])
        elif residual >= 5:
            ans += (symbol[i + 1] + (residual - 5) * symbol[i + 2])
        elif residual == 4:
            ans += (symbol[i + 2] + symbol[i + 1])
        else:
            ans += (residual * symbol[i + 2])

        # 记录完下一位的数值之后，取之后第二位的数字为num，继续遍历
        num = (num % query[symbol[i + 2]])
        if num == 0:
            break
    return ans


if __name__ == "__main__":
    num = 1994
    # 每次循环会处理两位
    ans = intToRoman(num)
    print(ans)
