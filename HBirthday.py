from datetime import datetime, date, timedelta
from collections import defaultdict
from calendar import day_name


users = [
    {'name': "Vasiliy", "birthday": date(1990, 9, 24)},
    {'name': "Kostya", "birthday": date(1988, 9, 25)},
    {'name': "Max", "birthday": date(1986, 9, 24)},
    {'name': "Masha", "birthday": date(1992, 9, 30)},
    {'name': "Polina", "birthday": date(1992, 9, 26)},
    {'name': "Tima", "birthday": date(1994, 9, 28)},
    {'name': "Ira", "birthday": date(1999, 9, 29)},
    {'name': "Katya", "birthday": date(1998, 9, 27)},
    {'name': "Nastya", "birthday": date(1996, 9, 25)},
    {'name': "Inna", "birthday": date(1999, 9, 29)},
    {'name': "Misha", "birthday": date(1990, 9, 28)},
    {'name': "Vova", "birthday": date(1992, 9, 30)},
    {'name': "Sergey", "birthday": date(1992, 9, 26)},
    {'name': "Mika", "birthday": date(1992, 9, 27)}
    ]


def get_birthdays_per_week(users):

    users = sorted(users, key=lambda x: x ["birthday"].day)
    result = defaultdict(str)
    for individ in users:
        if (datetime.now()).weekday() == 0:
            if (((individ["birthday"]).replace(year=(datetime.now()).year)) - (datetime.now()).date()) == timedelta(-2):
                result["Monday"] += (individ["name"]) + ", "
            if (((individ["birthday"]).replace(year=(datetime.now()).year)) - (datetime.now()).date()) == timedelta(-1):
                result["Monday"] += (individ["name"]) + ", "
            if timedelta(0) <= (((individ["birthday"]).replace(year=(datetime.now()).year)) - (datetime.now()).date()) <= timedelta(7):
                result[day_name[((individ["birthday"]).replace(year=(datetime.now()).year).weekday())]] += (individ["name"]) + ", "
        elif timedelta(0) <= (((individ["birthday"]).replace(year=(datetime.now()).year)) - (datetime.now()).date()) <= timedelta(7):
            result[day_name[((individ["birthday"]).replace(year=(datetime.now()).year).weekday())]] += (individ["name"]) + ", "

    for key, value in result.items():
        print(f"{key}: {value[:-2]}")


get_birthdays_per_week(users)