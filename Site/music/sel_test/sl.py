from selenium import webdriver
import os
import time

linkcreate = "http://127.0.0.1:8000/music/create"
link_home = "http://127.0.0.1:8000/music/"

try:
    browser = webdriver.Chrome()
    browser.get(linkcreate)
    title = browser.find_element_by_id("id_title")
    title.click()
    title.send_keys("test")
    text = browser.find_element_by_id("id_full_text")
    text.click()
    text.send_keys("test")
    date = browser.find_element_by_id("id_date")
    date.click()
    date.send_keys("2021-12-22 10:15:20")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_audio.mp3')
    file = browser.find_element_by_id("id_audio")
    file.send_keys(file_path)
    button = browser.find_element_by_id("add_button")
    button.click()
    time.sleep(3)
    browser.get(link_home)
    time.sleep(3)
    button_info = browser.find_element_by_id("info")
    button_info.click()
    button_del = browser.find_element_by_id("del")
    button_del.click()
    button_delete = browser.find_element_by_id("delete")
    button_delete.click()
finally:
    time.sleep(30)
    browser.quit()