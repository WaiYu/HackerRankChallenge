tests = int(input())
while tests:
    cuts = int(input())
    print (int(cuts/2) * (int(cuts/2) + cuts%2))
    tests -= 1
