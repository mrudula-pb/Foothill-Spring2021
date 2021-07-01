def convert_to_celsius(temp_f: float):
    """Covert temp_f to Celsius"""
    return 5 / 9 * temp_f - 32  # order of operators is not followed, hence logic error occurred, (temp-f - 32)


# We are dealing with logic error
def main():
    boiling = False
    while not boiling:
        response = float(input("What's the temp of water in F? "))
        temp_c = convert_to_celsius(response)
        if temp_c > 100:
            boiling = True
    print("It's soup")


if __name__ == '__main__':
    main()
