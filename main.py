cells = {
    "a1": " ",
    "b1": " ",
    "c1": " ",
    "a2": " ",
    "b2": " ",
    "c2": " ",
    "a3": " ",
    "b3": " ",
    "c3": " ",
}


def move_wins():
    if cells["a1"] == turn and cells["a2"] == turn and cells["a3"] == turn:
        return True
    elif cells["a1"] == turn and cells["b1"] == turn and cells["c1"] == turn:
        return True
    elif cells["a1"] == turn and cells["b2"] == turn and cells["c3"] == turn:
        return True
    elif cells["a2"] == turn and cells["b2"] == turn and cells["c2"] == turn:
        return True
    elif cells["a3"] == turn and cells["b2"] == turn and cells["c1"] == turn:
        return True
    elif cells["a3"] == turn and cells["b3"] == turn and cells["c3"] == turn:
        return True
    elif cells["b1"] == turn and cells["b2"] == turn and cells["b3"] == turn:
        return True
    elif cells["c1"] == turn and cells["c2"] == turn and cells["c3"] == turn:
        return True
    else:
        return False


def print_board_state():
    print(
        f"""
           a     b     c
              |     |     
        1  {cells["a1"]}  |  {cells["b1"]}  |  {cells["c1"]}  
         _____|_____|_____
              |     |     
        2  {cells["a2"]}  |  {cells["b2"]}  |  {cells["c2"]}  
         _____|_____|_____
              |     |     
        3  {cells["a3"]}  |  {cells["b3"]}  |  {cells["c3"]}  
              |     |      
        """
    )


turn = "X"
game_active = True
while game_active:

    print_board_state()

    # Check if there are any remaining cells
    if not bool({key: " " for (key, value) in cells.items() if value == " "}):
        print("No cells available. No one wins :(")
        if input("Play again? (y/n): ").lower() == "y":
            cells = {key: " " for (key, value) in cells.items()}
            turn = "X"
        else:
            game_active = False
    # Cells available, make a move...
    else:
        turn_not_complete = True
        while turn_not_complete:
            new_position = input(f"It's {turn}'s turn. Choose an available cell (e.g. 'a1'): ").lower()
            # Check if valid move
            if new_position not in cells:
                print("Invalid cell. Try again.")
                continue
            elif cells[new_position] == "X" or cells[new_position] == "O":
                print("That's already taken. Try again.")
                continue
            # It's valid, make the move
            cells[new_position] = turn
            # Check if we have a winner
            if move_wins():
                print_board_state()
                print(f"{turn} wins. Nice!")
                if input("Play again? (y/n): ").lower() == "y":
                    cells = {key: " " for (key, value) in cells.items()}
                    turn = "X"
                else:
                    game_active = False
            # Last move didn't win, change player turn
            else:
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
            turn_not_complete = False
