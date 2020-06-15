import requests
from bs4 import BeautifulSoup as BS
import csv

total_page = 334
URL = []
j = 0
URL.append("https://clutch.co/agencies/digital-marketing")
for i in range(1, total_page):
    URL.append("https://clutch.co/agencies/digital-marketing?page=" + str(i))

for link in URL:
    r = requests.get(link)
    soup = BS(r.content, 'html5lib')
    #print(soup.prettify())
    Table = []
    csvfile = open('Digital_Marketing2.csv','a', newline='', encoding="utf-8")
    elem_boxes = soup.find_all("li", class_ ="provider-row")
    
    for elem_box in elem_boxes:
        row = {}
        j= j +1
        row["index"] = j

        try:
            elem_box.find("h3", class_ ="company-name")
            row["company"] = elem_box.find("h3", class_ ="company-name").text
            #print(elem_box.find("h3", class_ ="company-name").text)
        except:
            row["company"] = None
    
        try:
            elem_box.find("p", class_ ="tagline")
            row["tagline"] = elem_box.find("p", class_ ="tagline").text
            #print(elem_box.find("p", class_ ="tagline").text)
        except:
            row["tagline"] = None
    
        try:
            elem_box.find("span", class_ ="rating")
            row["rating"] = elem_box.find("span", class_ ="rating").text
            #print(elem_box.find("span", class_ ="rating").text)
        except:
            row["rating"] = None
            #print(None)
    
        try:
            elem_box.find("blockquote", class_ = "blockquote-in-module")
            row["quote"] = elem_box.find("blockquote", class_ = "blockquote-in-module").text
            #print( elem_box.find("blockquote", class_ = "blockquote-in-module").text)
        except:
            row["quote"] = None
            #print(None)

        try:
            elem_box.find("ul", class_ ="module-list small-list")
            row["founder"] = elem_box.find("ul", class_ ="module-list small-list").text
            #print( elem_box.find("ul", class_ ="module-list small-list").text)
        except:
            row["founder"] = None
            #print(None)

        try:
            elem_box.find("i", class_ ="icon-paid")
            row["size"] = elem_box.find_all("div", class_ ="list-item")[0].text
            #print( elem_box.find_all("div", class_ ="list-item")[0].text)
        except:
            row["size"] = None
            #print(None)

        try:
            elem_box.find("i", class_ ="icon-clock")
            row["rate"] = elem_box.find_all("div", class_ ="list-item")[1].text
            #print( elem_box.find_all("div", class_ ="list-item")[1].text)
        except:
            row["rate"] = None
            #print(None)

        try:
            elem_box.find("i", class_ ="icon-person")
            row["employee"] = elem_box.find_all("div", class_ ="list-item")[2].text
            #print( elem_box.find_all("div", class_ ="list-item")[2].text)
        except:
            row["employee"] = None
            #print(None)

        try:
            elem_box.find("span", class_ ="location-city")
            row["locality"] = elem_box.find("span", class_ ="location-city").text
            #print( elem_box.find("span", class_ ="location-city").text)
        except:
            row["locality"] = None
            #print(None)

        Foc = []
        try:
            elem_box.find("div", class_ ="carousel-inner")
            elem_Foc = elem_box.find("div", class_ ="carousel-inner")
            F = elem_Foc.find_all("div")
            for elem_F in F:   
                Foc.append(elem_F.text)
            row["focus"] = ",".join(Foc)
        except:
            row["focus"] = None

        Table.append(row)
        
    obj=csv.DictWriter(csvfile,['index','company', 'tagline', 'rating', 'quote', 'founder', 'size', 'rate', 'employee', 'locality', 'focus'])
    for tb in Table:
        obj.writerow(tb)

csvfile.close()
