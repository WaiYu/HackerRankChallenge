test_count = int(input())
while test_count:
    count = 0
    i = 0
    s = input()
    cycle = int(len(s)/2)
    while cycle:
        count += abs(ord(s[len(s) - 1 - i]) - ord(s[i]))
        cycle -= 1
        i += 1
    print (count)
    test_count -= 1