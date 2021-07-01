
def currency_options(base_curr: str):
    """Print out a table of options for converting base_curr to all other currencies"""
    # print(f'GBP       USD       EUR       CAD       CHF       NZD       AUD       JPY')

    input_value = input("What is your home currency: ")
    print(f"{input_value}")
    for value in range(10, 91, 10):
        print(value)



currency_options("KKK")