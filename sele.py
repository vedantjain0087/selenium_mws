#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium import webdriver
from pyvirtualdisplay import Display
import os
from selenium.webdriver.chrome.options import Options 
import time
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from datetime import timedelta
from selenium.webdriver.common.keys import Keys


options = Options()
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('https://sellercentral.amazon.com./')
driver.find_element_by_xpath('//*[@id="sign-in-button"]/button').click()
username = driver.find_element_by_xpath('//*[@id="ap_email"]')
password = driver.find_element_by_xpath('//*[@id="ap_password"]')
username.send_keys("mainvedant.vns123@gmail.com")
password.send_keys("tony0087")
driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
otp = raw_input()
driver.find_element_by_xpath('//*[@id="auth-mfa-otpcode"]').send_keys(otp)
driver.find_element_by_xpath('//*[@id="auth-signin-button"]').click()


hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="sc-navtab-reports"]/a'))
hover.perform()
driver.find_element_by_xpath('//*[@id="sc-navtab-reports"]/ul/li[4]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="report_DetailSalesTrafficBySKU"]').click()
time.sleep(5)




today = datetime.date.today()
week_ago = today - datetime.timedelta(days=7)
for x in range(0,7):
    week_ago = week_ago + timedelta(days=1)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="toDate2"]')).double_click().perform()
    driver.find_element_by_xpath('//*[@id="toDate2"]').clear()
    driver.find_element_by_xpath('//*[@id="toDate2"]').send_keys(str(week_ago))
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="toDate2"]').send_keys(Keys.RETURN)
    time.sleep(3)

    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="fromDate2"]')).double_click().perform()
    driver.find_element_by_xpath('//*[@id="fromDate2"]').clear()
    driver.find_element_by_xpath('//*[@id="fromDate2"]').send_keys(str(week_ago))
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="fromDate2"]').send_keys(Keys.RETURN)
    time.sleep(3)

    hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="export"]')).click()
    hover.perform()
    driver.find_element_by_xpath('//*[@id="downloadCSV"]').click()
    time.sleep(3)

