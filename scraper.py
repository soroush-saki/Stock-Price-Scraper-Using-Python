import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
  
headers = {'user-agent':'Mozilla/5.0 \ 
            (Windows NT 10.0; Win64; x64) \ 
            AppleWebKit/537.36 (KHTML, like Gecko) \ 
            Chrome/84.0.4147.105 Safari/537.36'} 
  
urls = [ 
    'https://www.investing.com/equities/nike', 
    'https://www.investing.com/equities/coca-cola-co', 
    'https://www.investing.com/equities/microsoft-corp', 
    'https://www.investing.com/equities/3m-co', 
    'https://www.investing.com/equities/american-express', 
    'https://www.investing.com/equities/amgen-inc', 
    'https://www.investing.com/equities/apple-computer-inc', 
    'https://www.investing.com/equities/boeing-co', 
    'https://www.investing.com/equities/cisco-sys-inc', 
    'https://www.investing.com/equities/goldman-sachs-group', 
    'https://www.investing.com/equities/ibm', 
    'https://www.investing.com/equities/intel-corp', 
    'https://www.investing.com/equities/jp-morgan-chase', 
    'https://www.investing.com/equities/mcdonalds', 
    'https://www.investing.com/equities/salesforce-com', 
    'https://www.investing.com/equities/verizon-communications', 
    'https://www.investing.com/equities/visa-inc', 
    'https://www.investing.com/equities/wal-mart-stores', 
    'https://www.investing.com/equities/disney', 
    ] 
  
  
all=[] 
for url in urls: 
    page = requests.get(url,headers=headers) 
    try: 
        soup = BeautifulSoup(page.text, 'html.parser') 
        company = soup.find('h1', {'class':  
          'text-2xl font-semibold \ 
          instrument-header_title__gCaMF \ 
          mobile:mb-2'}).text 
        price = soup.find('div', {'class':  
          'instrument-price_instrument-price__xfgbB flex \ 
          items-end flex-wrap font-bold'}) 
            .find_all('span')[0].text 
        change = soup.find('div', {'class':  
           'instrument-price_instrument-price__xfgbB\ 
               flex items-end flex-wrap font-bold'}) 
                .find_all('span')[2].text 
        volume=soup.find('div',{'class':  
                   'trading-hours_value__5_NnB'}).text 
        x=[company,price,change,volume] 
        all.append(x) 
          
    except AttributeError: 
      print("Change the Element id") 
  
column_names = ["Company", "Price", "Change","Volume"] 
df = pd.DataFrame(columns = column_names) 
for i in all: 
  index=0
  df.loc[index] = i 
  df.index = df.index + 1
df=df.reset_index(drop=True) 
df.to_excel('stocks.xlsx')
