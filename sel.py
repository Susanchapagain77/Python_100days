from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


options = webdriver.FirefoxOptions()
profile = webdriver.FirefoxProfile('/home/susan/snap/firefox/common/.mozilla/firefox/rm3ci28a.Abc')
profile.set_preference('dom.webnotifications.enabled', False)  # disable web notifications
options.profile = profile
driver_path = "/home/susan/.cache/selenium/geckodriver/linux64/0.33.0/geckodriver"  # replace with the path to your geckodriver executable
service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service, options=options)
service.start()

# Test case 1: Verify that a user can successfully login with valid credentials
driver.get("https://www.hotstar.com/in") 
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("valid_username")
password.send_keys("valid_password")
login_button = driver.find_element_by_id("login-button")
login_button.click()
time.sleep(5)
assert "dashboard" in driver.current_url

# Test case 2: Verify that a user cannot login with invalid credentials
driver.get("https://www.hotstar.com/in")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("invalid_username")
password.send_keys("invalid_password")
login_button = driver.find_element_by_id("login-button")
login_button.click()
time.sleep(5)
assert "login" in driver.current_url

# Test case 3: Verify that the user is redirected to the dashboard page after successful login
driver.get("https://www.hotstar.com/in") 
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("valid_username")
password.send_keys("valid_password")
login_button = driver.find_element_by_id("login-button")
login_button.click()
time.sleep(5)
dashboard_button = driver.find_element_by_id("dashboard-button")
dashboard_button.click()
time.sleep(5)
assert "dashboard" in driver.current_url

# Close the browser
driver.close()


# from jmeter_api import JMeterTest

# test = JMeterTest()

# # Add a Thread Group element
# thread_group = test.add_thread_group(name='My Thread Group', num_threads=10, ramp_time=5, loops=1)

# # Add an HTTP Request element to the Thread Group
# http_request = thread_group.add_http_request(name='My HTTP Request', url='https://www.example.com')

# # Add a Listener element to capture the results of the load test
# listener = test.add_listener(name='My Listener', type='summary')

# # Run the test
# test.run()
