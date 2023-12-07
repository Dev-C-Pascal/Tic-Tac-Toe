from game import play_game
from leaderboard import clear_leaderboard, show_leaderboard


def input_command():
    return input("Enter command: ")


def main():
    print("Welcome to Tic Tac Toe! You can enter 'help' to see the list of available commands")

    while True:
        command = input_command()

        match command:

            case "clear leaderboard":
                clear_leaderboard()

            case "show leaderboard":
                show_leaderboard()

            case "play game":
                play_game()

            case "help":
                print("Available commands:")
                print("clear leaderboard - clears the leaderboard")
                print("show leaderboard - shows the leaderboard")
                print("play game - starts a game")
                print("help - shows this message")
                print("exit - exits the game")

            case "exit":
                print("Program exited")
                exit(0)

            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
