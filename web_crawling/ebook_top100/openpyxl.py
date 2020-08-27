import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목","저자"])

for p in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(p),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')
    # 컨테이너 선택자: 전체 > 자식
    container = html.select("div.lst_thum_wrap li")


    for cont in container:
        # 제목 선택자: strong / a strong
        title = cont.select_one("a strong").text
        writer = cont.select_one("span.writer").text

        print(title, writer)
        sheet.append([title, writer])

        # 열사이 쉼표제거
        title = title.replace(",", "")
        writer = writer.replace(",", "")

wb.save("ebook.xlsx")
