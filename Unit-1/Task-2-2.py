

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if (not(x or y or z)) == ((not x) and (not y) and (not z)):
                print(f"for x: {x}, y: {y}, z: {z}>> {True}")
            else:
                print(f"for x: {x}, y: {y}, z: {z}>> {False}")