import requests
from bs4 import BeautifulSoup

f= open("navertv.csv","w")

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info >>이거보니까 제목,채널명,재생수,좋아요수 딱 4개 컨테이너만 가진거 100개모아놓은거네
clips = html.select("dl.cds_info")

for cl in clips:
    # 수정된 부분
    title = cl.select_one("dt.title").text.strip()
    chn = cl.select_one("dd.chn").text.strip()
    hit = cl.select_one("span.hit").text.strip()
    like = cl.select_one("span.like").text.strip()

    # replace함수를 활용하여 ,를 제거한다 ( 이거과정 거치면 csv파일의 열이 제거가 잘 된것을 확인할수있음)
    title = title.replace(",", "")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    #replace함수 활용해서 "재생 수" 제거
    hit= hit.replace("재생 수", "")

    #1. replace함수 활용해서 "좋아요 수" 제거
    #hit= hit.replace("좋아요 수", "")
    #2. 슬라이싱 활용해서 "좋아요 수"제거 5:여기서 5번째부터가아니라 6번째부터(인덱스 0부터시작!)
    like= like[5:]

    print("제목", title)
    print("채널명", chn)
    print(hit)
    print(like)
    print("="*50)



# 앞에서 f = open("navertv.csv", "w") 이거 열어줬으면 close로 꼭 닫아야함!!!
f.close()
