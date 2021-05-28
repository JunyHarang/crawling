import urllib.request
import datetime, json, math


def getRequestUrl(url):
    request = urllib.request.Request(url)
    
    try:
        response = urllib.request.urlopen(request)
        
        if response.getcode() == 200:
            # print('[%s] success' % (datetime.datetime.now()))
            return response.read().decode('utf-8')
    
    except Exception as e:
        print('[%s] faliure' % (datetime.datetime.now()))
        print(e)
        return None
# def getRequestUrl(url) 끝

def getHospitalData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'

    access_key = 'SbocJjNjKADXSRaHDXBnRLvvmOlT9wCwQb7yPXXqCoTUdhSEVElEofF5POZcHAatHNlGut2%2BUJTw%2FEVKHofM7g%3D%3D'
    
    params = '?resultType=json'
    params += '&serviceKey=' + access_key
    params += '&pageNo=' + str(pageNo)
    params += '&numOfRows=' + str(numOfRows)
    
    url = end_point + params
    
    print('URL은 다음과 같습니다!')
    print(url)
    
    result = getRequestUrl(url)
    
    if(result == None):
        return None
    
    else :
        return json.loads(result)
# def getHospitalData(pageNo, numOfRows) 끝
    
jsonResult = []

pageNo = 1         # 페이지 번호
numOfRows = 100    # 1번에 조회할 최대 행 수
nPage = 0

while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRows)
    # print(jsonData)
    print('='*50)
    
    # 전달 받은 데이터에 접속을 성공 했다면?
    if(jsonData['MedicalInstitInfo']['header']['code'] == '00'):
        totalCount = jsonData['MedicalInstitInfo']['totalCount']
        print('데이터 총 개수는 ' + str(totalCount) + '입니다.')
        
        if totalCount == 0: # totalCount가 0이면 while문 종료
            break
        
        for item in jsonData['MedicalInstitInfo']['item']:
            jsonResult.append(item)
            
        nPage = math.ceil(totalCount/numOfRows) # 마지막 페이지를 계산
        
        if(pageNo == nPage):
            break # 마지막 페이지라면 while문 종료
            
        pageNo += 1
    
    else :
        break
    
    saveFileName = '부산광역시 의료기관, 약국 운영 시간 정보.json'
    
    # 별칭을 outfile로 준 saveFileName을 열어서 Write('w')을 utf-8로 한다.
    # with구문은 암묵적으로 Close() 까지 해 준다.
    with open(saveFileName, 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print(saveFileName + ' 의 파일 생성이 완료 되었습니다!')
    
print('작업이 완료 되었습니다!')