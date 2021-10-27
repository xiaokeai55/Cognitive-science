from copy import deepcopy
# reference: https://en.wikipedia.org/wiki/Minimax

# draw the chess board
def draw(board):
    l = len(board)
    for i in range(l):
        print("-------------")
        line = ''
        for j in range(l):
            line += "| "
            line += board[i][j]
            line += " "
        line += '|'
        print(line)
    print("-------------")

# AI win return 1
# Player win return 2
# tie return 0
# no result return -1
def check_win(grid):
    # check row
    for i in range(3):
        if grid[i][0] == grid [i][1] == grid[i][2]:
            if grid[i][0] == 'X':
                return 1
            elif grid[i][0] == 'O':
                return 2
    # check column
    for i in range(3):
        if grid[0][i] == grid [1][i] == grid[2][i]:
            if grid[0][i] == 'X':
                return 1
            elif grid[0][i] == 'O':
                return 2
    # check diagonal
    if grid[0][0] == grid [1][1] == grid[2][2]:
            if grid[0][0] == 'X':
                return 1
            elif grid[0][0] == 'O':
                return 2
    if grid[0][2] == grid [1][1] == grid[2][0]:
            if grid[0][2] == 'X':
                return 1
            elif grid[0][2] == 'O':
                return 2
            
    # check draw
    l = len(grid)
    for i in range(l):
        for j in range(l):
            if grid[i][j] == ' ':
                return -1
    return 0


def minimax(grid, turn) :
    # pseudocode for minimax algorithm
    '''
    function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
    '''
    
    win = check_win(grid)
 
    # check AI win
    if (win == 1) :
        return 10
 
    # check player win
    if (win == 2) :
        return -10
 
    # check draw
    if (win == 0) :
        return 0
 
    if (turn) :    
        value = -9999

        for i in range(3) :        
            for j in range(3) :

                if (grid[i][j] == ' ') :

                    grid[i][j] = 'X'

                    value = max( value, minimax(grid, False) )
 
                    grid[i][j] = ' '
        return value
 
    else :
        value = 9999
 
        for i in range(3) :        
            for j in range(3) :
              
                if (grid[i][j] == ' ') :
                 
                    grid[i][j] = 'O'
 
                    value = min(value, minimax(grid, True))
 
                    grid[i][j] = ' '
        return value

#check the next optimal step for AI
def next_step(grid):
    best = -9999
    ret = (-1, -1)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                tmp = deepcopy(grid)
                tmp[i][j] = 'X'
                score = minimax(tmp, False)
                if best < score:
                    best = score
                    ret = (i, j)
    return ret
    
def run(board):
    print('Game Start')
    print('AI: X')
    print('Player: O')
    print()
    draw(board)
    print('AI go first, try to beat AI')
    while True:
        # AI turn
        print('AI turn:')
        tmp = deepcopy(board)
        pos = next_step(tmp)
        board[pos[0]][pos[1]] = 'X'
        draw(board)
        win = check_win(board)
        if (win == 1) :
            print('AI wins!\n')
            break
        if (win == 0) :
            print('Tie!\n')
            break
        
        # Player turn
        print('\nPlayer turn:')
        print('Please enter the location')
        row, column = -1, -1
        while True:
            try:
                row = int(input('Row: ')) - 1
                column = int(input('Column: ')) - 1
            except:
                print('Invalid input, please enter integers between 1 ~ 3')
                continue
            if row > 2 or row < 0 or column > 2 or column < 0:
                print('Invalid input, please enter integers between 1 ~ 3')
                continue
            if board[row][column] != ' ':
                print('Location is not empty, please try again')
                continue
            break
        board[row][column] = 'O'
        draw(board)
        win = check_win(board)
        if (win == 2) :
            print('You win!\n')
            break
        if (win == 0) :
            print('Tie!\n')
            break
        print()
    
if __name__ ==  '__main__':
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        run(board)
        while True:
            rerun = input('Enter \'ok\' to play again, \'quit\' to exit ==> ')
            if rerun == 'quit' or rerun == 'ok':
                break
        if rerun == 'quit':
            break
