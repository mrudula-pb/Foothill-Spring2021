def main():
    # when given a number, we do not get ValueError
    # print("NO TRY EXCPT OR CHECKING FOR NUMERIC")
    # print("-------------------------------------")
    # quiz_answer = input("How many legs does a spider have: ") # when given string 'four', we get ValueError
    # int_answer = int(quiz_answer)
    # if int_answer ==8:
    #     print("You are genius")
    # else:
    #     print('Time to study more..')
    #
    # # Checking if input is int or not
    # print('CHECKING FOR NUMERIC')
    # print("---------------------")
    # quiz_answer = input("How many legs does a spider have: ")
    # if quiz_answer.isnumeric():
    #     int_answer = int(quiz_answer)
    #     if int_answer == 8:
    #         print("You are genius")
    #     else:
    #         print('Time to study more..')
    # else:
    #     print("Next time please enter number....")

    # Catching Exception using try except block
    print("USING EXCEPTIONS")
    print("----------------")
    quiz_answer = input("How many legs does a spider have: ")
    try:
        int_answer = int(quiz_answer) # if we fail with ValueError
    except ValueError:
        print("Next time please enter number....")
    else:
        if int_answer == 8:
            print("You are genius")
        else:
            print('Time to study more..')
    finally:
        print("Come back soon...")

    print("HANDLE ZeroDivisionError")
    print("-----------------")
    quiz_answer = input("How many legs does a spider have: ")
    try:
        int_answer = int(quiz_answer)  # if we fail with ValueError
        your_share = 250 / int_answer
    except ValueError:
        print("Next time please enter number....")
    except ZeroDivisionError:
        print("please do not enter zero")
    except:
        print("something bad happened")
    else:
        print("YOU WILL GET", your_share)
    finally:
        print("Come back soon...")


if __name__ == "__main__":
    main()
