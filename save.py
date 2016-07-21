
import os
import sys
import io
from os import path
import urllib
import urllib2

def creates(namea,detailss,picture):
    ozet = detailss
    yeni_yol = namea[:-1]
    anime = r'C:\\Users\\ahmetwww\\Desktop\\Animeler\\%s' % (yeni_yol)
    

    try: 
        if not os.path.exists(anime): #try to create folder if not exits
            os.makedirs(anime)
       
        name=os.path.join(anime,"ozet.txt") # define txt file's location.
        download_very_big_image(picture,os.path.join(anime,yeni_yol+".jpg"))#try to get image
        
        
         

        if not (os.path.isfile(name)):
            with open(name,"w") as f: # Try to write text to txt file
                f.write(ozet)
                f.close()


        try:
            db(yeni_yol,ozet) # Write data to database.
        except:
            print "database hatasi"


 

    except:
        print "Genel hata"


def download_very_big_image(urls,location):
    url = urls
    filename = location
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url,headers=hdr)
    conn = urllib2.urlopen(req)
    output = open(filename, 'wb') #binary flag needed for Windows
    output.write(conn.read())
    output.close()

def db(names,exts):  # Database data save function.
    import MySQLdb

    db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="deneme")        # name of the data base
   
    cur = db.cursor()
    cur.execute("insert into kl values(%s,%d)" % (names,exts))
    db.commit()
    
