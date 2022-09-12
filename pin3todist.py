from collections import defaultdict
from collections import Counter

state_c = defaultdict(Counter)
district_c = defaultdict(Counter)
sub_district_c = defaultdict(Counter)
pins = set()

with open("pin-dist-state.csv", "r") as file:
    next(file)  #header

    for line in file:
        row = line.rstrip()
        if row:
            pin, sub_district, district, state = row.split(",")
            pins.add(pin)
            state_c[pin][state] += 1
            district_c[pin][district] += 1
            sub_district_c[pin][sub_district] += 1

            # pin3 = pin[:3]
            # groups[pin3][district] += 1
            # groups[pin][district] += 1

            # groups[pin3][sub_district] += 1
            # groups[pin][sub_district] += 1

            # groups[pin3][state] += 1
            # groups[pin][state] += 1

getter = lambda pair: pair[1]
print(f"pin,sub_district,district,state")
for pin in pins:
    state = max(state_c[pin].items(), key=getter)[0]
    district = max(district_c[pin].items(), key=getter)[0]
    sub_district = max(sub_district_c[pin].items(), key=getter)[0]
    print(f"{pin},{sub_district},{district},{state}")
