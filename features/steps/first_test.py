# -*- coding: utf-8 -*-
from selenium import webdriver
from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Откроем браузер Мозилла
@given('browser Firefox')
def step(context):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()

#Откроем браузер Crome
@given('browser Chrome')
def step(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

#Введем текст в строку поиска
@then('enter text "{text}"')
def step(context, text):
    assert context.browser.find_element(By.XPATH, '//input[@id="text"]').send_keys("kek", Keys.ENTER)

@then('website "{url}"')
def step(context, url):
    context.browser.get(url)





#Введем текст в строку поиска
#@then("enter text '{text}'")
#def step(context, text):
   # context.browser.find_element(By.XPATH, '//input[@id="text"]').send_keys('google', Keys.ENTER)


#Теперь нажмем на кнопку "Найти"
#@then("push button with text '{text}'")
#def step(context, text):
    #WebDriverWait(context.browser, 120).until(
        #EC.element_to_be_clickable((By.class_name, 'button'))
    #)
    #context.browser.find_element_by_class_name('button').click()

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
#@then("page include text '{text}'")
#def step(context, text):
    #WebDriverWait(context.browser, 120).until(
        #EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    #)
    #assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    #context.browser.quit()
