def Utopia(cycle, ini_h):
    count = 1
    while count <= cycle:
        if count % 2 != 0:
            ini_h *= 2
        else:
            ini_h += 1
        count += 1
    return ini_h

test_case = input()
height = 1
while test_case:
    cycle = input()
    print(Utopia(cycle, height))
    test_case -= 1
