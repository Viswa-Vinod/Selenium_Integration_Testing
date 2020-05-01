from selenium import webdriver

# download chrome driver from https://sites.google.com/a/chromium.org/chromedriver/home
# pip install selenium
chrome_browser = webdriver.Chrome('./chromedriver')


chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Show Message' in chrome_browser.page_source


show_message_button = chrome_browser.find_element_by_css_selector('#get-input > button')
show_message_button_text = show_message_button.get_attribute("innerHTML")

assert show_message_button_text == "Show Message"

user_message_input = chrome_browser.find_element_by_id('user-message')
user_message_input.clear()
user_message_input.send_keys("sample message sent from python code")

show_message_button.click()

display_span = chrome_browser.find_element_by_id('display')
display_text = display_span.get_attribute('innerHTML')

assert display_text == "sample message sent from python code"

chrome_browser.quit()
