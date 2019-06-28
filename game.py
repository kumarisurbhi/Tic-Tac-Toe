# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:18:06 2019

@author: Sourabh Kumar
"""

import numpy as np
    
def horizontal_check(board):
    for i in range(len(board)):
        l = []
        for j in range(len(board)):
            l.append(board[i][j])
        l_set = set(l)
        x = l_set.pop()
        if len(set(l)) == 0 and x != 0:
            return True
    return False
    
def vertical_check(board):
    for i in range(len(board)):
        l = []
        for j in range(len(board)):
            l.append(board[j][i])
        l_set = set(l)
        x = l_set.pop()
        if len(l_set) == 0 and x != 0:
            return True
    return False
    
def diag_check(board):
    diag1 = [board[0,0], board[1,1], board[2,2]]
    diag2 = [board[2,0], board[1,1], board[0,2]]
    diag1_set = set(diag1)
    diag2_set = set(diag2)
    x1 = diag1_set.pop()
    x2 = diag2_set.pop()
    if (len(diag1_set) == 0 and x1 != 0) or (len(diag2_set) == 0 and x2 != 0):
        return True
    else:
        return False

def check_win(board):
    return (vertical_check(board) or horizontal_check(board)) or diag_check(board)
    
def player1_turn(board):
    try_again = True
    print("Player 1 turn")
    while try_again == True:
        print("Enter the row and column you want to place your sign")
        l = [int(i) for i in input().strip().split()]
        if board[l[0], l[1]] == 0:
            board[l[0], l[1]] = 1
            try_again = False
        else:
            print("That place is already filled")
    print(board)
    
def player2_turn(board):
    try_again = True
    print("Player 2 turn")
    while try_again == True:
        print("Enter the row and column you want to place your sign")
        l = [int(i) for i in input().strip().split()]
        if board[l[0], l[1]] == 0:
            board[l[0], l[1]] = 2
            try_again = False
        else:
            print("That place is already filled")
    print(board)
    
def play_game():
    board = np.zeros((3,3), dtype = "int32")
    print(board)
    
    player1_turn(board)
    player2_turn(board)
    
    while True:
        player1_turn(board)
        if check_win(board) == True:
            print("Player 1 win")
            break
        player2_turn(board)
        if check_win(board) == True:
            print("Player 2 win")
            break
        
play_game()