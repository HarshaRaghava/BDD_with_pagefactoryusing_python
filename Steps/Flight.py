import allure
from allure_commons.types import AttachmentType
from behave import *

# from Base.object import objects
import time

from seleniumpagefactory import PageFactory

from Base.Browser import browser


# class homepage(PageFactory):
#     def __init__(self, driver):
#         self.driver = driver
#
#     locators = {
#             "Flights":("XPATH","//a[text()=' FLIGHTS ']")
#         }
#     def click_Flights(self):
#         self.Flights.click_button()
#         windowlist = self.driver.window_handles
#         print(len(windowlist))
#         self.driver.switch_to.window(windowlist[1])
class Flights(PageFactory):
    def __init__(self,driver):
        self.driver=driver
        self.timeout=120
        self.highlight=True

    locators ={
        "origin" : ("ID","stationFrom"),
        "stext" : ("XPATH","//div[text()='Hyderabad (HYD)']"),
        "destination":("ID","stationTo"),
        "etext":("XPATH","//div[text()='Tirupati (TIR)']"),
        "departure":("ID","originDate"),
        "month":("XPATH","//div[contains(@class,'rdeparturedate')]//span[text()='October']"),
        "day":("XPATH","//span[text()=' 30']"),
        "search":("XPATH","//button[text()='Search ']"),
        "modify":("XPATH","//button[text()='Modify ']")
    }

    def starting(self):
        self.origin.set_text('Hyderabad')
        time.sleep(5)
        self.stext.click_button()
    def ending(self):
        self.destination.set_text("Tirupati")
        self.etext.click_button()
        time.sleep(4)
    def dep(self):
        self.departure.set_text("1")
        time.sleep(3)
        self.month.click_button()
        time.sleep(3)
        self.day.click_button()
        time.sleep(3)
    def  search_button(self):
        self.search.click_button()

    def modify_button(self):
        a =self.modify.is_displayed()
        assert  a
        print(a)
        time.sleep(5)


# home = None
# flights = None

#
# @given(u'click on Flights option')
# def step_impl(context):
#     # objects.dic['home'].click_Flights()
#     global home
#     home = homepage(browser.driver)
#     home.click_Flights()
#     allure.attach(browser.driver.get_screenshot_as_png(), name="HOME", attachment_type=AttachmentType.PNG)



@when(u'Enter origin as "HYD" select "HYD" from list')
def step_impl(context):
    # objects.dic['Flights'].starting()
    global flights
    flights = Flights(browser.driver)
    flights.starting()
    allure.attach(browser.driver.get_screenshot_as_png(), name="Origin city", attachment_type=AttachmentType.PNG)



@when(u'Enter destination as "TIR" Select "TIR" from list')
def step_impl(context):
    # objects.dic['Flights'].ending()
    flights.ending()
    allure.attach(browser.driver.get_screenshot_as_png(), name="destination city", attachment_type=AttachmentType.PNG)



@when(u'Select departure month as "OCTOBER" and date as "26"')
def step_impl(context):
    # objects.dic['Flights'].dep()
    flights.dep()
    allure.attach(browser.driver.get_screenshot_as_png(), name="Month & Date", attachment_type=AttachmentType.PNG)


@when(u'click on search')
def step_impl(context):
    # objects.dic['Flights'].search_button()
    flights.search_button()
    allure.attach(browser.driver.get_screenshot_as_png(), name="Search", attachment_type=AttachmentType.PNG)


@then(u'modify button appears')
def step_impl(context):
    # objects.dic['Flights'].modify_button()
    flights.modify_button()
    allure.attach(browser.driver.get_screenshot_as_png(), name="list", attachment_type=AttachmentType.PNG)
