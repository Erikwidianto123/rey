from time import time
from selenium.common.exceptions import *
import time
from objClass import object

class run():
    Obj = object()
    Obj.driver.maximize_window()
    Obj.driver.switch_to.window(Obj.driver.current_window_handle)
    time.sleep(2)
    Obj.driver.get(Obj.url)
    time.sleep(10)
    Obj.driver.find_element_by_xpath(Obj.btnCookie).click()
    time.sleep(3)
    Obj.driver.find_element_by_xpath(Obj.BtnSearchPockemon).click()
    time.sleep(3)
    Obj.driver.find_element_by_xpath(Obj.txtSearch).send_keys('Pikachu')
    time.sleep(3)
    Obj.driver.find_element_by_xpath(Obj.btnSearch2).click()
    time.sleep(3)
    Obj.driver.find_element_by_xpath(Obj.listDetail).click()
    time.sleep(3)
    txt = Obj.driver.find_element_by_xpath(Obj.assertion1)
    time.sleep(3)
    assert "Pikachu #025" in txt.text, "Data Yang muncul tidak sama dengan yang di input di pencarian!"
    time.sleep(3)
    Obj.driver.execute_script("window.scrollTo(0,800)")
    time.sleep(3)
    Obj.driver.find_element_by_xpath(Obj.exploreMore).click()
    time.sleep(3)
    Obj.driver.execute_script("window.scrollTo(0,800)")
    time.sleep(3)
    Obj.driver.find_element_by_xpath(Obj.loadMore).click()
    time.sleep(3)
    height = 800
    for i in range(10):
        time.sleep(3)
        Obj.driver.execute_script("window.scrollTo(0," + str(height * i) + ")")
        time.sleep(3)

run()
