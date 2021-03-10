import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable 

baseurl = " https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"
product_details=[]
product_title =[]
product_price=[]
product_manufct=[]
product_stock=[]
for page_no in range(1, 3):
    r = requests.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage={x}')
    soup = BeautifulSoup(r.text, 'html.parser')
    prod = soup.find_all(id="Div1",class_="product")

    for pr in prod:
        product_title.append(pr.find('a',class_="catalog-item-name").get_text())
        product_price.append(pr.find('span',class_="price").get_text())
        product_manufct.append(pr.find('a',class_="catalog-item-brand").get_text())
        product_stock.append(("true","false")[pr.find('span',class_="out-of-stock").get_text()=="Out of Stock"])
        per_details = {"title":None,"price":None,"maftr":None,"In-stock":None}
        per_details["title"] = pr.find('a',class_="catalog-item-name").get_text()
        per_details["price"] = pr.find('span',class_="price").get_text()
        per_details["maftr"] = pr.find('a',class_="catalog-item-brand").get_text()
        per_details["In-stock"]=("true","false")[pr.find('span',class_="out-of-stock").get_text()=="Out of Stock"]
        product_details.append(per_details)

# print(product_details)

for prd in product_details:
    json_obj=json.dumps(prd,indent=4)
    print(json_obj)

myTable = PrettyTable(["Title", "Price", "Maftr", "In-Stock"]) 
for item in product_details:
    myTable.add_row([item["title"], item["price"], item["maftr"], item["In-stock"]])
print(myTable)