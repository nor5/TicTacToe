#Tic TAc Toe AI game using a minimax algorithme, smart computer win or tie but never lose
import math
import time
import random
#####Board class#####
class Board():
    def __init__(self):
        self.board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        self.current_winner = None
    def printBoard(self):
        for position in self.board:
             print(' | '.join(position))

    
    def insertLetter(self, position, letter):
        for row in self.board :
            for val in row:
                
                if  val ==  position :
                    row[row.index(val)] = letter
                    if self.winner(position, letter):
                       self.current_winner = letter

    def undomove(self,position):
        
        sim_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in sim_board:     

             for val in row:
                    
                    if  val ==  position :
                        i = sim_board.index(row)
                        j = row.index(val)
        
                        self.board[i][j] = position


        
    
    def   availablePosition(self):
        positionList=[]
        for row in self.board :
            for P in row:
                
              if  P in [str(i) for i in range(9)]:
                
                  
                  positionList.append(P)
          
        if len(positionList) == 0:
            return False
        else:
            return {'availabe position':positionList, 'num_empty_squar' : len(positionList)}
         
    
    def  validPosition(self, position):
           
            if position in self.availablePosition()['availabe position']:
                return True
            else:
                return False
            
   

    def winner(self, position, letter):
         row_ind = math.floor(int(position )/ 3)
         row = self.board[row_ind]
         if all([s == letter for s in row]):
            return letter
         col_ind = int(position) % 3
         column = [row[col_ind ]  for row in self.board]     
         if all([s == letter for s in column]):
            return letter
         diagonal1=[]
         diagonal2=[]
         i=0
         j=2
         for row in self.board:
              diagonal1.append(row[i] )
              diagonal2.append(row[j])
              i=i+1
              j=j-1
         if all([s == letter for s in diagonal1]):
            return letter
         if all([s == letter for s in diagonal2]):
            return letter
         
         return False
###player section########

class Player():
    def __init__(self, letter):
        self.letter = letter
    def  position(self):
        pass
    
class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def position(self, game ):
        valid_position = True
       
        while  valid_position:
            position = input(self.letter + '\' s turn. Choose a position in (0, 8)')
            try:

                if position not in game.availablePosition()['availabe position']:
                    raise ValueError
                valid_position = False

            except ValueError:
                print('Invalid position. Try again.')
            
        return position
                
class ComputerPlayer(Player):                    
         def __init__(self,letter):
             super().__init__(letter)

         def  position(self, game):
             position = random.choice(game.availablePosition()['availabe position'])
            
             return str(position)



class smartComputer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def position(self, game):
        if game.availablePosition()['num_empty_squar'] == 9:
            position = random.choice(game.availablePosition()['availabe position'])
           
        else:
            position = self.minimax(game, self.letter)['position']
        return str(position)

    def minimax(self, board, player):
        max_player = self.letter #computer player
        other_player = "O" if player == "X" else "X"
        #chek for every move if there is a winner
        if board.current_winner  == other_player and board.availablePosition() :
            #defin score with the empty square in state
            return {'position':None, 'score':1*(game.availablePosition()['num_empty_squar'] + 1 ) if other_player == max_player
                        else   -1*(board.availablePosition()['num_empty_squar'] +1)}
         #check if the board is full      
        elif  not board.availablePosition():
            return{'position':None, 'score':0}

        if player == max_player:
            best ={'position':None, 'score': -math.inf}
        else:
            best = {'position':None, 'score': math.inf}
        for possible_move in board.availablePosition()['availabe position']:
            board.insertLetter(possible_move, player)
            simulate = self.minimax(board, other_player)#simulate the game
            board.undomove(possible_move) # undo the move by replacing the letter by the position number
            board.current_winner = None
            simulate['position'] = possible_move
            if player == max_player:
              if simulate['score'] > best['score']: #maximising the max palyer
                  best = simulate
            else:
               if  simulate['score'] < best['score']: #minimising the other
                    best = simulate

        return best
        




        
o_player = smartComputer('O')
x_player = HumanPlayer('X')
player = o_player
game= Board()
winner= False
availablePosition = True
print('Start the Tic Tac Toe game')
game.printBoard()

def play(player, game):
            position = player.position(game)

            game.insertLetter(position, player.letter)
            print(f" #####  {player.letter}  choose: <{position}>#######")
            game.printBoard()
            if game.winner(position, player.letter) ==  player.letter:
                print(f"{player.letter} wins")
                
                return True
                
                

while not winner  and game.availablePosition() :
   
    if  player == o_player:
        player = x_player
        x = play(player, game)
        if x:
            winner = True
    else:
        
        player =o_player
        o = play(player, game)
        if o:
            winner = True
       
    time.sleep(.8)         
if  winner == False and  not game.availablePosition():
     print("it is a tie")































