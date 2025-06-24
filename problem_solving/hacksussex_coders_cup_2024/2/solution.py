# Check if every row and column contains all numbers
# An n x n matrix is valid if every row and every column 
# contains all the integers form 1 to n (inclusive)
# Given an n x n integer matrix matrix, return true
# if the matrix is valid. Otherwise, return false.

# Example 1:
# Input: matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
# Output: true

# Explanation: In this case, n = 3, and every row and column
# contains the numbers 1, 2, and 3.
# Hence, we return true.
def check_bounds(num: int, bound: int):
  if num > bound or num < 1:
    return False
  return True

def solution(matrix):
  row = []
  column = []
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if matrix[i][j] in row:
        return False
      elif check_bounds(matrix[i][j], len(matrix)) == False:
        return False
      else:
        row.append(matrix[i][j])
    for k in range(len(matrix)):
      if matrix[k][i] in column:
        return False
      elif  check_bounds(matrix[k][i], len(matrix)) == False:
        return False
      else:
        column.append(matrix[k][i])
    row.clear()
    column.clear()
  return True

if __name__ == '__main__':
  matrices = [
      [[1, 2, 3],
      [3, 1, 2],
      [2, 3, 1]],

      [[1, 2, 3],
      [1, 2, 2],
      [2, 3, 1]],

      [[1, 2, 3],
      [3, 1, 2],
      [1, 3, 1]],

      [[1]],

      [[1, 2],
      [2, 1]],

      [[1, 1],
      [2, 2]],

      [[1, 2, 3, 4],
      [2, 3, 4, 1],
      [3, 4, 1, 2],
      [4, 1, 2, 3]],

      [[1, 2, 3, 4],
      [2, 3, 4, 1],
      [3, 4, 1, 2],
      [4, 4, 2, 3]],

      [[1, 2, 3, 4],
      [2, 3, 4, 1],
      [3, 4, 1, 2],
      [1, 1, 2, 3]],

      [[5, 5, 5],
      [5, 5, 5],
      [5, 5, 5]],

      [[1, 2, 3],
      [1, 2, 3],
      [1, 2, 3]],

      [[1, 2, 3],
      [2, 3, 4],
      [3, 1, 2]]
  ]

  for matrix in matrices:
    print(solution(matrix))