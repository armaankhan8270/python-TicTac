
def printboard(xstate, ostate):
    zero = 'x' if xstate[0] else ('O' if ostate[0]else 0)
    one = 'x' if xstate[1] else ('O' if ostate[1]else 1)
    two = 'x' if xstate[2] else ('O' if ostate[2]else 2)
    three = 'x' if xstate[3] else ('O' if ostate[3]else 3)
    four = 'x' if xstate[4] else ('O' if ostate[4]else 4)
    five = 'x' if xstate[5] else ('O' if ostate[5]else 5)
    six = 'x' if xstate[6] else ('O' if ostate[6]else 6)
    seven = 'x' if xstate[7] else ('O' if ostate[7]else 7)
    eight = 'x' if xstate[8] else ('O' if ostate[8]else 8)
    # one=  'x' if xstate[9] else ('O' if ostate[9]else 9)
    print(f" {zero} | {one} | {two}")
    print(f" {three} | {four} | {five}")
    print(f" {six} | {seven} | {eight}")


def sum(a, b, c):
    return a+b+c


def checkwin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("X Won the match")
            return 1
        if (sum(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1


if __name__ == '__main__':
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("xchance")
    print("www")
    while (True):
        printboard(xstate, ostate)
        if (turn == 1):
            print("xchances")
            value = int(input("pleas enter a value"))
            xstate[value] = 1
        else:
            print("ochances")
            value = int(input("pleas enter a value"))
            ostate[value] = 1
        cwin = checkwin(xstate, ostate)
        if (cwin != -1):
            print("over")
            break

        turn = 1-turn
