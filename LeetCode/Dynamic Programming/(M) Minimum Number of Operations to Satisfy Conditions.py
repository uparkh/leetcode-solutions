
# @anushdubey01's solution, with my own notes
# Time: O(n*m*10) = O(n*m)
# Space: O(n*m*10) = O(n*m), can be shortened to O(m*10) = O(m)
# because we only need the previous column's values
class Solution:
    def minimumOperations(self, grid):
        n, m = len(grid), len(grid[0])
        count = [
            [
                # count[column][value] is the number of cells in column 'column'
                # that are different from 'value' AKA min number of operations to make all cells in
                # column 'column' equal to 'value'
                sum(
                    grid[row][column] != value for row in range(n)
                )
                for value in range(10)
            ]
            for column in range(m)
        ]
        # base case row
        dp = [[float('inf')] * 10 for _ in range(m)]
        dp.append([0] * 10)
        for column in range(m - 1, -1, -1):  # right to left
            for value in range(10):
                for i in range(10):
                    if i != value:
                        dp[column][value] = min(
                            # keep current?
                            dp[column][value],

                            # or is this val's count + changing next column to i lower?
                            count[column][value] + dp[column + 1][i]
                        )

        return min(dp[0])
