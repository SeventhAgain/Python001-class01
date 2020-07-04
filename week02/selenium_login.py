# -*- coding:utf-8 -*-

from selenium import webdriver
import time

try:
    login_url = "https://shimo.im/login?from=home"
    browser = webdriver.Chrome()
    browser.get(login_url)

    browser.find_element_by_xpath("//input[@name='mobileOrEmail']").send_keys("15764336100")

    browser.find_element_by_xpath("//input[@name='password']").send_keys("123456")

    time.sleep(5)
    browser.find_element_by_xpath("//button[contains(text(), '立即登录')]").click()

    cookie = browser.get_cookies()
    print(cookie)
except Exception as e:
    print(e)
