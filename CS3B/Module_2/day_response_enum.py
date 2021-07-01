from enum import Enum


class DayOfWeek(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = 'Saturday'
    SUNDAY = "Sunday"


def day_response(day: DayOfWeek):
    """ Give an appropriate response depending on the day of the week.
    """
    if day == DayOfWeek.MONDAY:
        return "Ack, Monday"
    elif day == DayOfWeek.TUESDAY:
        return "Ack, Tuesday"
    elif day == DayOfWeek.WEDNESDAY:
        return "Ack, Wednesday"
    elif day == DayOfWeek.THURSDAY:
        return "Ack, Thursday"
    elif day == DayOfWeek.FRIDAY:
        return "Ack, Friday"
    elif day == DayOfWeek.SATURDAY:
        return "Ack, Saturday"
    elif day == DayOfWeek.SUNDAY:
        return "Ack, Sunday"


print(day_response(DayOfWeek.TUESDAY))
print(DayOfWeek.MONDAY.name)
print(DayOfWeek.MONDAY.value)
for day in DayOfWeek:
    print(f"Message for {day.value} is {day_response(day)}")
