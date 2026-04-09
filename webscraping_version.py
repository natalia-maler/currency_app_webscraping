import requests 
from bs4 import BeautifulSoup 
import re 
import os
from datetime import datetime
import sys

def repair_title(filename):
    return re.sub(r"[|%*?<>#]","",filename) 


sys.stdout.reconfigure(encoding='utf-8') 

response = requests.get("https://kantor.pl/kursy-walut")
response.encoding = 'UTF-8'

# czy dane połączenie zostało udane
if response.status_code == 200:

    html_content = response.text

    page = BeautifulSoup(html_content, 'html.parser')

    if page.title:
        title = page.title.string.strip()  
        title = repair_title(title)
    else:
        title ="no_title"

    filename = f"pages/{title}.html" 

    directory = "pages"
    if not os.path.exists(directory):
        os.makedirs(directory) 

    with open (filename, "w", encoding="UTF-8") as file:
        file.write(html_content)

    print(f"HTML SAVED IN: {filename}")

else:
    print("Connection problem")


with open ("pages/Aktualne kursy walut - kurs NBP - Kantor.pl.html","r", encoding="UTF-8") as file:
    content = file.read()

page = BeautifulSoup(content,"html.parser")

# funkcja która zwróci cene kupca i sprzedazy waluty
def get_price(currency): 
    buy = page.find("span", id=f"buy_{currency}").text.strip()  
    sell = page.find("span", id=f"sell_{currency}").text.strip()

    return buy, sell

currencies = ["USD", "JPY", "EUR","CHF"]

# pobranie kursów walut
results = []

for currency in currencies:
    buy, sell = get_price(currency)
    buy = buy.replace(",",".")  
    sell = sell.replace(",",".")
    avg = round((float(buy)+float(sell))/2,4)   
    print(f"{currency}:  buy for: {buy} PLN, sell: {sell} PLN,  avg: {avg} PLN")
    results.append(f"{currency}:  buy for: {buy} PLN, sell: {sell} PLN,  avg: {avg} PLN")

data_directory = "data"

if not os.path.exists(data_directory):
    os.makedirs(data_directory) 

# plik txt do zapisu kursów
data_file_path = os.path.join(data_directory, "kursy_walut.txt")
 
current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # zamiana formatu daty czyli na dzien, miesiac

with open(data_file_path, "a", encoding="UTF-8") as data_file:
    data_file.write(f"Date: {current_date}\n")
    for price in results:
        data_file.write(f"{price}\n")
    
    data_file.write("\n")