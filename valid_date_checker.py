import re

def valid_date(date: str):

    if len(date) != 10:
        return []

    parts = re.findall(r'\d+', date)

    # to see if there are 3 parts
    if len(parts) != 3:
        return []
    
    # to segregate year and (month & date)
    fourdigit = [part for part in parts if len(part) == 4 and int(part) >= 1900 and int(part) <= 2025]
    twodigit  = [part for part in parts if len(part) == 2 and int(part) >= 1 and int(part) <= 31]

    if len(fourdigit) != 1:
        return []

    # to see if there are two parts more than 12
    chance = 1 # as there can be one part that can be more than 12 (dates)
    
    for part in twodigit:
        if int(part) > 12:
            chance -= 1

    if chance < 0:
        return []
    
    twodigit.sort()
    twodigit.append(fourdigit[0][-2:])

    # If the code reaches here, no condition  passes, hence its a valid date
    return twodigit