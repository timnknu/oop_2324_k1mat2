data = {}
with open('input01.txt') as f:
    for line in f:
        rec = line.strip().split()
        if len(rec)>0:
            assert len(rec)==2
            pwr = int(rec[0])
            assert pwr >= 0
            coef = float(rec[1])
            print(pwr, coef)