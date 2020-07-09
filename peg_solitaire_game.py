'''
Name: Aayush Ritesh Dani
Student ID: 9082015224
Net ID: ardani
'''


def readValidInt(string_prompt, minimum, maximum):

    while True:
        integer = input(string_prompt)

        if integer.isnumeric():
            integer = int(integer)
            if integer >= minimum and integer <= maximum:
                return integer

        print()


def createBoard(boardType):

    cross = [
                ['#','#','#','@','@','@','#','#','#'],
                ['#','#','#','@','@','@','#','#','#'],
                ['@','@','@','@','@','@','@','@','@'],
                ['@','@','@','@','-','@','@','@','@'],
                ['@','@','@','@','@','@','@','@','@'],
                ['#','#','#','@','@','@','#','#','#'],
                ['#','#','#','@','@','@','#','#','#'],
            ]

    circle = [
                ['#','-','@','@','-','#'],
                ['-','@','@','@','@','-'],
                ['@','@','@','@','@','@'],
                ['@','@','@','@','@','@'],
                ['-','@','@','@','@','-'],
                ['#','-','@','@','-','#'],
            ]

    traingle = [
                ['#','#','#','-','@','-','#','#','#'],
                ['#','#','-','@','@','@','-','#','#'],
                ['#','-','@','@','-','@','@','-','#'],
                ['-','@','@','@','@','@','@','@','-'],
            ]

    simpleT = [
                ['-','-','-','-','-'],
                ['-','@','@','@','-'],
                ['-','-','@','-','-'],
                ['-','-','@','-','-'],
                ['-','-','-','-','-'],
            ]

    if boardType == 1:
        return cross
    elif boardType == 2:
        return circle
    elif boardType == 3:
        return traingle
    elif boardType == 4:
        return simpleT
    else:
        # Handling invalid inputs
        return False


def displayBoard(board):

    print("  ", end="")
    for value in range(1, len(board[0])+1):
        print(value, end=" ")
    print()

    for row, row_value in enumerate(board):
        print(row+1, end=" ")
        for column, column_value in enumerate(board[row]):
            print(column_value, end=" ")
        
        print()


def readValidMove(board):

    rows = len(board)
    columns = len(board[0])

    column = input("Choose the COLUMN of a peg you'd like to move: ")
    if not column.isnumeric():
        while True:
            column = input(f"Please enter your choice as an integer between 1 and {columns}: ")

            if column.isnumeric():
                
                column = int(column)
                if column < 1 or column > columns:
                    continue
                else:
                    break
    else:
        column = int(column)

        if column < 1 or column > columns:
            while True:
                column = input(f"Please enter your choice as an integer between 1 and {columns}: ")

                if column.isnumeric():
                    
                    column = int(column)
                    if column < 1 or column > columns:
                        continue
                    else:
                        break

    row = input("Choose the ROW of a peg you'd like to move: ")
    if not row.isnumeric():
        while True:
            row = input(f"Please enter your choice as an integer between 1 and {rows}: ")

            if row.isnumeric():
                
                row = int(row)
                if row < 1 or row > rows:
                    continue
                else:
                    break
    else:
        row = int(row)

        if row < 1 or row > rows:
            while True:
                row = input(f"Please enter your choice as an integer between 1 and {rows}: ")

                if row.isnumeric():
                    
                    row = int(row)
                    if row < 1 or row > rows:
                        continue
                    else:
                        break

    direction = input("Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT: ")
    if not direction.isnumeric():
        while True:
            direction = input("Please enter your choice as an integer between 1 and 4: ")

            if direction.isnumeric():

                direction = int(direction)
                if direction < 1 or direction > 4:
                    continue

                if direction == 1 and row == 1:
                    print("\nMoving UP from row 1 is an illegal move.\n\n")
                    readValidMove(board)
                elif direction == 2 and row == rows:
                    print(f"\nMoving DOWN from row {rows} is an illegal move.\n\n")
                    readValidMove(board)
                elif direction == 3 and column == 1:
                    print("\nMoving LEFT from column 1 is an illegal move.\n\n")
                    readValidMove(board)
                elif direction == 4 and column == columns:
                    print(f"\nMoving RIGHT from column {columns} is an illegal move.\n\n")
                    readValidMove(board)

    else:
        direction = int(direction)

        if direction < 1 or direction > 4:
            while True:
                direction = input("Please enter your choice as an integer between 1 and 4: ")

                if direction.isnumeric():
                    
                    direction = int(direction)
                    if direction < 1 or direction > 4:
                        continue
                    
                    if direction == 1 and row == 1:
                        print("\nMoving UP from row 1 is an illegal move.\n\n")
                        readValidMove(board)
                    elif direction == 2 and row == rows:
                        print(f"\nMoving DOWN from row {rows} is an illegal move.\n\n")
                        readValidMove(board)
                    elif direction == 3 and column == 1:
                        print("\nMoving LEFT from column 1 is an illegal move.\n\n")
                        readValidMove(board)
                    elif direction == 4 and column == columns:
                        print(f"\nMoving RIGHT from column {columns} is an illegal move.\n\n")
                        readValidMove(board)

    return row-1, column-1, direction


