def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    copyMatrix = matrix
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]==0:
                
                # setting all row elements to 0
                for i in range(col):
                    copyMatrix[row][i] = 0
                #setting all col elements to 0
                for i in range(row):
                    copyMatrix[i][col] = 0
    return copyMatrix


## Testing
our_matrix = [
    [1, 2, 3, 4, 0],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 0, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
returned_matrix = zero_matrix(our_matrix)
for i in range(len(returned_matrix)):
    for j in range(len(returned_matrix[0])):
        print(f"{returned_matrix[i][j]:3d}", end='')
    print('')