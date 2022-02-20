from selenium import webdriver
from selenium.webdriver.common import keys
import time
chrome_driver_path = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://cutm.icloudems.com/corecampus/index.php")
time.sleep(2)
user_id = driver.find_element_by_name("userid")
user_id.send_keys("your registration number here")
password = driver.find_element_by_name("pass_word")
password.send_keys("your password here")
time.sleep(2)
submit = driver.find_element_by_id("formsubmitbutton")
submit.click()
driver.get("https://cutm.icloudems.com/corecampus/student/attendance/subwise_attendace_new.php")
