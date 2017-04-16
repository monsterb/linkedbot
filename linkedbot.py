#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: linkedbot - A bot to automate Chrome web browser tasks.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    linkedbot.py
# version:     0.00

from selenium import webdriver
import time


def login_linkedin(my_email, my_password):

    chromedriver = webdriver.Chrome(executable_path = '/home/monsterb/Downloads/chromedriver')

    url = 'https://www.linkedin.com/uas/login'

    chromedriver.get(url)

    email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')
    email.send_keys(my_email)

    password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')
    password.send_keys(my_password)

    sign_in = chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')
    sign_in.click()

    time.sleep(15)

login_linkedin('email','password')

chromedriver.quit()
