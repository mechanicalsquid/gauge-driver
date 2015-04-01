from bs4 import BeautifulSoup
import requests
import time
import serial

wind_max_pos=362
wind_min_pos=0
wind_range=25

gust_max_pos=362
gust_min_pos=0
gust_range=31

ser = serial.Serial('/dev/ttyAMA0', 4800)

windlookup=[0,7,14,27,41,57,75,93,112,128,146,160,176,192,206,220,235,250,265,279,292,304,317,330,343,357]
gustlookup=[0,8,35,65,89,115,142,170,195,225,250,280,305,335,364,390,418,445,475,500,530,560,585,615,645,670,700,725,755,780,810,840]

r=requests.get("http://www.bramblemet.co.uk/wap/")
data=r.text
soup=BeautifulSoup(data)
link=soup.find('a')
p=requests.get(r.url[:-18]+link.get('href'))
windpage=p.text
soup=BeautifulSoup(windpage)
windspeed=int(soup.prettify()[309:314])
gustspeed=int(soup.prettify()[315:318])
print("The current windspeed in the Solent is: "+ str(windspeed)+" Knots")
print("The current gustspeed in the Solent is: "+ str(gustspeed)+" Knots")

if windspeed>wind_range:
	windspeed=wind_range

if gustspeed>gust_range:
        gustspeed=gust_range

windpos=windlookup[windspeed]
gustpos=gustlookup[gustspeed]

if windpos<wind_min_pos:
	windpos=wind_min_pos

if gustpos<gust_min_pos:
        gustpos=gust_min_pos

ser.write("a")
ser.write(str(gustpos))
ser.write("\n")

          
ser.write("b")
ser.write(str(windpos))
ser.write("\n")
ser.close()
