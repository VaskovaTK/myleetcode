from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox(executable_path="E:\geckodriver.exe")
# browser = webdriver.Chrome(executable_path="E:\chromedriver.exe")
# browser.get("https://www.google.com/")
# browser = webdriver.Firefox()
browser.get("https://free.edu.1c.ru/library.html")
# browser.get("https://accounts.google.com/signin")
# textarea = browser.find_element(By.CLASS_NAME, value="whsOnd zHQkBf").send_keys("vaskova")
textarea = browser.find_element(By.ID, value="x-auto-25")
# textarea = browser.find_element_by_css_selector('#x-auto-24-input')
textarea.send_keys("vaskovatk")

# textarea = browser.find_element(By.ID, value="x-form-el-x-auto-24")
# textarea = browser.find_element_by_css_selector('#x-auto-25-input')
# textarea.send_keys("angeldj12@mail.ru")

# textarea2 = browser.find_element(By.ID, value= "x-form-el-x-auto-25" )
# textarea.send_keys("rbvfkbyf15")
# submit = browser.find_element(By.CLASS_NAME, value="x-btn-text ")
# submit = browser.find_element_by_class_name("x-btn-text")
# submit.click()