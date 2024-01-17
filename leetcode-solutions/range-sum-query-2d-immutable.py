class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.psum = [ [0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.psum[r][c] = self.psum[r][c-1]+self.psum[r-1][c]-self.psum[r-1][c-1]+matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.psum[row2][col2] - self.psum[row2][col1-1]-self.psum[row1-1][col2]+self.psum[row1-1][col1-1]        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)