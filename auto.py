from selenium import webdriver
import time

# # Set the path to the Chrome driver executable
driver_path = "chromedriver.exe"

# # Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Aman Syed\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = webdriver.Chrome(driver_path, options=options)
# # Navigate to the website
driver.get("https://play.decathlon.in/event-details/t-spark/79f7297e-a520-11ed-9932-f795308ff2fb")
driver.maximize_window()
time.sleep(2)
book_now = driver.find_element_by_xpath("//*[text()='BOOK NOW']")
book_now.click()
time.sleep(5)
name_field = driver.find_element_by_name('firstName')
last_field = driver.find_element_by_name('lastName')
name_field.send_keys('Aakash')
time.sleep(2)
last_field.send_keys('Gupta')
time.sleep(2)
mobile_field = driver.find_element_by_name('mobileNumber')
email_field = driver.find_element_by_name('email')
mobile_field.send_keys('9321456786')
time.sleep(2)
email_field.send_keys('johndoe123@gmail.com')
time.sleep(2)
# Click the Save button
save_button = driver.find_element_by_xpath("//button[@id='save-attendee']")
save_button.click()
time.sleep(5)
# Click the Checkbox
checkbox = driver.find_element_by_name('termsandcondition')
if not checkbox.is_selected():
    checkbox.click()
proceed_button = driver.find_element_by_xpath("//*[@id='rzp-button1']/span[2]")
proceed_button.click()
time.sleep(5)


driver.quit()