def isValidMove(board, row, column, direction):
    
    if direction == 1:
        targetRow = row - 1
        targetColumn = column
    elif direction == 2:
        targetRow = row + 1                                                                                                 
        targetColumn = column
    elif direction == 3:
        targetRow = row
        targetColumn = column - 1
    else:
        targetRow = row
        targetColumn = column + 1

    invalid = True

    try:
        if board[targetRow][targetColumn] == "@":
            if direction == 1:
                if targetRow - 1 >= 0:
                    if board[targetRow-1][targetColumn] == "-":
                        invalid = False

            elif direction == 2:
                if targetRow + 1 <= len(board)-1:
                    if board[targetRow+1][targetColumn] == "-":
                        invalid = False

            elif direction == 3:
                if targetColumn - 1 >= 0:
                    if board[targetRow][targetColumn-1] == "-":
                        invalid = False

            else:
                if targetColumn + 1 <= len(board[0])-1:
                    if board[targetRow][targetColumn+1] == "-" :
                        invalid = False

    except Exception as error:
        # Rows and Columns which fall out of range
        pass

    if invalid:
        return False

    return True


def performMove(board, row, column, direction):

    if direction == 1:
        board[row-1][column] = "-"
        board[row][column] = "-"
        board[row-2][column] = "@"

    elif direction == 2:
        board[row+1][column] = "-"
        board[row][column] = "-"
        board[row+2][column] = "@"

    elif direction == 3:
        board[row][column-1] = "-"
        board[row][column] = "-"
        board[row][column-2] = "@"

    else:
        board[row][column+1] = "-"
        board[row][column] = "-"
        board[row][column+2] = "@"


def countPegsRemaining(board):
    
    pegs_count = 0

    for row, row_value in enumerate(board):
        for column, column_value in enumerate(board[row]):
            if column_value == "@":
                pegs_count += 1

    return pegs_count


def countMovesAvailable(board):
    moves = 0

    for row, row_value in enumerate(board):
        for column, column_value in enumerate(board[row]):
            if column_value == "@":
                upwards_check = isValidMove(board, row, column, 1)
                downwards_check =  isValidMove(board, row, column, 2)
                left_check = isValidMove(board, row, column, 3)
                right_check = isValidMove(board, row, column, 4)

                if upwards_check:
                    moves += 1
                if downwards_check:
                    moves += 1
                if left_check:
                    moves += 1
                if right_check:
                    moves += 1

    return moves


def main():
    print('''\nWELCOME TO CS300 PEG SOLITAIRE!
===============================\n''')


    board_choice = readValidInt('''Board Style Menu
1) Cross
2) Circle
3) Triangle
4) Simple T
Choose a board style: ''', 1, 4)
    
    board = createBoard(board_choice)
    
    direction_converstion = {
        1: "UP",
        2: "DOWN",
        3: "LEFT",
        4: "RIGHT"
    }

    while True:
        print()

        if countPegsRemaining(board) == 1:
            displayBoard(board)
            print()

            print("Congrats, you won!\n")

            while True:
                restart_check = input("Do you want to play again? (1- Restart, 2- Quit): ")

                if restart_check.isnumeric():
                    restart_check = int(restart_check)

                    if restart_check > 2 or restart_check < 1:
                        continue

                    if restart_check == 1:
                        print("\n\n\n")
                        main()
                    else:
                        print('''\n==========================================
THANK YOU FOR PLAYING CS300 PEG SOLITAIRE!\n''')
                        break
            break


        if countMovesAvailable(board):
            displayBoard(board)

            row, column, direction = readValidMove(board)

            if not isValidMove(board, row, column, direction):
                print(f"Moving a peg from row {row+1} and column {column+1} {direction_converstion[direction]} is not currently a legal move.")
                continue

            performMove(board, row, column, direction)
        else:
            displayBoard(board)
            print()

            print("It looks like there are no more legal moves.  Please try again.\n")
            
            while True:
                restart_check = input("Do you want to play again? (1- Restart, 2- Quit): ")

                if restart_check.isnumeric():
                    restart_check = int(restart_check)

                    if restart_check > 2 or restart_check < 1:
                        continue

                    if restart_check == 1:
                        print("\n\n\n")
                        main()
                    else:
                        print('''\n==========================================
THANK YOU FOR PLAYING CS300 PEG SOLITAIRE!\n''')
                        break
            break

main()