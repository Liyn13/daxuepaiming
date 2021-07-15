from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
browser = webdriver.Chrome()#指定浏览器
browser.maximize_window()#最大化窗口
browser.get(url)
page = 3
def la():
    global page
    n = 1
    for i in range(30):
        html = browser.find_element_by_xpath('//*[@id="content-box"]/div[2]/table/tbody/tr['+str(n)+']')
        bsObj = BeautifulSoup(html.get_attribute('outerHTML'),'html.parser')
        print(bsObj.get_text().replace(' ','').replace('\n',' '))
        n += 1
    n = 1

    #翻页
    for i in range(21):
        if page < 8:
            for i in range(4):
                browser.find_element_by_xpath('/html').send_keys(Keys.PAGE_DOWN)
            sleep(0.2)
            browser.find_element_by_xpath('//*[@id="content-box"]/ul/li['+str(page)+']/a').click()
            sleep(0.2)
            for i in range(4):
                browser.find_element_by_xpath('/html').send_keys(Keys.PAGE_UP)
            sleep(0.2)

            for i in range(30):
                html = browser.find_element_by_xpath('//*[@id="content-box"]/div[2]/table/tbody/tr['+str(n)+']')
                bsObj = BeautifulSoup(html.get_attribute('outerHTML'),'html.parser')
                print(bsObj.get_text().replace(' ','').replace('\n',' '))
                n += 1
            n = 1

            page += 1
        elif page == 20:
            for i in range(4):
                browser.find_element_by_xpath('/html').send_keys(Keys.PAGE_DOWN)
            sleep(0.2)
            browser.find_element_by_xpath('//*[@id="content-box"]/ul/li[8]/a').click()
            sleep(0.2)
            for i in range(4):
                browser.find_element_by_xpath('/html').send_keys(Keys.PAGE_UP)
            sleep(0.2)

            for i in range(30):
                html = browser.find_element_by_xpath('//*[@id="content-box"]/div[2]/table/tbody/tr['+str(n)+']')
                bsObj = BeautifulSoup(html.get_attribute('outerHTML'),'html.parser')
                print(bsObj.get_text().replace(' ','').replace('\n',' '))
                n += 1
            input('结束啦！！！')
        else:
            page -= 1
            for i in range(4):
                browser.find_element_by_xpath('/html').send_keys(Keys.PAGE_DOWN)
            sleep(0.2)
            browser.find_element_by_xpath('//*[@id="content-box"]/ul/li['+str(page)+']/a').click()
            sleep(0.2)
            for i in range(4):
                browser.find_element_by_xpath('/html').send_keys(Keys.PAGE_UP)
            sleep(0.2)

            for i in range(30):
                html = browser.find_element_by_xpath('//*[@id="content-box"]/div[2]/table/tbody/tr['+str(n)+']')
                bsObj = BeautifulSoup(html.get_attribute('outerHTML'),'html.parser')
                print(bsObj.get_text().replace(' ','').replace('\n',' '))
                n += 1
            n = 1

            page += 1

la()
input()
browser.close()

