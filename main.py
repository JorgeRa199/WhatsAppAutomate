import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

message = "Oye"

options = Options()
options.add_argument("--user-data-dir-chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# CHROME WEB DRIVER PATH
driver = webdriver.Chrome(
    'chromedriver.exe', options=options)
driver.maximize_window()
# YOU NEED TO BE AUTHENTICATED IN WHATSAPPWEB
driver.get('https://web.whatsapp.com')

time.sleep(30)
driver.find_element_by_xpath("//*[@title='Jorge']").click()

for x in range(30):
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    time.sleep(1.5)

time.sleep(10)
driver.close()
