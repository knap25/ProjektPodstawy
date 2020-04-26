import unittest
from selenium import webdriver
from time import sleep # sleep(2)
# import time ->  time.sleep(2)

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.sukienkimm.pl/")
        self.driver.maximize_window()

    def testSelenium(self):
        driver = self.driver
        print("Wylaczam alert")
        al = driver.find_element_by_id("onesignal-popover-cancel-button")
        al.click()
        print("Klikam zaloguj sie")
        zaloguj_btn = driver.find_element_by_xpath('//span[text()=" zaloguj się"]')
        zaloguj_btn.click()
        # Sleep tylko w celach debagowych
        sleep(2)

    def tearDown(self):
        print("sprzatanie po tescie")
        self.driver.quit()