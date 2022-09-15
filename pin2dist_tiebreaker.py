from collections import defaultdict
from collections import Counter

state_c = defaultdict(Counter)
district_c = defaultdict(Counter)
pins = set()

with open("pin_dist_state_uniq_20k.csv", "r") as file:
    next(file)  #header

    for line in file:
        row = line.strip()
        if row:
            pin, district, state = row.split(",")
            pins.add(pin)
            state_c[pin][state] += 1
            district_c[pin][district] += 1

getter = lambda pair: pair[1]
print(f"pin,district,state")
for pin in pins:
    state = max(state_c[pin].items(), key=getter)[0]
    district = max(district_c[pin].items(), key=getter)[0]
    print(f"{pin},{district},{state}")
