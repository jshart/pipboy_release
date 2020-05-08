import requests
import json
import math
import os

locationHost='http://ipinfo.io'
tileHost='https://a.tile.openstreetmap.org'

# from https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
  return (xtile, ytile)

# parse the response
response=requests.get(locationHost)
print(response)
print(response.json())
json_response = response.json()
print(response.json())

#write location details out to text file
screensPath = "UIScreens"
locationFile = os.path.join(screensPath,"map.txt")

locFile = open(locationFile,"w") 
  
# \n is placed to indicate EOL (End of Line) 
locFile.write(json_response['country']+"\n")
locFile.write(json_response['region']+"\n") 
locFile.write(json_response['city']+"\n") 


# fetch the co-ordinate locations
print(json_response['loc'])
x,y=json_response['loc'].split(',')
locFile.write(x+"\n")
locFile.write(y+"\n")

xtile, ytile = deg2num(float(x),float(y),10)
locFile.write("{:d}\n".format(xtile))
locFile.write("{:d}\n".format(ytile))
locFile.close() #to change file access modes


#fetch a tile using (256x256)
#https://a.tile.openstreetmap.org/10/506/340.png
#black and white version
#http://a.tile.stamen.com/toner/10/506/340.png

# download the image
command="wget -O UIScreens/rawMap.png "+tileHost+"/10/{:d}/{:d}.png".format(xtile,ytile)
print(command)
os.system(command)

