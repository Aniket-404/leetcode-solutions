class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        
        for i in range(1, rowIndex + 1):
            for k in range(i, 0, -1):
                row[k] = row[k] + row[k-1]
        
        return row