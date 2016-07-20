import os
import sys
import io
from os import path
import urllib


def creates(namea,detailss,picture):
    
    yeni_yol = namea[:-1]
    anime = r'C:\\Users\\ahmetwww\\Desktop\\Animeler\\%s' % (yeni_yol)
    extension= "txt"

    try: 
        if not os.path.exists(anime):
            os.makedirs(anime)
       
        name=anime+'\\'+yeni_yol+"."+extension
        
        urllib.urlretrieve(picture, anime+"\\"+yeni_yol+".jpg")
        
        try:
            if not (os.path.isfile(name)):
                with open(name,"w") as f:
                    f.write(detailss)
        except:
            print "hata yazi yazilamadi"
    except:
        print "hata image indirelemedi"

