import urllib.request
import cv2
import numpy as np
import os

def sotre_raw_images(path):
    neg_image_urls = urllib.request.urlopen(path).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + '.jpg')
            img = cv2.imread("neg/" + str(pic_num) + '.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + '.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    for file_type in ['neg']:
        ''' for img in os.listdir(file_type):
           print (file_type + ',' + img) '''
    for a in os.listdir('main'):
        print (a)

