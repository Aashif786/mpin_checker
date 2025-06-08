from itertools import permutations
from valid_date_checker import valid_date

def generate_pins_specific(date : str):
    parts = valid_date(date)
    if not parts: 
        return []
    day, month, year = parts[0], parts[1], parts[2]
    pins = []
    
    # add 4 digit pins combinations
    pins.append(year)
    year = year[-2:]
    pins.append(day+month)
    pins.append(day+year)
    pins.append(month+year)
    pins.append(month+day)
    pins.append(year+month)
    pins.append(year+day)

    # add 6 digit pins combinations
    pins.append(day+month+year)
    pins.append(day+year+month)
    pins.append(month+year+day)
    pins.append(month+day+year)
    pins.append(year+month+day)
    pins.append(year+day+month)

    return list(set(pins))  # to avoid duplicates

def generate_pins_all(dob_self: str, dob_spouse: str, anniversary: str):
    
    total_parts = []
    for date in [dob_self, dob_spouse, anniversary]:
        parts = valid_date(date)
        if not parts: 
            return []
        total_parts.extend(parts)

    four_digit_mpins = [''.join(p) for p in permutations(total_parts, 2)]
    six_digit_mpins  = [''.join(p) for p in permutations(total_parts, 3)]

    return list(set(four_digit_mpins + six_digit_mpins))
    
