def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return 2 <= len(s) <= 6 and s[:2].isalpha()



if __name__ == "__main__":
    main()
