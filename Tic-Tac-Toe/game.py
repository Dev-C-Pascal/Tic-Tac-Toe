from leaderboard import leaderboard_update

first_player = 'X'
second_player = 'O'
game_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def input_move():
    while True:
        try:
            row, column = map(int, input("Enter row and column [1-3 each, separated by space]: ").split())
            if 1 <= row <= 3 and 1 <= column <= 3:
                if game_field[row - 1][column - 1] == " ":
                    return row - 1, column - 1
                else:
                    print("This cell is already filled. Please try one more time.")
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")


def print_field():
    field = '-' * 11 + '\n'
    for row in game_field:
        field += '|'
        for cell in row:
            field += f' {cell} '
        field += '|\n'
    field += '-' * 11
    print(field)


def congratulate_player(winner):
    print(f"Congratulations! Player {winner} won!")


def check_winner():
    if game_field[0][0] == game_field[1][1] == game_field[2][2] != " ":
        return game_field[0][0]
    if game_field[0][2] == game_field[1][1] == game_field[2][0] != " ":
        return game_field[0][2]
    for i in range(3):
        if game_field[i][0] == game_field[i][1] == game_field[i][2] != " ":
            return game_field[i][0]
        if game_field[0][i] == game_field[1][i] == game_field[2][i] != " ":
            return game_field[0][i]
    return None


def check_player_name(name):
    with open("leaderboard.csv", "r") as file:
        for line in file:
            if name in line:
                print(f"Hi, {name}! Nice to see you again")
                return
    print(f"Hi, {name}! Good luck")
    add_player_to_leaderboard(name)
    return


def add_player_to_leaderboard(name):
    with open("leaderboard.csv", "a") as file:
        file.write(f"{name},0,0,0\n")


def game_processing(player1, player2):
    current_player = first_player
    game_is_over = 9
    counter = 0  # counter of our attempts, after 9 attempt the game will be finished

    while counter < game_is_over:
        row, column = input_move()
        game_field[row][column] = current_player
        print_field()
        winner = check_winner()
        current_player = first_player if current_player == second_player else second_player
        counter += 1

        if winner is not None:
            congratulate_player(winner)
            leaderboard_update(winner, player1, player2)
            break

    else:
        print("It's draw")
        leaderboard_update('draw', player1, player2)


def play_game():
    player1 = input("Enter the name of the first player: ")
    check_player_name(player1)
    player2 = input("Enter the name of the second player: ")
    check_player_name(player2)
    game_processing(player1, player2)
    return
