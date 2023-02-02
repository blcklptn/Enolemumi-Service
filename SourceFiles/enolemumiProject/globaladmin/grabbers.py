from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from time import sleep
import pathlib
import os
import requests
from threading import Thread
from .models import Cases
from datetime import datetime

class DriverMan:
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def killDriver(self, driver: webdriver) -> None:
        try:
            driver.close()
            driver.quit()
        except Exception as ex:
            print(ex)

    def downloadPDF(self, link: str) -> str:
        response = requests.get(link)
        name = link.split('/')[-1]
        with open(f'Datas/{name}', 'wb') as file:
            Cases.objects.create(path_to_file=f'Datas/{name}', site='tiesa')
            file.writelines(response)

        

class Tiesa(DriverMan):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
    
    def runTiesa(self):
        url = 'https://www.satv.tiesa.gov.lv/cases/?case-filter-years=&case-filter-status=%5B42%5D&case-filter-types=&case-filter-result=&searchtext='
        driver = webdriver.Chrome()
        driver.get(url)
        links = []
        for i in range(23):
            try:
                case = driver.find_element(By.XPATH, f'/html/body/div/div[1]/div/div/div[3]/div[2]/div/div[{str(i)}]').click()
                try:
                    first = driver.find_element(By.XPATH, f'/html/body/div/div[1]/div/div/div[3]/div[2]/div/div[{str(i)}]/div[4]/div[1]/a').get_attribute('href')
                    links.append(first.replace('https://www.satv.tiesa.gov.lv/web/viewer.html?file=', ''))
                except:
                    pass
                try:
                    second = driver.find_element(By.XPATH, f'/html/body/div/div[1]/div/div/div[3]/div[2]/div/div[{str(i)}]/div[4]/div[2]/a').get_attribute('href')
                    links.append(second.replace('https://www.satv.tiesa.gov.lv/web/viewer.html?file=', ''))
                except:
                    pass
            except:
                pass
        
        
        print(links)
        try:
            os.mkdir('Datas/')
        except:
            pass
        self.killDriver(driver)
        for i in links:
            
            self.downloadPDF(i)

class Run(Tiesa):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
    
    def run(self):
        self.runTiesa()