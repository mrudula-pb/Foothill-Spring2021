
def main():
    height = int(input("Welcome to Disneyland, how tall are you?? "))
    if height < 32:
        print('Sick with kiddy rides')
    if height >= 54:
        print('Alone')
    # Compund comparison
    if 32 <= height < 54:
        print("lets go together")

if __name__ == "__main__":
    main()