#made in python 3.7

from bs4 import BeautifulSoup
import requests

#add wanted items below
item = ["Green d'hide body","Rune_med_helm","Rune med helm","Iron Platebody","Mithril Pickaxe","Mithril Platebody"]


x = len(item)
        
natureinput = input("Use GE's Nature Rune price? (y/n): ")
        #Grabs wiki's nature rune's price if user's input is Y
if natureinput == "y" or natureinput == "Y":
    url= "http://oldschoolrunescape.wikia.com/wiki/Nature Rune"
    raw= requests.get(url).text
    raw= BeautifulSoup(raw, 'lxml')
    robado = raw.find('span',class_="GEItem").text
    robado = robado.replace(",","",1)
    nature= int(robado)
    print("Price of Nature Rune: " + str(nature) + "gp")
        #Or user can just enter a custom Nature's Rune price
else:
    nature = input("Price of Nature Rune: ")
    nature= int(nature)
    
print("Analyzing the market...")
print("")

#This starts browsing item per item (The x range is the number of items in the item row)
for i in range(0,x):
    
    url= "http://oldschoolrunescape.wikia.com/wiki/" + item[i]  #Item will be put in here to access the wiki page
    raw= requests.get(url).text
    raw= BeautifulSoup(raw, 'lxml')                             #Just getting all the html data from the site

    #Below is for GE item price
    robado = raw.find('span',class_="GEItem").text
    robado = robado.replace(",","",1)
    geprice= int(robado)
        
    #Below is for HighAlch item price
    robado = raw.find_all('td')
    c = 0
    for z in robado:
        if(c==7): #High alch price was in the 7th row
            alchprice = z.text
            alchprice =alchprice.replace(" ","")
            alchprice =alchprice.replace(",","")
            alchprice =alchprice.replace("coins","")
            alchprice=int(alchprice)
        c+=1
        
    #Aight now this calculates the profit and prints it

    profit = alchprice-geprice-nature
    print("Item: "+item[i]+"     | GE Price: " +str(geprice) +" | Alch Price: " + str(alchprice) + " | Profit: " + str(profit) )
        
    

