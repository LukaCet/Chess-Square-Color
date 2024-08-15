def chess_square_color(square):
    column = square[0].lower()
    row = int(square[1])

    convert_column_to_number = ord(column) - ord('a') + 1
    if (row + convert_column_to_number) % 2 == 0:
        return "Black"
    else:
        return "White"
    
user_input = input("Enter a Chess Square such as E4, C6, H3: ")
color = chess_square_color(user_input)
print(f"{user_input.upper()} is {color}")
