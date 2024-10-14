# # This is lesson 4 assignment

# # Download, extract and move geckodriver & chromedriver to working folder
# # Chromedriver
# # https://googlechromelabs.github.io/chrome-for-testing/
# # Export path to chromedriver to PATH (export PATH=$PATH:/home/ken/Desktop/DevOps_Online_Training/github/to_github/chromedriver)
# # Geckodriver
# # https://github.com/mozilla/geckodriver/releases
# # Export path to geckodriver to PATH (export PATH=$PATH:/home/ken/Desktop/DevOps_Online_Training/github/to_github/geckodriver)
# # Remove the snap installer version of firefox (https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz)
# # Update, upgrade and install firefox using apt 
# #
# # Activate said environment (source env/bin/activate)
# # Install selenium (pip install selenium)

# from selenium import webdriver

# # Import time
# import time

# # Let the user provide the link they want to open
# website = input("Please provide the website you want to open:\n")
# # Let the user choose between Chrome and Firefox
# chromeOfirefox = input("Choose either 'chrome' or 'firefox':\n")

# # The webdriver.Chrome function
# # This opens the provided link in Chrome
# def open_with_chrome(website):
#     # Initialize the chrome driver
#     chrome_driver = webdriver.Chrome()
#     # And call the website using the driver variable
#     chrome_driver.get(website)

# # Call the function
# # open_with_chrome(website)

# # The webdriver.Firefox function
# # This open the provided link in Firefox
# def open_with_firefox(website):
#     # Initialize the chrome driver
#     firefox_driver = webdriver.Firefox()
#     # And call the website using the driver variable
#     firefox_driver.get(website)
#     # Delay the browser on screen for specified time
#     time.sleep(20)

# # Call the function
# # open_with_firefox(website)

# # Add the logic
# if chromeOfirefox == "chrome":
#     open_with_chrome(website)
# elif chromeOfirefox == "firefox":
#     open_with_firefox(website)
# else:
#     print("Choose either 'chrome' or 'firefox'")

# website = "https://ubuntu.com/"
##################################################################################

# 2.
# It's the same link
##################################################################################

# 3.
# Yes
##################################################################################

# # 4. 
# # Open Google Translate web page
# # Write anything in Hebrew in the text area

# # Import Selenium
# from selenium import webdriver
# # Import time
# import time
# # Import By
# from selenium.webdriver.common.by import By

# # Let the user provide the link they want to open
# # website = input("Please provide the website you want to open:\n")
# website = "https://translate.google.com/?sl=auto&tl=es&op=translate"

# # And also provide the words to translate
# # users_words = input("What do you want to translate?\n")
# users_words = "לְשַׁכֵּן"
# # Initialize the chrome driver
# chrome_driver = webdriver.Chrome()

# # The webdriver.Chrome function
# # This open the provided link in Chrome
# def open_with_chrome(website):
#     # And call the website using the driver variable
#     chrome_driver.get(website)
#     time.sleep(5)

#     # This accepts the cookies
#     chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span").click()
#     time.sleep(5)

# # Write something in the receiving box
# def to_translate():
#     # change_language = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button').click()
#     to_translate_location = chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea")
#     to_translate_location.send_keys(users_words)
#     # Select the language to translate it to
#     # language_to_translate_to = chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button")
#     # path_to_eng = "//div[@class='qSb8Pe RCaXn KKjvXb']//div[@class='Llmcnf'][normalize-space()='English']"
#     # language_to_translate_to_eng = chrome_driver.find_element(By.XPATH, path_to_eng)
#     # language_to_translate_to_eng.click()
#     time.sleep(5)

# # Call the function
# open_with_chrome(website)
# to_translate()
#############################################################################################

# # 5.
# # Open a Youtube web page
# # Type a name of a song
# # Click on search

# # Import webdriver
# from selenium import webdriver
# # Import By
# from selenium.webdriver.common.by import By
# # Import keys
# from selenium.webdriver.common.keys import Keys
# # Import time
# import time

# # Initialize the webdriver
# chrome_driver = webdriver.Chrome()

# # Get the website
# website = "https://www.youtube.com/"
# song_search = "top rap music"

# chrome_driver.get(website)
# time.sleep(5)

# # This accepts the cookies
# accept_cookies = chrome_driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div").click()
# time.sleep(3)

# # Go to the search area
# path_to_search = "//input[@id='search']"
# search_area = chrome_driver.find_element(By.XPATH, path_to_search)
# # Type in the given text
# search_area.send_keys(song_search)

# # Press enter
# search_area.send_keys(Keys.ENTER)

# time.sleep(10)
#################################################################################

# # 6.
# # Open Chrome browser on Google Translate website:
# # https://translate.google.com/
# #  Find translation text field (the one you send keys to)
# # with 3 different locators and print the WebElement
# # you created.

# # Import webdriver
# from selenium import webdriver
# # Import By
# from selenium.webdriver.common.by import By
# # Import keys
# from selenium.webdriver.common.keys import Keys
# # Import time
# import time

# # Initialize the webdriver
# chrome_driver = webdriver.Chrome()

# # Get the website
# website = "https://translate.google.com/"

# chrome_driver.get(website)
# time.sleep(5)

# # This accepts the cookies
# accept_cookies = chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button").click()
# time.sleep(3)

# # WebElement created
# # <textarea aria-label="Source text" aria-autocomplete="list" aria-expanded="false" aria-controls="kvLWu" class="er8xn" jsaction="blur:TP1Wfd; click:R8nDBd; focus:HCeAxb; input:r9XDpf,Gyn8rd; keydown:O0Dsab,RHer4; select:BR6jm,RHer4; paste:puy29d;" jsname="BJE2fc" jslog="176025; track:click,input,paste;" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" rows="1" placeholder="" spellcheck="false" style="height: 32px;"></textarea>

