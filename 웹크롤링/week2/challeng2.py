data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum = 0
for datum in data:
    print(datum)

for datum in data:
    datum = datum.replace('조회수: ', '').replace(',', '')
    print(datum)

for datum in data:
    sum += int(datum.replace('조회수: ','').replace(',',''))


print(sum)