''' Generate The Days Schedule for Casa Sol
'''

from math import trunc

DAY_1= 45292.0
DAY_FINAL = 45658.0
HALF_HOUR = 1/48

days_list = []

days_dict = {
    0: "Sáb",
    1: "Dom",
    2: "Seg",
    3: "Ter",
    4: "Qua",
    5: "Qui",
    6: "Sex",
}

hours_dict = {
    16: "08:00 -> 08:30",
    17: "08:30 -> 09:00",
    18: "09:00 -> 09:30",
    19: "09:30 -> 10:00",
    20: "10:00 -> 10:30",
    21: "10:30 -> 11:00",
    22: "11:00 -> 11:30",
    23: "11:30 -> 12:00",
    24: "12:00 -> 12:30",
    25: "12:30 -> 13:00",
    26: "13:00 -> 13:30",
    27: "13:30 -> 14:00",
    28: "14:00 -> 14:30",
    29: "14:30 -> 15:00",
    30: "15:00 -> 15:30",
    31: "15:30 -> 16:00",
    32: "16:00 -> 16:30",
    33: "16:30 -> 17:00",
    34: "17:00 -> 17:30",
    35: "17:30 -> 18:00",
    36: "18:00 -> 18:30",
    37: "18:30 -> 19:00",
    38: "19:00 -> 19:30",
    39: "19:30 -> 20:00",
    40: "20:00 -> 20:30",
    41: "20:30 -> 21:00",
    42: "21:00 -> 21:30",
    43: "21:30 -> 22:00",
}


'''with open("CasaSol_WorkingDays.txt", "a") as file:
    day = 0
    while day < DAY_FINAL:
        day += HALF_HOUR
        if day%1 <= 1/3 or day%1 >= 11/12:
            continue
        else:
            file.write(f"{int(day)}\n")'''

'''with open("CasaSol_WeekDays.txt", "a") as file:
    day = DAY_1
    while day < DAY_FINAL:
        day += HALF_HOUR
        if day%1 < 1/3 or day%1 >= 11/12:
            continue
        else:
            file.write(f"{days_dict[int(day) % 7]}\n")'''

'''with open("CasaSol_WorkingHours.txt", "a") as file:
    day = DAY_1
    fraction_hour = 0
    while day < DAY_FINAL:
        day += HALF_HOUR
        fraction_hour += 1

        if fraction_hour == 48:
            fraction_hour = 0

        if day%1 < 1/3 or day%1 > 11/12:
            continue

        else:
            file.write(f"{hours_dict[fraction_hour]}\n")'''

