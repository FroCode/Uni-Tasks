def next_generation(board):
    n, m = len(board), len(board[0])
    new_board = [['.' for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            alive_neighbors = 0
            
            # Counting alive neighbors
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == y == 0:
                        continue
                    ni, nj = (i + x) % n, (j + y) % m
                    if board[ni][nj] == 'X':
                        alive_neighbors += 1
            
            # Applying the rules of Game of Life
            if board[i][j] == 'X' and alive_neighbors in [2,3]:
                new_board[i][j] = 'X'
            elif board[i][j] == '.' and alive_neighbors == 3:
                new_board[i][j] = 'X'

    return new_board

# Example usage:
initial_board = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.'],
    ['.', 'X', '.', 'X', '.', '.'],
    ['.', '.', 'X', 'X', '.', '.'],
    ['.', '.', '.', '.', ".", "."]
]

next_gen_board = next_generation(initial_board)
for row in next_gen_board:
    print(''.join(row))


# To determine the number of live neighbors for the cell in the second row and nineteenth column in the thirty-seventh generation, 
# we would need to know the initial configuration of the board. Without this information
# it is impossible to provide an accurate answer.
#Sooo
# The Game of Life is known for its complex and unpredictable behavior, 
# and it is difficult to predict exactly when a particular pattern will stabilize. However, 
# some patterns are known to be stable or oscillating. 
# For example, the “block” pattern is a stable pattern that remains unchanged from one generation to the next.
#     The “blinker” pattern is an oscillating pattern that alternates between two states every two generations.