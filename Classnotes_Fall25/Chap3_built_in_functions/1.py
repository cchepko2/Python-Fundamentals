import art

def main():
    number = 13
    bin_number = 0b1101

    print(f"{bin(number)=}")
    print(f"{bin_number=}")

    print(f"{hex(number)=}")

    print(chr(0x00B0))
    print(ord('°'))

    print(globals())
    print()
    print(locals())

    print(art.card, end = '')
    print("Same line!")


if __name__ == '__main__':
    main()