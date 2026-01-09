def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(n):
  l=[]
  for i in range(n):
    l2=[]
    for j in range(n):
      l2.append(' ')
    l.append(l2)
  return l

def get_location(n,board):
  while True:
    r=input(f'Enter a row index between 0 and {n-1}: ')
    c=input(f'Enter a column index between 0 and {n-1}: ')
    if r.isdigit()==False or c.isdigit()==False:
      print(f'({r}, {c}) is not a legal input!')
      continue
    elif int(r)>n-1 or int(r)<0 or int(c)>n-1 or int(c)<0:
      print( f'({int(r)}, {int(c)}) is not a legal space!')
      continue
    elif board[int(r)][int(c)]!=' ':
      print( f'({int(r)}, {int(c)}) is not an available space!')
      continue
    else:
      break
  return (int(r),int(c))


  
def row_win(n,board,player):
  
  for i in board:
    count=0
    for j in i:
      if j==player:
        count+=1
    if count==n:
      return True
    

def column_win(n,board,player):
  count=0
  for i in range(n):
    str=''
    for j in board:
      str+=j[i]
    if str==n*player:
      count+=1
      return True
  if count==0:
    return False  

def diag_win(n,board,player):
  str=''
  for i in range(0,n):
    str+=board[i][i]
  if str==n*player: 
    return True
  else:
    return False

def anti_diag_win(n,board,player):
  str=''
  for i in range(n):
    str+=board[i][(n-1)-i]
  if str==n*player:
    return True
  else:
    return False

def has_won(n,board,player):
  l=[]
  l.append(row_win(n,board,player))
  l.append(column_win(n,board,player))
  l.append(diag_win(n,board,player))
  l.append(anti_diag_win(n,board,player))
  if True in l:
    return True
  else:
    return False

# Test column win for player 'X'
board = [
    ['X', 'O', 'O'],
    ['X', 'O', 'X'],
    ['X', 'X', 'O']
]
assert has_won(3, board, 'X') == True # Assertion error if this is false

# Test diagonal win for player 'X'
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'X'],
    ['X', 'O', 'O']
]
assert has_won(3, board, 'X') == True # Assertion error if this is false

# Test no win for player 'X'and player 'O'
board = [
    ['O', 'O', 'X'],
    ['X', 'X', 'O'],
    ['O', 'O', 'X']
]
assert has_won(3, board, 'X') == False # Assertion error if this is true


def play_game(n):
  print(f'*** Welcome to {n} by {n} Tic-Tac-Toe ***')
  board=make_empty_board(n)
  print_board(n, board)
  while True:
    
    print("* X's turn *")

    index_X=get_location(n,board)

    board[index_X[0]][index_X[1]]=board[index_X[0]][index_X[1]].replace(' ','X')

    print_board(n, board)

    if has_won(n,board,'X')==True:
      print(f'X wins!')
      break

    count=0
    for i in board:
      for j in i:
        if j!=' ':
          count+=1
    if count==n**2:
      print('Tie!')
      break
    
    
    print("* O's turn *")

    index_O=get_location(n,board)

    board[index_O[0]][index_O[1]]=board[index_O[0]][index_O[1]].replace(' ','O')

    print_board(n, board)

    if has_won(n,board,'O')==True:
      print(f'O wins!')
      break

    count=0
    for i in board:
      for j in i:
        if j!=' ':
          count+=1
    if count==n**2:
      print('Tie!')
      break
    


n=int(input('Enter the size of the Tic-Tac-Toe board (n x n): '))
print('\n') 
play_game(n)   
  
    
      



