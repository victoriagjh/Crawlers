import requests
from bs4 import BeautifulSoup
def crawlSubjects():
        url = 'http://ce.khu.ac.kr/index.php?hCode=UNIVERSITY_02_01_01'
        source_code = requests.get(url)
        source_code.raise_for_status()
        source_code.encoding = None

        html = source_code.text
        soup = BeautifulSoup(html,"lxml")
        #lxml은 Parser, html.parser보다 처리 속도가 월등히 빠름

        tableDiv = soup.find(id="conTD")
        tables = tableDiv.find_all("table")
        ceLecture = tables[0]
        trs = ceLecture.find_all('tr')
        cnt = 0
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds)==14:
                cnt+=1
                print(tds[0].get_text())

crawlSubjects()



