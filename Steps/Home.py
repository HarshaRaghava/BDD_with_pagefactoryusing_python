import allure
from allure_commons.types import AttachmentType
from behave import *
from seleniumpagefactory import PageFactory

from Base.Browser import browser


class homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.highlight=True

    locators = {
            "Flights":("XPATH","//a[text()=' FLIGHTS ']")
        }
    def click_Flights(self):
        self.Flights.click_button()
        windowlist = self.driver.window_handles
        print(len(windowlist))
        self.driver.switch_to.window(windowlist[1])


@given(u'click on Flights option')
def step_impl(context):
    # objects.dic['home'].click_Flights()
    global home
    home = homepage(browser.driver)
    allure.attach(browser.driver.get_screenshot_as_png(), name="IRCTC", attachment_type=AttachmentType.PNG)
    home.click_Flights()
    allure.attach(browser.driver.get_screenshot_as_png(), name="HOME", attachment_type=AttachmentType.PNG)
