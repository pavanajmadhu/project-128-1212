from bs4 import BeautifulSoup
import requests
import pandas as pd
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(START_URL)


soup=BeautifulSoup(page.text,"html.parser")
startable=soup.find_all("table")
temp_list=[]
trows=startable.find_all("tr")
for tr in trows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
luminosity=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i[1]])
    distance.append(temp_list[i[3]])
    mass.append(temp_list[i[5]])
    radius.append(temp_list[i[6]])
    luminosity.append(temp_list[i[7]])

df=pd.DataFrame(list(zip(star_names,distance,mass,radius,luminosity)),columns=["star_names","distance","mass","radius","luminosity"])
print(df)
df.to_csv("bright_starts.csv")




