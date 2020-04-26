import unittest
from selenium import webdriver
from time import sleep # sleep(2)
# import time ->  time.sleep(2)

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
        self.driver = webdriver.Firefox()
    #zadanie pkt 1
        self.driver.get("https://www.sukienkimm.pl/")
    #powiekszenie strony
        self.driver.maximize_window()

    def testSelenium(self):
    #zeby nie trzebabylo pisac self.driver wpisuje driver=
        driver = self.driver
        print("wylaczam alert")
        al = driver.find_element_by_id('onesignal-popover-cancel-button')
        al.click()
        print("klikam zaloguj sie")
        zaloguj_btn = driver.find_element_by_xpath('//span[text()=" zaloguj się"]')
        zaloguj_btn.click()
    #sleep tylko w celach debagowych
        sleep(2)


    def tearDown(self):
        print("sprzatanie po tesciee")
    #zamkniecie strony
        self.driver.quit()




if __name__=='__main__':
    unittest.main()