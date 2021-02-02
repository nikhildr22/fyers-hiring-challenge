
if __name__=="__main__":
    with open('airlines.csv') as f_hand:
        lis = f_hand.readlines()
    air_count = dict()
    for i in lis[1:]:
        temp = i.split(',')
        air_count[temp[1]+temp[2]] = air_count.get(temp[1]+temp[2],0) + 1
    outputs = {'output1':air_count}
    maxi = []
    for key, value in air_count.items():
        maxi.append((value,key))
    maxi.sort(reverse=True)
    outputs["output2"] = maxi[0]
    outputs["output3"] = maxi[-1]
    print(outputs['output1'])
    print(f"{outputs['output2'][1]} - {outputs['output2'][0]}")
    print(f"{outputs['output3'][1]} - {outputs['output3'][0]}")