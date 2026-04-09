class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row logic
        for i in board:
            row = Counter(i)
            for val in row:
                if row[val] > 1 and val != '.':
                    return False
        
        # column logic
        column_list = []
        for i in range(len(board)):
            for row in board:
                column_list.append(row[i])
            column_set = Counter(column_list)
            for val in column_set:
                if column_set[val] > 1 and val != '.':
                    return False
            column_list = []

        # box logic
        box_dict = {}
        for row in range(9):
            for column in range(9):
                val = board[row][column]
                if val != '.':
                    current_box = (row // 3, column // 3)
                    
                    if current_box not in box_dict:
                        box_dict[current_box] = []
                        
                    box_dict[current_box].append(val)
        
        for box_vals in box_dict.values():
            box_counts = Counter(box_vals)
            for val in box_counts:
                if box_counts[val] > 1:
                    return False

        return True