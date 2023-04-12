
# Importing necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setting Chrome options to disable notifications and popups, and start the browser maximized
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("start-maximized")

# Creating a new instance of Chrome browser with the specified options
browser = webdriver.Chrome(options=chrome_options)

# Navigating to Facebook's login page
browser.get('https://www.facebook.com/login')

# Waiting for 2 seconds
time.sleep(2)

# Filling in the login details and pressing the 'Enter' key to log in
email = browser.find_element(By.ID, 'email')
email.send_keys('YOUR EMAIL' + Keys.TAB)

password = browser.find_element(By.ID, 'pass')
password.send_keys('YOUR PASSWORD' + Keys.RETURN)

# Waiting for 10 seconds to allow the page to load completely
time.sleep(10)

# Navigating to Facebook Marketplace link
browser.get('https://web.facebook.com/marketplace/?ref=app_tab')

# Waiting for 5 seconds
time.sleep(5)

# Finding the search bar and entering the search term 'Bass'
search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input')
search.send_keys('Bass' + Keys.RETURN)

# Waiting for 10 seconds to allow the search results to load completely
time.sleep(10)

# Finding the Facebook element and scrolling down 50 times to load more items
fb = browser.find_element(By.ID, 'facebook')
for i in range(50):
    fb.send_keys(Keys.END)
    time.sleep(1)

# Finding all the listings and their corresponding links
baixos = browser.find_elements(By.CSS_SELECTOR, '.x1nrcals')
lista = []
links = browser.find_elements(By.TAG_NAME, 'a')
links = [a.get_attribute('href') for a in links]
links = [a for a in links if str(a).startswith("https://www.facebook.com/marketplace/item")]

# Iterating over the listings and extracting their name, price, and link, and storing them in a dictionary
for i, link in zip(baixos, links):
    nome = i.find_element(By.CSS_SELECTOR, '.xo1l8bm.xzsf02u .x1n2onr6').text
    preco = i.find_element(By.CSS_SELECTOR, '.x676frb.x1s688f').text
    lista.append({
            'Nome': nome,
            'Preço': preco,
            'URL': link
        })

# Converting the dictionary to a pandas DataFrame
df = pd.DataFrame(lista)

# Saving the DataFrame to a CSV file
df.to_csv('fb_bass.csv', index=False)

# Printing the DataFrame to the console
print(df)
