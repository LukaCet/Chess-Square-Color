# Chess Square Color
Determine the color of a Chess Square, such as E4, F3, H6

## Understand the Chess Board:
To help visualise the Chess Board:
- [A proper Image of the Chess Board](https://www.google.com/search?client=opera-gx&hs=Yy1&sca_esv=82f832aba91fe7d7&sxsrf=ADLYWILQRhdJhKhzcSPp2pPNeoQhytJdBw:1723737093065&q=chess.com+chessboard&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2joQcoZ-0Q2Udkt2zEybT7HdNV1kobqvEwEVRYBCltlBtQd5-pPeakpVgpgEn2RgmgzeZo15rltNMrDtoZe63sl46hHJXZmfPBeZdqdwrtlSxkvce3I&sa=X&ved=2ahUKEwiA5viIrfeHAxW1RaQEHeEWAc8QtKgLegQIEBAB&cshid=1723737099491164&biw=1495&bih=715&dpr=1.25#vhid=XdVW6qO-5PBNcM&vssid=mosaic)
- [Understand the code](https://github.com/LukaCet/Chess-Square-Color/blob/main/ChessCode.py)

## Explanation:

Section 1:
```python
def chess_square_color(square): #A define function in order to find the color of the square
    column = square[0].lower()
    row = int(square[1]) # [0] and [1] is used to get the first and second character of the str respectively
```
Section 2:
```python
    convert_column_to_number = ord(column) - ord('a') + 1 #Here, I used the ord function and made a new variable to convert the column str variable into a number. So G, with a value of 103 would have a converted value of 7 because 103 - 97 (Value of 'a') + 1 = 7
    if (row + convert_column_to_number) % 2 == 0: # Now if the sum of the row and the converted column are even, then the answer is Black, otherwise it's White, so G6 for instance is white because 7 + 6 is not an even number.
        return "Black"
    else:
        return "White"
    
user_input = input("Enter a Chess Square such as E4, C6, H3: ")
color = chess_square_color(user_input)
print(f"{user_input.upper()} is {color}")
```
