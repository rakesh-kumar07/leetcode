class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row_counts=[0]*m
        col_counts=[0]*n

        for r,c in indices:
            row_counts[r]+=1
            col_counts[c]+=1
        odd_rows=sum(r%2!=0 for r in row_counts)
        odd_cols=sum(c%2!=0 for c in col_counts)

        even_rows=m-odd_rows
        even_cols=n-odd_cols

        return odd_rows*even_cols+even_rows*odd_cols