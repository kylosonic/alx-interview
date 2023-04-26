#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    '''scripts to rotate nxn 2D matrix clockwise
    Return: Nothing '''
    
  # step-1: transpose the matrix
  for i in range(len(matrix)):
    for j in range(i):
      matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

  # step-2: reverse the rows of the matrix
  N=len(matrix)
  for i in range(N//2):
    for j in range(N):
      matrix[i][j],matrix[N-1-i][j]=matrix[N-1-i][j],matrix[i][j]


if __name__ == "__main__":
  matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

  rotate_2d_matrix(matrix)

  print(matrix)
