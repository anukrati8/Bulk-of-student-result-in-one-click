from selenium import webdriver
from time import sleep

eno_list = [146891369,
157048394,
122341030,
147560163,
151983259,
155402167]

driver = webdriver.Chrome(executable_path='C:/Users/DELL/Desktop/web/chromedriver.exe')
driver.maximize_window()

for i in range (len(eno_list)):
    driver.get ("https://termendresult.ignou.ac.in/TermEndJune21/TermEndJune21.asp")    
    enrollment = driver.find_element_by_name("eno")
    enrollment.send_keys(eno_list[i])
    submit = driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()
    filename = str(eno_list[i])+".png"
    driver.save_screenshot(filename)
    driver.back()
    driver.back()
    