# # cssSelector
# # #yDmH0d > c-wiz > div > div.ToWKne > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > div > c-wiz > span > span > div > textarea

# # XPATH
# # //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea

# # class name
# # driver.find_element(By.className("rm1UF UnxENd"))
################################################################################################################################################################

# # 7.
# # Open Chrome browser on Facebook website
# # https://www.facebook.com/
# #  Login into Facebook (No need to send me credentials).

# Import webdriver
# from selenium import webdriver
# # Import By
# from selenium.webdriver.common.by import By
# # Import Keys
# from selenium.webdriver.common.keys import Keys
# # Import time
# import time

# # Initialize the webdriver
# chrome_driver = webdriver.Chrome()
# # Give the website a variable
# website = "https://www.facebook.com/"

# # Open the website
# chrome_driver.get(website)
# chrome_driver.maximize_window()

# # Decline optional cookies
# path = "//*[@id='facebook']/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]"
# decline_optional_cookies = chrome_driver.find_element(By.XPATH, path)
# decline_optional_cookies.click()

# # Put a delay here
# time.sleep(3)

# # Fill in email
# email_address = "kk@gmail.com"
# path_to_email = "//input[@id='email']"
# email_location = chrome_driver.find_element(By.XPATH, path_to_email)
# email_location.send_keys(email_address)

# # Fill in password
# password = "1234567890"
# path_to_password = "//input[@id='pass']"
# password_location = chrome_driver.find_element(By.XPATH, path_to_password)
# password_location.send_keys(password)
# password_location.send_keys(Keys.ENTER)

# # Delay the closing
# time.sleep(25)
#########################################################################################

# # 8.
# # Open Chrome browser on any webpage.
# # Delete all cookies from browser.
# # Make sure all cookies are deleted by printing all cookies
# # stored in the browser.

# # Import webdriver
# from selenium import webdriver
# # Import By
# from selenium.webdriver.common.by import By
# # Import ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# # Import time
# import time

# # Initialize the webdriver
# chrome_driver = webdriver.Chrome()
# # Give the website a variable
# website = "https://www.facebook.com/"

# # # Create a cookie
# # cookie = {
# #         'name': 'cookie_name',
# #         'value': 'cookie_value',
# #         'path': '/',
# #         'domain': "https://www.facebook.com/",
# #         'secure': False, # Set to True if the cookie should be secure
# #         'httpOnly': False, # Set to True if the cookie should be HTTP only
# #     }

# chrome_driver.get(website)
# chrome_driver.maximize_window()

# # Accept cookies
# allow_all_cookies = chrome_driver.find_element(By.XPATH, "//*[@id='facebook']/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]")
# allow_all_cookies.click()

# # Decline cookies
# # decline_optional_cookies = chrome_driver.find_element(By.XPATH, "//*[@id='facebook']/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]")
# # decline_optional_cookies.click()

# # Delay here
# time.sleep(3)

# # Get cookies and print them on screen
# cookies = chrome_driver.get_cookies()
# print(cookies)

# # Delay here
# time.sleep(5)

# # chrome_driver.add_cookie(cookie)
# chrome_driver.delete_all_cookies()

# # Delay here
# time.sleep(5)

# # Get cookies and print them on screen
# cookies = chrome_driver.get_cookies()
# print(cookies)

# # Delay here
# time.sleep(5)
#######################################################################################################

# # 9.
# # Open any browser on "Github" website.
# #  https://github.com/
# #  Enter “Selenium” keyword in search textfield
# #  Press Enter to search (through code - of course).

# # Import Selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize webdriver
# chrome_driver = webdriver.Chrome()

# # Open website
# website = "https://github.com"
# chrome_driver.get(website)
# chrome_driver.maximize_window()

# # Delay here
# time.sleep(3)

# # Click on the search button
# search_button = chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input")
# search_button.click()

# # Add the words selenium in the search bar
# add_words_in_search_bar = chrome_driver.find_element(By.ID, "query-builder-test")
# add_words_in_search_bar.send_keys("selenium")
# # This presses enter
# add_words_in_search_bar.send_keys(Keys.ENTER)

# # Delay here
# time.sleep(13)
#####################################################################################

# 10.
# Find a way to disable all extensions in
# o Chrome
# o Firefox
# o Internet Explorer.
#  Run browsers without extensions.

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# website = "https://www.facebook.com"

# # This is the webdriver for chrome
# def chrome_browser():
#     chrome_driver   = webdriver.Chrome()
#     chrome_driver.get(website)
#     chrome_options = webdriver.ChromeOptions()
#     # Disable extensions
#     chrome_options.add_argument('--disable-extensions')
#     time.sleep(4)
#     chrome_driver.quit()

# chrome_browser()


# # This is the webdriver for chrome
# def firefox_browser():
#     firefox_driver  = webdriver.Firefox()
#     firefox_driver.get(website)
#     firefox_options = webdriver.FirefoxOptions()
#     firefox_options.add_argument('--disable-extensions')
#     time.sleep(44)
#     firefox_driver.quit()

# firefox_browser()


# # This is the webdriver for Internet Explorer
# def ie_browser():
#     ie_driver  = webdriver.Ie()
#     ie_driver.get(website)
#     ie_options = webdriver.IeOptions()
#     ie_options.add_argument('--disable-extensions')
#     time.sleep(4)
#     ie_driver.quit()

# ie_browser()