# Use Hashset
# Time: O(9^2) Space: O(9^2) Beacuse we are iterating through all over the grid
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # initializing hashmaps 
        col = collections.defaultdict(set) 
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set)  #key = (r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":   #if board is empty then continue
                    continue
                if (board[r][c] in row[r] or   #the current row that we are in, row is hash set and r is the key
                    board[r][c] in col[c] or #check for columns, if the current position is eqaul to that col
                    board[r][c] in squares[(r//3,c//3)]):  #check in the current square
                    return False
                #updating all the hashmaps
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
