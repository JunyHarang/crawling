import json
from pandas import DataFrame

jsonfile = '부산광역시 의료기관, 약국 운영 시간 정보.json'

myfile = open(jsonfile, 'rt', encoding='utf-8')
myfile = myfile.read()

jsonData = json.loads(myfile)

print(type(jsonData))
print('='*50)

totallist = []
mycolumns = []    # 컬럼 이름을 담을 List
idx = 0

for oneitem in jsonData:
    # print(type(oneitem))
    sublist = []
    for key in oneitem.keys():
        
        if idx == 0:
            # 첫번째 행에 컬럼 제목이 있고, 이것을 가져와야 하기 때문에 한번만 불러서 columns에 넣는다.
            mycolumns.append(key)
            
        sublist.append(oneitem[key])
    
    idx += 1

    totallist.append(sublist)
    print('='*50)

print(totallist)

myframe = DataFrame(totallist, columns=mycolumns)

fileName = 'pusanHospitalExcel.csv'

# Excel에서 한글이 안 깨지게 하기 위해서는 encoding을 다음과 같이 설정
myframe.to_csv(fileName, encoding='utf-8', index=False)

print(fileName + '의 저장이 완료 되었습니다!')