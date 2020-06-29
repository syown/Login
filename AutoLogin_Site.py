# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_binary
import json
import os
import signal



def Eneos_elec():
    try:
        json_open = open('info.json', 'r')
        json_load = json.load(json_open)
        loginId = json_load["Eneos_elec"]["userID"]
        loginPass = json_load["Eneos_elec"]["password"]
    
   #     ブラウザを開く。
        driver = webdriver.Chrome()
        driver.get("https://www.eneos-denki.jp/web/portal/login?_ga=2.116893379.454616050.1588981635-61412109.1588981635")
        #ログインID
        login_id = driver.find_element_by_id("userId")

        login_id.send_keys(loginId)
        #ログインパスワード
        login_pass = driver.find_element_by_id('password')
        login_pass.send_keys(loginPass)
        #ログインボタン
        login_btn = driver.find_element_by_xpath('//*[@id="wrapperLoginDefault"]/form/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/input')
        login_btn.click()
        #time.sleep(300)
    finally:
        #os.kill(driver.service.process.pid,signal.SIGTERM)
        print('a')

    
def Eneos_gas():
    try:
        json_open = open('info.json', 'r')
        json_load = json.load(json_open)
        loginId = json_load["Eneos_gas"]["userID"]
        loginPass = json_load["Eneos_gas"]["password"]

        # ブラウザを開く。
        driver = webdriver.Chrome()
        driver.get("https://www.eneos-gas.jp/portal/action/login/index?_ga=2.40743520.331454412.1588980270-848679447.1580815617")
        #ログインID
        login_id = driver.find_element_by_name('form.loginIdOrMailAddress')
        login_id.send_keys(loginId)
        #ログインパスワード
        login_pass = driver.find_element_by_name('form.userPassword')
        login_pass.send_keys(loginPass)
        #ログインボタン
        login_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div[5]/div/button')
        login_btn.click()
        #time.sleep(300)
    finally:
       #os.kill(driver.service.process.pid,signal.SIGTERM)
        print('a')