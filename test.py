import datetime,calendar

today = calendar.day_name[datetime.date.today().weekday()]

with open("Shedule.txt", "r", encoding="UTF-8") as file:
    for elem in file:
        if elem.split(":")[0] == today:
            scedule = elem.split(":")[1]
res = "\n".join([elem  for elem in scedule.split("\t")])
print(res)