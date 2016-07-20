from bs4 import BeautifulSoup
import requests
import save
c = 1
while c<= 9006:
	r = requests.get("http://anizm.tv/anime-detay.asp?ID="+str(c)+"") 
	soup = BeautifulSoup(r.content,"html.parser")
	g_data = soup.find_all("div",{"id":"layout"})
	for a in g_data:
		try:
			ad = a.find("h3").text
			ozet = a.find("article", {"class":"b_block post r_post"}).text
			tur = a.find("div",{"class":"anime-bilgileri"}).find("p").text
			link = a.find("div",{"class":"counter clearfix"}).find("img")
			link2 = "https://anizm.tv/"+link["src"]
			save.creates(ad,ozet,link2)
			print ad + "a\n" + ozet + "\n" + tur
			
			if ad == "Anime Takvimi": continue
			break
		except:
			c+=1
	c+=1

