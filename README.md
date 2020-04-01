# ConnectX

Variant of connect 4 with arbitrary game board size and win-length

Inputs: Board X, Board Y, Win Length... player count?!
Examples:
 - ConnectX(3,3,3)
 - ConnectX(10,8,4)

Win condition:
 - A player has an uninterrupted run of win_length
 
Lose/tie condition:
 - oh god no

Constraints / error conditions:
 - Win length must be less than or equal to board max dimension in X/Y/diag
 - Board should not take more than 1s to process on each turn
 - Min/max sizes. Min = 3, Max = 100

Likely modules
