def clear_leaderboard():
    with open("leaderboard.csv", "w") as file:
        file.write("Player,win,draw,loss\n")
    print("Leaderboard cleared")
    return


def show_leaderboard():
    with open("leaderboard.csv", "r") as file:
        lines = file.readlines()

    headings = lines[0]
    lines = sorted(lines[1:], key=lambda x: (int(x.split(',')[1]), ((-1) * (int(x.split(',')[2]) + int(x.split(',')[3][:-1])))), reverse=True)

    player, win, draw, loss = headings.split(',')
    print(f"{player: <18}{win: <4}{draw: <5}{loss[:-1]: <4}")
    print('-' * 31)
    for line in lines:
        player, win, draw, loss = line.split(',')
        print(f"{player: <18}{win: <4}{draw: <5}{loss[:-1]: <4}")


def leaderboard_update(winner, player1_name, player2_name):
    with open("leaderboard.csv", "r") as file:
        old_lines = file.readlines()

    match winner:
        case 'X':
            leaderboard_update_winner(old_lines, player1_name, player2_name)
        case 'O':
            leaderboard_update_winner(old_lines, player2_name, player1_name)
        case 'draw':
            leaderboard_update_draw(old_lines, player1_name, player2_name)


def leaderboard_update_winner(old_lines, winner, looser):
    WIN = -3
    LOSS = -1

    with open("leaderboard.csv", "w") as file:
        for line in old_lines:
            if winner == line.split(',')[0]:
                line = line.split(',')
                line[-1] = line[-1][:-1]
                line[WIN] = str(int(line[WIN]) + 1)
                line_str = ','.join(line) + '\n'
                line = line_str

            elif looser == line.split(',')[0]:
                line = line.split(',')
                line[-1] = line[-1][:-1]
                line[LOSS] = str(int(line[LOSS]) + 1)
                line_str = ','.join(line) + '\n'
                line = line_str

            file.write(line)


def leaderboard_update_draw(old_lines, player1, player2):
    DRAW = -2

    with open("leaderboard.csv", "w") as file:
        for line in old_lines:
            if player1 == line.split(',')[0]:
                line = line.split(',')
                line[-1] = line[-1][:-1]
                line[DRAW] = str(int(line[DRAW]) + 1)
                line_str = ','.join(line) + '\n'
                line = line_str

            elif player2 == line.split(',')[0]:
                line = line.split(',')
                line[-1] = line[-1][:-1]
                line[DRAW] = str(int(line[DRAW]) + 1)
                line_str = ','.join(line) + '\n'
                line = line_str

            file.write(line)
