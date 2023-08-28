# import time
#
# from seleniumpagefactory import PageFactory
#
#
# class Flights(PageFactory):
#     def __init__(self,driver):
#         self.driver=driver
#         self.timeout=120
#
#     locators ={
#         "origin" : ("ID","stationFrom"),
#         "stext" : ("XPATH","//div[text()='Hyderabad (HYD)']"),
#         "destination":("ID","stationTo"),
#         "etext":("XPATH","//div[text()='Tirupati (TIR)']"),
#         "departure":("ID","originDate"),
#         "month":("XPATH","//div[contains(@class,'rdeparturedate')]//span[text()='October']"),
#         "day":("XPATH","//span[text()=' 30']"),
#         "search":("XPATH","//button[text()='Search ']"),
#         "modify":("XPATH","//button[text()='Modify ']")
#     }
#
#     def starting(self):
#         self.origin.set_text('Hyderabad')
#         time.sleep(5)
#         self.stext.click_button()
#     def ending(self):
#         self.destination.set_text("Tirupati")
#         self.etext.click_button()
#         time.sleep(4)
#     def dep(self):
#         self.departure.set_text("1")
#         time.sleep(3)
#         self.month.click_button()
#         time.sleep(3)
#         self.day.click_button()
#         time.sleep(3)
#     def  search_button(self):
#         self.search.click_button()
#
#     def modify_button(self):
#         assert self.modify.is_displayed()
#         time.sleep(5)
#
#
#
