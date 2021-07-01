from enum import Enum


class DayWeek(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = 'Saturday'
    SUNDAY = "Sunday"


def day_response(day: DayWeek):
    """ Give an appropriate response depending on the day of the week."""
    if day == DayWeek.MONDAY:
        return "Ack, Monday"
    elif day == DayWeek.TUESDAY:
        return "Ack, Tuesday"
    elif day == DayWeek.WEDNESDAY:
        return "Ack, Wednesday"
    elif day == DayWeek.THURSDAY:
        return "Ack, Thursday"
    elif day == DayWeek.FRIDAY:
        return "Ack, Friday"
    elif day == DayWeek.SATURDAY:
        return "Ack, Saturday"
    elif day == DayWeek.SUNDAY:
        return "Ack, Sunday"


# access names of Enum
# print(DayWeek.MONDAY.name)

# iterate over the days of the week
for day in DayWeek:
    print(f"Message for {day.value} is {day_response(day)}")

print(DayWeek.MONDAY.value)

print(day_response(DayWeek.MONDAY))
