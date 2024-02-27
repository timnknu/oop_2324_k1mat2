data = {}
with open('input01.txt') as f:
    for line in f:
        rec = line.strip().split()
        if len(rec)>0:
            assert len(rec)==2
            try:
                pwr = int(rec[0])
            except:
                print("Wrong power", rec[0])
                continue
            assert pwr >= 0
            try:
                coef = float(rec[1])
            except:
                print("Wrong coef", rec[1])
                continue
            assert pwr not in data
            data[pwr] = coef
print(data)