def print_table(table):
    print("_______________")
    for i in table:
        print(i)
    print("---------------")


def field_validation(table):
    while True:
        place_x = -1
        place_y = -1
        while place_x < 0 or place_x > len(table) - 1:
            try:
                place_x = int(input("Melyik sorba? ")) - 1
                if place_x < 0 or place_x > len(table) - 1:
                    print("A sor 1 és " + str(len(table)) + " közé essen!")
            except ValueError:
                print("1 és " + str(len(table)) + " közé eső SZÁMOT kell megadni!")
        while place_y < 0 or place_y > len(table) - 1:
            try:
                place_y = int(input("Melyik oszlopba? ")) - 1
                if place_y < 0 or place_y > len(table) - 1:
                    print("Az oszlop 1 és " + str(len(table)) + " közé essen!")
            except ValueError:
                print("1 és " + str(len(table)) + " közé eső SZÁMOT kell megadni!")
        if table[place_x][place_y] == "_":
            return {"x": place_x, "y": place_y}
            # volt szó róla, hogy akár dictionary-t is visszaadhatunk, hogy a 'main'-ben könnyebben érthető legyen
        else:
            print("Már foglalt")


def who_wins(sign, player_one, player_two):
    if sign == "X":
        winner = player_one
        return winner
    if sign == "O":
        winner = player_two
        return winner


def validation(table, sign, player_one, player_two):
    count = 0
    for i in table:
        for j in i:
            count += j.count("_")
    if count == 0:
        winner = "dontetlen"
        return winner
    for row in range(len(table)):
        if table[row][0] == sign and table[row][1] == sign and table[row][2] == sign:
            winner = who_wins(sign, player_one, player_two)
            return winner
    for column in range(len(table)):
        if table[0][column] == sign and table[1][column] == sign and table[2][column] == sign:
            winner = who_wins(sign, player_one, player_two)
            return winner
    if table[0][0] == sign and table[1][1] == sign and table[2][2] == sign:
        winner = who_wins(sign, player_one, player_two)
        return winner
    if table[0][2] == sign and table[1][1] == sign and table[2][0] == sign:
        winner = who_wins(sign, player_one, player_two)
        return winner


def main():
    player_one = input("Első játékos neve: ").title()
    player_two = input("Második játékos neve: ").title()
    player_one_sign = "X"
    player_two_sign = "O"
    table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    print_table(table)
    player_one_turn = True
    while True:
        if player_one_turn:
            sign = player_one_sign
            print("Te jössz " + player_one)
        else:
            sign = player_two_sign
            print("Te jössz " + player_two)
        player_position = field_validation(table)
        table[player_position["x"]][player_position["y"]] = sign
        print_table(table)
        winner = validation(table, sign, player_one, player_two)
        if winner == "dontetlen":
            print("Döntetlen!")
            break
        elif winner == player_one:
            print(player_one + " a győztes!")
            break
        elif winner == player_two:
            print(player_two + " a győztes!")
            break
        player_one_turn = not player_one_turn


main()
