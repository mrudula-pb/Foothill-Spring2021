
def main():
    for number in range(0, 30, 2):
        if number % 3 == 0:
            continue
        if number == 14:
            break
        print(number, end=' ')  # end has space
    else:
        print("\nI printed the whole range")
    print("\nI am done!")


if __name__ == '__main__':
    main()