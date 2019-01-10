class papaJohns:
    def __init__(self, address, posCode, size, toppingsNum, qty):
        self.address = address
        self.posCode = posCode
        self.size = size
        self.toppingsNum = toppingsNum
        self.qty = qty
        
    def findCost(self):    
        import csv
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.expected_conditions import (
            presence_of_element_located)
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.chrome.options import Options
        
        
        #options = Options()
        #options.headless = True
        #driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/lenov/seleniumWebDriver/chromedriver.exe')
        driver = webdriver.Chrome(executable_path="C:/Users/lenov/seleniumWebDriver/chromedriver.exe")
        
        #opens Papa John's webapage using Selenium Webdriver
        driver.get("https://www.papajohns.com/")
        
        #navigates to address page
        driver.find_element_by_xpath('/html/body/header/nav/div/div/div/ul/li[1]/a').click()
        
        #enters address and postal code to text boxes
        addressTB = driver.find_element_by_xpath('//*[@id="locations-streetaddress"]')
        addressTB.send_keys(self.address)
        
        posCodeTB = driver.find_element_by_xpath('//*[@id="locations-postalcode"]')
        posCodeTB.send_keys(self.posCode)
        
        #naviagtes to menu
        driver.find_element_by_xpath('//*[@id="locations-form"]/div[9]/input').click()
        
        #enters build pizza menu
        wait = WebDriverWait(driver, 10)
        buildPizza = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/section[1]/div[1]/ul/li/form/button')))
        buildPizza.click()
        
        
        #selects size using radio buttons
        sizes = driver.find_element_by_xpath('//*[@id="size_0"]/fieldset[2]/div')
        buttons = sizes.find_elements_by_tag_name('input')
        for button in buttons:
            if (button.get_attribute("data-pizza-name") == self.size):
                driver.execute_script("arguments[0].click()", button)
                break
        
        #naviagtes to toppings menu
        driver.find_element_by_xpath('/html/body/div[2]/main/form/div/div/div/div[3]/ul/li[4]/a').click()
        
        #adds specified number of toppings
        toppingsTable = driver.find_element_by_xpath('//*[@id="Fresh-Veggies_0"]/fieldset/ul')
        toppings = toppingsTable.find_elements_by_tag_name('li')
        i = 1
        for topping in toppings:
            topping.click()
            i+=1
            if (i > self.toppingsNum):
                break
            
        #selects quantity of pizzas using drop down menu
        select_element = Select(driver.find_element_by_xpath('//*[@id="quantity"]'))
        select_element.select_by_index(self.qty-1)
        
        #adds to cart
        driver.find_element_by_xpath('//*[@id="Fresh-Veggies_0"]/nav/button').click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cart"]/a/span[1]')))
        
        #navigates to cart menu
        driver.find_element_by_xpath('//*[@id="cart"]/a').click()
        
        #finds price
        total = driver.find_element_by_xpath('//*[@id="vcFormId"]/table/tbody/tr[5]/td[2]/h3')
        return total.text
        
p1 = papaJohns("433 Brock Street", "K7L1T5", "Small", 2, 1)
print(p1.findCost())