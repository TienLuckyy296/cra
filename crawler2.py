from selenium import webdriver
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = "/Users/TienLN/Downloads/chromedriver-win64/chromedriver-win64"
driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()