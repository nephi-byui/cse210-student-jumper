def draw_parachute(hp):

    hits_taken = 4 - hp
    # base drawing

    if hp > 0:
        parachute_ascii = [ "  ___  ",
                            " /___\ ",
                            " \   / ",
                            "  \ /  ",
                            "   0   ",
                            "  /|\  ",
                            "  / \  ",
                            "       ", 
                            "^^^^^^^" ]
        for i in range(0, hits_taken):
            parachute_ascii[i] = "       "

    elif hp == 0:
        parachute_ascii = [ "       ",
                            "       ",
                            "       ",
                            "       ",
                            "   X   ",
                            "  /|\  ",
                            "  / \  ",
                            "       ", 
                            "^^^^^^^" ]

    # print the output
    for line in parachute_ascii:
            print(line)

def main():
    print("Drawing parachute at 4 HP:")
    draw_parachute(4)
    print()

    print("Drawing parachute at 3 HP:")
    draw_parachute(3)
    print()

    print("Drawing parachute at 2 HP:")
    draw_parachute(2)
    print()

    print("Drawing parachute at 1 HP:")
    draw_parachute(1)
    print()

    print("Drawing parachute at 0 HP:")
    draw_parachute(0)
    print()

if __name__ == "__main__":
    main()