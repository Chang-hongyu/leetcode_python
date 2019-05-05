# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 解数独
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    # 判断位置i,j处的元素是否有效
    # board表示9*9的表盘
    def isvalid(self, board, i, j):
        # 同一列不能相同，m代表行
        for m in range(9):
            if m != i and board[m][j] == board[i][j]:
                return False
        # 同一行不能相同，n代表列
        for n in range(9):
            if n != j and board[i][n] == board[i][j]:
                return False
        # 不同box区域不能相同
        for m in range((i // 3) * 3, (i // 3) * 3 + 3):
            for n in range((j // 3) * 3, (j // 3) * 3 + 3):
                if m != i and n != j and board[m][n] == board[i][j]:
                    return False
        return True

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # 典型的回溯法
        self.board = board
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                # 若为.则遍历赋值，递归检测是否符合要求
                if board[i][j] == ".":
                    for c in '123456789':
                        board[i][j] = c
                        if self.isvalid(board, i, j):
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                        board[i][j] = '.'
                    return False
        return True
