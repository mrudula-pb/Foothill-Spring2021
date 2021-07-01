from enum import Enum

def day_response(day: int):
    """ Give an appropriate response depending on the day of the week.
    """
    if day == 0:
        return "Ack, Monday"
    elif day == 1:
        return "Ack, Tuesday"
    elif day == 2:
        return "Ack, Wednesday"
    elif day == 3:
        return "Ack, Thursday"
    elif day == 4:
        return "Ack, Friday"
    elif day == 5:
        return "Ack, Saturday"
    elif day == 6:
        return "Ack, Sunday"

print(day_response(0))


