class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        w = len(word) # 當index抵達w時，代表全部的字都被找到了
        path = set()

        def dfs(i, j, k):
            if k == w:
                return True
            if (i < 0 or i >= row 
                or j < 0 or j >= col
                or board[i][j] != word[k]
                or (i, j) in path):
                return False
            path.add((i, j))

            found = (dfs(i-1, j, k+1) or 
                   dfs(i+1, j, k+1) or 
                   dfs(i, j-1, k+1) or 
                   dfs(i, j+1, k+1))

            path.remove((i, j))
            return found 

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True


        return False