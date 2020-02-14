import cv2
import numpy as np
from selenium import webdriver
import urllib.request
import time
import os
from selenium.webdriver.chrome.options import Options


def get_insta_urls(centerinstaurl):
    posts = ['/html/body/div[1]/section/main/div/div[@class=" _2z6nI"]/article/div/div/div/div[1]/a','/html/body/div[1]/section/main/div/div[@class=" _2z6nI"]/article/div/div/div/div[2]/a','/html/body/div[1]/section/main/div/div[@class=" _2z6nI"]/article/div/div/div/div[3]/a']
    instaUrls = list()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=r'/Users/yeoah/PycharmProjects/InstaScraper/chromedriver',chrome_options=options)
    driver.get(centerinstaurl)
    driver.set_page_load_timeout(5)
    for post in posts:
        try:
            instaUrls.append(driver.find_element_by_xpath(post).get_attribute('href'))
        except Exception:
            pass

    driver.close()
    return instaUrls


def download_insta_image(url,imgName):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=r'/Users/yeoah/PycharmProjects/InstaScraper/chromedriver',chrome_options=options)
    driver.get(url)
    time.sleep(1)

    try:
        srcset = driver.find_element_by_class_name('FFVAD').get_attribute('srcset')
        imgUrlList = srcset.split()
        driver.close()
        urllib.request.urlretrieve(imgUrlList[0], imgName)
        print("Image download success")
    except Exception as e:
        print(e)


def mse(imageA, imageB):
    imageA = cv2.imread(imageA)
    imageB = cv2.imread(imageB)
    imageB = cv2.resize(imageB,(imageA.shape[1],imageB.shape[0]))
    try:
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageB.shape[1])
        print(err)
        if err > 2000.00:
            return False
        else:
            return True
    except ValueError:
        return False


def check_insta_pics(instaUrl,ogImagePath):
    instaUrls = get_insta_urls(instaUrl)

    for url in instaUrls:
        download_insta_image(url,'pic.jpg')
        if mse(ogImagePath,'pic.jpg'):
            os.remove('pic.jpg')
            return True

    return False

