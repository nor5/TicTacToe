import math
import time
import random
#####Board class#####
class Board():
    def __init__(self):
        self.board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        
    def printBoard(self):
        for position in self.board:
             print(' | '.join(position))

    
    def insertLetter(self, position, letter):
        for row in self.board :
            for val in row:
                
                if  val ==  position :
                    row[row.index(val)] = letter
##                    print( f" {letter } has choose  { position}   row[] {row[row.index(position)]}")

    
    def   availablePosition(self):
        positionList=[]
        for row in self.board :
            for P in row:
                
              if  P in [str(i) for i in range(9)]:
                  #print(f' t is :{t}  and g is: {g}' )
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
            return True
         col_ind = int(position) % 3
         column = [row[col_ind ]  for row in self.board]     
         if all([s == letter for s in column]):
            return True
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
            return True
         if all([s == letter for s in diagonal2]):
            return True
         
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




        
o_player = ComputerPlayer('O')
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
            if game.winner(position, player.letter) :
                print(f"{player.letter} wins")
                return True
                
                

while not winner  and game.availablePosition() :
   
    if  player == o_player:
        player = x_player
        x = play(player, game)
        if x  :
                winner = True
    else:
        
        player =o_player
        o = play(player, game)
        if o  :
                winner = True
    
    time.sleep(.8)         
if not o and not x and  not game.availablePosition():
     print("it is a tie")

