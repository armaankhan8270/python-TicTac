
def printboard(xstate, ostate):
    one = 'x' if xstate[0] else ('o' if ostate[0]else 0)
    two = 'x' if xstate[1] else ('o' if ostate[1]else 1)
    three = 'x' if xstate[2] else ('o' if ostate[2]else 2)
    f = 'x' if xstate[3] else ('o' if ostate[3]else 3)
    fi = 'x' if xstate[4] else ('o' if ostate[4]else 4)
    s = 'x' if xstate[5] else ('o' if ostate[5]else 5)
    se = 'x' if xstate[6] else ('o' if ostate[6]else 6)
    e = 'x' if xstate[7] else ('o' if ostate[7]else 7)
    n = 'x' if xstate[8] else ('o' if ostate[8]else 8)
    # one=  'x' if xstate[9] else ('o' if ostate[9]else 9)
    print(f" {one} | {two} | {three}")
    print(f" {f} | {fi} | {s}")
    print(f" {se} | {e} | {n}")


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
        turn = 1-turn
