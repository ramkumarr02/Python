# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:00:30 2016

@author: ramrajagopalan

This code is added to GIT Repo

Branch 2 is created

"""

##---------------------------------------------------------------------------------------------------------


def tictactoe():    
    
    '''
    A TicTacToe Game
    '''
   ##-------------------------------------------------------
   ##Variables
       
    global matrix
    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,8,9]
    matrix = [row1,row2,row3]
   
    global game_flag
    game_flag = 'Open'   
    
    global position_dict
    position_dict = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

    global player
    
    global position_single
    global position_single_list
    global round_counter
    round_counter = 0
    
    global player_mark
    
    position_single_list = [1,2,3,4,5,6,7,8,9]
    
   ##------------------------------------------------------
   ##Main Code
    
   
    import os
    os.system('cls')
    
        
    print "Welcome to TicTacToe Game"
    print "-------------------------"
        
    for row in matrix:
        print row
                             
    while game_flag <> 'Gameover':
        position_single = getinput('X')
        validategame(position_single,"X")

        position_single = getinput('O')
        validategame(position_single,"O")        
    
    
##---------------------------------------------------------------------------------------------------------

def getinput(player):
    
    global round_counter
    
    if round_counter < 9:
        round_counter = round_counter + 1
        position_single = input("Player {}'s turn, Please enter your choice of position : ".format(player))
    elif round_counter >= 9:
        print "Game over : Draw"
        endgame()
            

    #Validate input------------------------------------------------------------------------------------------
    
    if position_single not in position_single_list:
        while position_single not in position_single_list:
            position_single = input("Wrong position, Please enter your choice from the above grid ")  
        
    return position_single
##---------------------------------------------------------------------------------------------------------

def validategame(position_single,player_mark):
    x = position_dict[position_single][0]
    y = position_dict[position_single][1]        
        
    matrix[x][y] = player_mark    
    
    if (matrix[0][0] == matrix[0][1] == matrix[0][2]) or \
       (matrix[1][0] == matrix[1][1] == matrix[1][2]) or \
       (matrix[2][0] == matrix[2][1] == matrix[2][2]) or \
       (matrix[0][0] == matrix[1][0] == matrix[2][0]) or \
       (matrix[0][1] == matrix[1][1] == matrix[2][1]) or \
       (matrix[0][2] == matrix[1][2] == matrix[2][2]) or \
       (matrix[0][0] == matrix[1][1] == matrix[2][2]) or \
       (matrix[0][2] == matrix[1][1] == matrix[2][0]):
        for row in matrix:
            print row        
                
        global game_flag
        #game_flag = 'Gameover'
        
        print "Game over : Player {} wins\n\n".format(player_mark)    
        endgame()
    
    else:
        for row in matrix:
            print row


##---------------------------------------------------------------------------------------------------------

def endgame():
    
    import sys    
    sys.exit(0)
         

 ##---------------------------------------------------------------------------------------------------------
            
tictactoe()

