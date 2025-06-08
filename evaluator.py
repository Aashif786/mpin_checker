from common_pins import is_common_pin
from generate_pins import generate_pins_all
from generate_pins import generate_pins_specific

def find_reasons(mpin: str, dob_self: str, dob_spouse: str, anniversary: str) -> list[str]:
    
    reasons_found = []
    demographic_reasons = ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY", "DEMOGRAPHIC_DATES_MIXED"]


    demo_self = generate_pins_specific(dob_self)
    demo_spouse = generate_pins_specific(dob_spouse)
    demo_anniversary = generate_pins_specific(anniversary)


    # to check if the pin is in any of the demographic dates
    for idx, demo_lists in enumerate([demo_self, demo_spouse, demo_anniversary]):
        if not demo_lists:
            return ["INVALID_DATE"] 
        if mpin in demo_lists:
            reasons_found.append(demographic_reasons[idx])
    
    # to check if the pin is in any of the common pins
    if is_common_pin(mpin):
        reasons_found.append("COMMONLY_USED")

    # to check if the pin is in any of the generated pins
    mixed_demographic_pins = generate_pins_all(dob_self, dob_spouse, anniversary)
    if not mixed_demographic_pins:
        return ["INVALID_DATE"]
    if mpin in mixed_demographic_pins:
        reasons_found.append(demographic_reasons[3])
    

    return reasons_found