import cv2
import urllib.request
from PIL import Image
import numpy as np

def writeImageListFromFile(inputPath, outputPath):
    f = open(inputPath, "rt", encoding='utf8')
    list = []
    linkList = []
    cnt = 0;
    while True:
        line = f.readline()
        if not line : break
        if line.find('<img class="rg_ic rg_i" data-src=') != -1:
            list.append(line)

    for i in range (list.__len__()) :
        while list[i].find('<img class="rg_ic rg_i" data-src=') != -1:
            list[i] = list[i][list[i].find('<img class="rg_ic rg_i" data-src=')+34 : ]
            linkList.append(list[i][0:list[i].find('"')])
    f.close()

    print (linkList)
    f = open(outputPath, "w")
    for i in linkList:
        f.write(i + '\n')

def getImageFromLink(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image

image = getImageFromLink('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPR8FOXPDfOmP7WVinKv90V_SKGjJmqt_PmX_A7JiIj--M2lxw')
cv2.imshow("image", image)
cv2.waitKey(0)