import requests
from bs4 import BeautifulSoup

f = open("daumnews.csv", "w")
f.write("제목,기사요약\n")

for n in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text

        print(title)
        print(summary)
        print("="*50)

        title = title.replace(",", "")
        summary = summary.replace(",", "")

f.close()
