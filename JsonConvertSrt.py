import json
import datetime


with open('data.json',  encoding="utf8") as json_file:
    data = json.load(json_file)

bodyFrom = data['body']

def changeSecond(second):
    fromRoot = str(datetime.timedelta(seconds=second)) #set
    fromRootAddZero = '0' + fromRoot[0:11]
    fromRootFinal = fromRootAddZero.replace(".",",")
    if ',' not in fromRootFinal:
        fromRootFinal = fromRootFinal + ',000'
    return fromRootFinal


listObject = []
index = 0
for item in bodyFrom:
    index = index +1
    fromRoot = changeSecond(item['from'])
    toRoot = changeSecond(item['to'])
    listObject.append({
        "locate":index,
        "from":fromRoot,
        "to":toRoot,
        "content":item['content']
    })

with open('final.srt','w',encoding="utf8") as file:
   print('Mở file SRT thành công') 
   for item in listObject:
        file.write(f"{item['locate']}\n")
        file.write(f"{item['from']} --> {item['to']}\n")
        file.write(f"{item['content']}\n")
        file.write("\n")
   print('Đóng file Srt !!!') 

    

