from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException, 
    StaleElementReferenceException, 
    NoSuchElementException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from PyQt5.QtWidgets import *


class Browser(object):

    def __init__(self, chromedriver_path):
        super(Browser, self).__init__()
        self.cdpath = chromedriver_path

        self.br = webdriver.Chrome(executable_path=self.cdpath)


    def get(self):
        print("get geçti") 
        self.br.maximize_window()

        self.br.get("https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp") 

    def switch_to_frame(self, locator):
        test_frame = self.element( 
            locator,
            wait_=True
        )
    
        self.br.switch_to.frame(test_frame)

    def element(self, locator, multiple = False, while_ = False, wait_ = False, wait_second = 60, click_ = False):
        if wait_:
            wait = WebDriverWait(self.br, wait_second)
            if while_:
                if click_:
                    while True:
                        try:

                            web_element_ = wait.until(
                                EC.element_to_be_clickable(locator)
                            )

                            web_element_.click()
                            
                            break
                        
                        except ElementClickInterceptedException:
                            continue

                        except StaleElementReferenceException:
                            continue  

                else:
                    while True:
                        try:
                            web_element_ = wait.until(
                                EC.element_to_be_clickable(locator)
                            )
                            
                            return web_element_
                            
                            break
                        
                        except ElementClickInterceptedException:
                            continue
                        
                        except StaleElementReferenceException:
                            continue


            else:
                web_element_ = wait.until(
                    EC.element_to_be_clickable(locator)
                )
                
                return web_element_

        else:
            try:
                if multiple:
                    web_element_ = self.br.find_elements_by_xpath(locator)
                    return web_element_

                else:
                    web_element_ = self.br.find_element_by_xpath(locator)
                    return web_element_

            except NoSuchElementException:
                return False


