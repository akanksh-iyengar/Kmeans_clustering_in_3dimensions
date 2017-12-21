import json
import csv
final_data={}
csv_file=open("months-data.csv",'r')
csv_file_2=open("Final_data.csv",'a')
writer = csv.writer(csv_file, delimiter=',')
writer1 = csv.writer(csv_file_2, delimiter=',')
ulta={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
diff_months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
data1 = list(csv.DictReader(csv_file))
temp=[]
for item in data1:
    temp.append(item['Place'])
print(temp)
with open('lat_lon_place.json','r') as duke:
    data=json.load(duke)
print(data)
places=list(data.keys())
print(places)
#print(data[places[0]])
#print(data1)
for item in data1:
    temp1 = [item['Place'], item['Jan'], item['Feb'], item['Mar'], item['Apr'], item['May'], item['Jun'], item['Jul'],
             item['Aug'], item['Sept'], item['Oct'], item['Nov'], item['Dec']]
    #print(temp1)
    start=0
    end=0
    arr=[0]
    arr.extend([int(i) for i in temp1[1:]])
    #print(arr)
    start = 0
    end = 0
    opt=[]
    arr.append(0)
    for k in range(1, 14):
        if arr[k] == 1:
            if start == 0:
                start = k
                end = k
            else:
                end = k
        else:
            if start != 0 and end != 0:
                opt.append((start, end))
                # print(start)
                # print(end)
                start = 0
                end = 0
    del arr[0]
    del arr[-1]
    row = [temp1[0]]
    row.extend(arr)
    #print(opt)
    if len(opt) == 2:
        row.append(ulta[opt[1][0]])
        row.append(ulta[opt[0][1]])
    elif len(opt) == 1:
        row.append(ulta[opt[0][0]])
        row.append(ulta[opt[0][1]])
    else:
        row.append('Null')
        row.append('Null')
    print(row)
    if temp1[0] in places:
        pair=data[temp1[0]]
        if(len(pair)==0):
            row.append('Null')
            row.append('Null')
        else:
            row.append(pair['lat'])
            row.append(pair['lon'])
    else:
        row.append('Null')
        row.append('Null')
    print(row)
    writer1.writerow(row)
