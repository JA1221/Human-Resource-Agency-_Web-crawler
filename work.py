import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

Area_Codes=['01','02','03','05','06','07','08'
              ,'09','11','12','13'
              ,'14','15','16','18','20'
              ,'04','21','22'
              ,'23','24','25']

DataOfGet = {'page': 0,'fs':1,'si':1}
n = 0
Corporation = {}
Salary = {}
Experience = {}
Education = {}
Check=''

print('__________ 臺灣 1111人力銀行調查統計程式 __________')
print('北部:')
print('<1>台北市 <2>新北市 <3>基隆市 <4>桃園市 <5>新竹市 <6>新竹縣 <7>苗栗縣')
print('中部:')
print('<8>台中市 <9>南投縣 <10>彰化縣 <11>雲林縣')
print('南部:')
print('<12>嘉義市 <13>嘉義縣 <14>台南市 <15>高雄市 <16>屏東縣')
print('東部:')
print('<17>宜蘭縣 <18>花蓮縣 <19>台東縣')
print('離島:')
print('<20>澎湖縣 <21>金門縣 <22>連江縣\n')

while True:
    area = input('請選擇地區(或不輸入 搜尋全台):')
    if area=='':
        break
    elif area.isdigit():
        num = int(area)
        if num>0 and num<=len(Area_Codes):
            DataOfGet['wc']='10' + str(Area_Codes[num-1]) + '00'
            break
    print('請輸入正確選項!')

job = input('請輸入工作關鍵字(或不輸入 搜尋全部直職缺)：')
DataOfGet['ks'] = job

while True:
    DataOfGet['page'] = DataOfGet['page']+1
    r = requests.get("https://www.1111.com.tw/job-bank/job-index.asp", params=DataOfGet)

    bsObj = BeautifulSoup(r.text, "html.parser")
    cprt = bsObj.findAll('span',{'itemprop':'name'})#公司
    needs = bsObj.findAll('div','needs')#薪水,經驗,學歷
    
    if Check==bsObj.get_text():
        break
    
    n = n + len(cprt)
    for i in range(len(cprt)):
        TempX = cprt[i].get_text()
        TempY = needs[i].get_text().split('/')
        #公司
        if TempX in Corporation:
            Corporation[TempX] = Corporation[TempX] + 1
        else:
            Corporation[TempX] = 1
        #薪水
        if TempY[0] in Salary:
            Salary[TempY[0]] = Salary[TempY[0]] + 1
        else:
            Salary[TempY[0]] = 1
        #經驗
        if TempY[1] in Experience:
            Experience[TempY[1]] = Experience[TempY[1]] + 1
        else:
            Experience[TempY[1]] = 1
        #學歷
        if TempY[2] in Education:
            Education[TempY[2]] = Education[TempY[2]] + 1
        else:
            Education[TempY[2]] = 1
    Check = bsObj.get_text()
    
print('\n__________ 統計完畢 總共', n, '筆職缺 __________')
while True:
    num = input('統計資料查詢 <1>薪水 <2>工作經驗 <3>學歷 <4>公司(不輸入可結束):')
    
    if num=='':
        break
    elif num.isdigit():
        if int(num)>0 and int(num)<=4:
            num = int(num)
        else:
            print('請輸入正確的選項!!')
            continue
    else:
        print('請輸入正確的選項!!')
        continue

    if num==1:
        data = Salary
    elif num==2:
        data = Experience
    elif num==3:
        data = Education
    else:
        data = Corporation

    num = 0
    data = sorted(data.items(), key=lambda d: d[1],reverse=True)
    for i in data:
        num = num + 1
        print('<', num, '>', i[0], ':', i[1])
    print('***總共', len(data), '筆資料***\n')
    
print('\n*程式結束*')
