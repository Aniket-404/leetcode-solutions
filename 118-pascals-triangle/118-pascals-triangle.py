from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates the first numRows of Pascal's triangle.
        
        In Pascal's triangle, each number is the sum of the two numbers 
        directly above it.
        """
        # Base case: If 0 rows are requested, return an empty list
        if numRows == 0:
            return []
        
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        # Start generating from the second row (index 1) up to numRows-1
        for i in range(1, numRows):
            # Get the previous row
            prev_row = triangle[-1]
            
            # Start the current row with 1
            current_row = [1]
            
            # Calculate the inner elements
            # Iterate from j=1 up to the second-to-last element of the previous row
            for j in range(1, len(prev_row)):
                # The element is the sum of the two elements directly above it
                new_element = prev_row[j-1] + prev_row[j]
                current_row.append(new_element)
            
            # End the current row with 1
            current_row.append(1)
            
            # Add the completed current row to the triangle
            triangle.append(current_row)
            
        return triangle