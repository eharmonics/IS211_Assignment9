from bs4 import BeautifulSoup
import requests
count = 0

URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="Pb(10px) Ovx(a) W(100%)")
results = results.find("table", class_="W(100%) M(0)")
all_results = results.find_all("tr", class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")
output = ""
for result in all_results:
    try:
        date = result.contents[0].getText()
        open = result.contents[1].getText()
        high = result.contents[2].getText()
        low = result.contents[3].getText()
        close = result.contents[4].getText()
        adj_close = result.contents[5].getText()
        volume = result.contents[6].getText()
        output = output + date.strip() + "\t\t" + open.strip() + "\t\t" + high.strip() + "\t\t" + low.strip() + "\t\t" + close.strip() + "\t\t" + adj_close.strip() + "\t\t" + volume.strip() + "\n"
    except:
        continue


print("====================================================================================================================")
print("Date\t\t\tOpen\t\tHigh\t\tLow\t\tClose\t\tAdj Close\tVolume")
print("====================================================================================================================")
print(output)

