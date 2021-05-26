import folium
import requests
import pandas as pd

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='

api_key = 'b78634f74383cec67bf8cd217efb7bef'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGocoder(address):
    result = ""
    url = url_header + address
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result
# end def getGocoder(address)

def makeMap(brand, store, geoInfo):
    shopinfo = store + '(' + brand_dict[brand] + ')'
    mycolor = brand_color[brand]
    latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

    # Marker 그리기
    folium.Marker([latitude, longitude], popup=shopinfo, icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)

# end def makeMap(brand, store, geoInfo)

brand_dict = {'cheogajip':'처가집', 'goobne':'굽네치킨', 'pelicana':'페리카나', 'nene':'네네치킨'}
brand_color = {'cheogajip':'red', 'goobne':'green', 'pelicana':'purple', 'nene':'blue'}

# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

csv_file = '../../02.crawling/allStoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
# print(myframe.info())

where = '서대문구'
brandName = 'cheogajip'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData01 = myframe.loc[condition1 & condition2]
# print('='*100)
# print(mapData01)

# print('='*100)

brandName = 'nene'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData02 = myframe.loc[condition1 & condition2]
# print(mapData02)

brandName = 'goobne'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData03 = myframe.loc[condition1 & condition2]

brandName = 'pelicana'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData04 = myframe.loc[condition1 & condition2]

mylist = []
mylist.append(mapData01)
mylist.append(mapData02)
mylist.append(mapData03)
mylist.append(mapData04)

mapData = pd.concat(mylist, axis=0)
# print(mapData)

ok, no = 0, 0
for idx in range(len(mapData.index)):
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    geoInfo = getGocoder(address)

    print(geoInfo)

    if geoInfo == None :
        print('nope! : ' + address)
        no += 1

    else:
        print('Okay! : ' + brand + ' ' + address)
        ok += 1
        makeMap(brand, store, geoInfo)
    print('='*100)

total = ok + no
print('ok : ', ok)
print('no : ', no)
print('total : ', total)

filename = '/workspace/crawling/00.Practice/mapvisual/mapresult.html'
mapObject.save(filename)
print('파일 저장 완료')