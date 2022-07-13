from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url = "http://demo.guru99.com/test/newtours/"
driver.get(url)

actual_title = driver.title
expected_title = 'Welcome: Mercury'

if actual_title != expected_title:
    print('Test failed')
else:
    print('Test passed')
