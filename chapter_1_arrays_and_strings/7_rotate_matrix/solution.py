# we have to rotate a matrix to 90 degree clockwise

def rotate_matrix(matrix):
    """
    matrix should be given as 2d array means 2d list
    like [[],[],[]]
    """
    height = len(matrix)
    width = len(matrix[0])
    newMatrix = [[0 for i in range(height)] for j in range(width)]
    for row in range(height):
        for col in range(width):
            newMatrix[col][(height-row-1)] = matrix[row][col]
        
    return newMatrix

print(rotate_matrix([[1,2,3],[4,5,6]]))            # ans: [[4, 1], [5, 2], [6, 3]]
print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))    # ans: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]