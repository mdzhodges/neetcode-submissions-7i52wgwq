class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ## so first need to find which array it is in, then do a binary search
        # could also do a BST to determine array



        # do a bst on row then a bst on colums

        left_row = 0
        right_row = len(matrix)

        row_count = 0


        while left_row < right_row:
            mid = (left_row + right_row) // 2
            
            if target < matrix[mid][0]:
                right_row = mid

            elif target > matrix[mid][len(matrix[mid])-1]:
                left_row = mid +1
            
            else:
                row_count = mid
                break



        left = 0
        right = len(matrix[row_count])

        while left < right:
            mid = (left + right)//2
            if matrix[row_count][mid] < target:
                left = mid+1
            elif matrix[row_count][mid] > target:
                right = mid

            elif matrix[row_count][mid] == target:
                return True
            



        return False;
                



        