# sudoku_game
This program validates a Sudoku board by ensuring it adheres to the rules of Sudoku. The program reads 9 rows of input, each containing 9 digits, and checks that each row, each column, and each of the nine 3x3 sub-squares contain all digits from 1 to 9. It uses helper functions to validate these conditions: one function checks if a group of digits contains exactly the digits from 1 to 9, and another extracts a 3x3 sub-square from the board. If all rows, columns, and sub-squares are valid, the program outputs "Yes"; otherwise, it outputs "No". This ensures the board is a valid Sudoku solution.
