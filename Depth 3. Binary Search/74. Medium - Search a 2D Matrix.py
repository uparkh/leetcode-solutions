# My Solution

# Notes:
# Can't concatenate row arrays -> single array, would be an O(m) operation
# Can't run binary search on each row, would be an O(m * log(n)) operation
# Probably can just convert coordinates into a single integer, and vice versa, to
# pretend like I'm working with a single unnested array.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, self.convertToMatrixIndex(matrix, (len(matrix)-1, len(matrix[0])-1))
        while l <= r:
            middleIndex = (l+r)//2
            middleTuple = self.convertToMatrixCoords(matrix, middleIndex)
            if target < matrix[middleTuple[0]][middleTuple[1]]:
                r = middleIndex - 1
            elif target > matrix[middleTuple[0]][middleTuple[1]]:
                l = middleIndex + 1
            else:
                return True
        return False
    
    def convertToMatrixCoords(self, matrix: list[list[int]], index: int) -> tuple:
        row = index // len(matrix[0])
        return (row, index - row*len(matrix[0]))
    
    def convertToMatrixIndex(self, matrix: list[list[int]], coords: tuple) -> int:
        return coords[0]*len(matrix[0]) + coords[1]

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 20))

# NeetCode's Solution
# Their solution utilizes the second property in order to perform two binary searches.
# The first one narrows down the specific row that the target will be in, while the second
# does a normal binary search through that row.

# The first loop works because we know that the first integer of any row is bigger than 
# the last integer of the row before that one. So, we can narrow down which row the target will be
# in.

# This algorithm definitely is much more efficient space-wise, because intermediary tuples
# and conversions are not needed, and we are working with just integers.

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         ROWS, COLS = len(matrix), len(matrix[0])

#         top, bot = 0, ROWS - 1
#         while top <= bot:
#             row = (top + bot) // 2
#             if target > matrix[row][-1]:
#                 top = row + 1
#             elif target < matrix[row][0]:
#                 bot = row - 1
#             else:
#                 break

#         if not (top <= bot):
#             return False
#         row = (top + bot) // 2
#         l, r = 0, COLS - 1
#         while l <= r:
#             m = (l + r) // 2
#             if target > matrix[row][m]:
#                 l = m + 1
#             elif target < matrix[row][m]:
#                 r = m - 1
#             else:
#                 return True
#         return False

