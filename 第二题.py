result = {}

with open("longtext.txt", "r") as f:
    data = f.readlines()
    result['name'] = data[0].strip()
    result['lei'] = data[1].strip()
    result['sub_fund'] = []
    print(data)
    t = {}
    for i in range(2,len(data)):
        if data[i][0].isdigit():
            if i != 2:
                result['sub_fund'].append(t)
                t = {}
            t['title'] = data[i][3:].strip()
            t['isin'] = []
        else:
            t['isin'].append(data[i].strip())

    print(result)