class Solution(object):
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = rows - 1

        while low <= high:
            mid = (low + high) // 2

            # Find maximum element in row mid
            max_col = 0

            for j in range(cols):
                if mat[mid][j] > mat[mid][max_col]:
                    max_col = j

            # Values above and below
            up = mat[mid - 1][max_col] if mid > 0 else -1
            down = mat[mid + 1][max_col] if mid < rows - 1 else -1

            # Peak found
            if mat[mid][max_col] > up and mat[mid][max_col] > down:
                return [mid, max_col]

            # Move upward
            elif up > mat[mid][max_col]:
                high = mid - 1

            # Move downward
            else:
                low = mid + 1