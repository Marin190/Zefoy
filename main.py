from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re


# Create a new instance of the Chrome driver

driver = webdriver.Chrome()

# Open the Python website

driver.get("https://zefoy.com")


input("resolve captcha : ")

driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button').click()
time.sleep(3)
inpu = driver.find_element(By.XPATH, "/html/body/div[10]/div/form/div/input")
inpu.send_keys("https://vm.tiktok.com/ZNdkcTJUg/")
time.sleep(2)
go = driver.find_element(By.XPATH, "/html/body/div[10]/div/form/div/div/button")
go.click()
time.sleep(3)
while True:
	timer = driver.find_element(By.XPATH, "/html/body/div[10]/div/div/span")
	if ("Please" in timer.text):
		print(timer.text, end="\r")
	else:
		try:
			go = driver.find_element(By.XPATH, "/html/body/div[10]/div/form/div/div/button")
			go.click()
			time.sleep(5)
			driver.find_element(By.XPATH, "/html/body/div[10]/div/div/div[1]/div/form/button").click()
			print("+500 vues")
		except:
			input("pub")

	time.sleep(5)
# Close the browser window

driver.close()
