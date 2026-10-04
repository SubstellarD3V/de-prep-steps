def find_first_dentist(people):
    isdent = {}
    z = people[0]
    print(z)
    y = z.values()
    for x in z.items():
        print(x)
    print(isdent)


find_first_dentist([{"name": "Callum", "is_dentist": True}])