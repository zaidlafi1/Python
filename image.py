import requests
from bs4 import BeautifulSoup
import os
"""
"""
url = 'https://www.aljfinance.com/index_ar.aspx'


def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),
                              folder))  # crete new folder with joining the current directory with folder directory
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('zaidtest', name)


imagedown('https://www.elevatus.io/about-us', 'elevatus')

"""
def video_down(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),
                              folder))  # crete new folder with joining the current directory with folder directory
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('video')
    for image in images:
        name = image['source']
        link = image['source']
        with open(name.replace('/', '-') + '.mp4', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('zaidtest', name)


video_down('https://www.elevatus.io/', 'elevatus-vedio')

"""