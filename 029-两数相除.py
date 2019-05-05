# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 计算两数相除 不使用乘除法和mod运算符
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 使用移位的思想
def divide(dividend, divisor):
    # 边界条件
    if divisor == 0:
        return False
    if divisor == 1:
        return dividend
    # 计算符号
    sign = 1
    if (dividend * divisor < 0):
        sign = -1

    ans = 0
    cnt = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    # 记录被除的数
    tmp_divisor = divisor
    while dividend >= divisor:
        while (tmp_divisor << 1) <= dividend:
            cnt <<= 1
            tmp_divisor <<= 1
        ans += cnt
        dividend -= tmp_divisor
        # 初始化循环条件
        tmp_divisor = divisor
        cnt = 1
    return min(sign * ans, 2147483647)


if __name__ == "__main__":
    divident = 10
    divisor = 3
    ans = divide(divident, divisor)
    print(ans)
