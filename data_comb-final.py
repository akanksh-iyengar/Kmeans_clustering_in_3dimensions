import json
import csv
final_data={}
csv_file=open("months-data.csv",'a')
writer = csv.writer(csv_file, delimiter=',')
ulta={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
diff_months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
with open('tourism_data_3.json','r') as duke:
    data=json.load(duke)
    for state in data:
        for place in data[state]:
            #print(place)
            req=[]
            arr=[0,0,0,0,0,0,0,0,0,0,0,0,0]
            for website in data[state][place]:
                #print(website)
                if website=='district':
                    district=data[state][place][website]
                    continue
                var=data[state][place][website].split()
                #print(var)
                req.append((var[0],var[2]))
                for entry in req:
                    m1=entry[0]
                    m2=entry[1]
                    if m1 in months.keys():
                        n1=months[m1]
                    else:
                        n1=diff_months[m1]
                    if m2 in months.keys():
                        n2=months[m2]
                    else:
                        n2=diff_months[m2]
                    if n1>n2:
                        for i in range(n1,13):
                            arr[i]=arr[i]+1
                        for i in range(1,n2+1):
                            arr[i]=arr[i]+1
                    else:
                        for i in range(n1,n2+1):
                            arr[i]=arr[i]+1
            #print(req)
            print(arr)
            maximum=max(arr)
            opt=[]
            for i in range(0,len(arr)):
                if arr[i]==maximum and arr[i]!=0:
                    arr[i]=1
                else:
                    arr[i]=0
            start=0
            end=0
            arr.append(0)
            for k in range(1,14):
                if arr[k]==1:
                    if start==0:
                        start=k
                        end=k
                        #print(start)
                        #print(end)
                    else:
                        end=k
                        #print(start)
                        #print(end)
                else:
                    if start!=0 and end!=0:
                        opt.append((start,end))
                        #print(start)
                        #print(end)
                        start=0
                        end=0
                        #print(start)
                        #print(end)
            del arr[0]
            del arr[-1]
            print(arr)
            row=[place]
            row.extend(arr)
            print(opt)
            if len(opt)==2:
                row.append(ulta[opt[1][0]])
                row.append(ulta[opt[0][1]])
            elif len(opt)==1:
                row.append(ulta[opt[0][0]])
                row.append(ulta[opt[0][1]])
            else:
                row.append('Null')
                row.append('Null')
            print(row)
            writer.writerow(row)
