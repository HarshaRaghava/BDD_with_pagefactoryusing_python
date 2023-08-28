from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class browser:
    driver=None

    def open_Chromebrowser(self,url):
        service_obj = Service("C:\\Users\\HarshavardhanRaghava\\PycharmProjects\\BDD\\Drivers\\chromedriver.exe")
        browser.driver=webdriver.Chrome(service=service_obj)
        browser.driver.get(url)
        browser.driver.maximize_window()
        return browser.driver
    def open_firefoxbrowser(selfself,url):
        service_obj=Service("C:\\Users\\HarshavardhanRaghava\\PycharmProjects\\BDD\\Drivers\\geckodriver.exe")
        browser.driver=webdriver.Firefox(service=service_obj)
        browser.driver.get(url)
        browser.driver.maximize_window()
        return browser.driver
    def open_edgebrowser(self,url):
        service_obj=Service("C:\\Users\\HarshavardhanRaghava\\PycharmProjects\\BDD\\Drivers\\msedgedriver.exe")
        browser.driver=webdriver.Edge(service=service_obj)
        browser.driver.get(url)
        browser.driver.maximize_window()
        return browser.driver
    def initialize_wait(self,time):
        wait = WebDriverWait(self,time)
        return time
