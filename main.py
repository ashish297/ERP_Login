from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import constants as const

# Path to your Chrome User Data
user_data_dir = f'{const.CHROME_USER_DATA_DIRECTORY}'  # Replace with your path

# Name of the specific profile
profile_name = "Profile 5"  # Replace with your desired profile name from the directory

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument(f"--profile-directory={profile_name}")
chrome_options.add_experimental_option("detach", True)  # prevent closing of browser after the script ends
# remove the "controlled by automation" message in chrome browser
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# Suppress console warnings
chrome_options.add_argument("--log-level=3")  # INFO=0, WARNING=1, LOG_ERROR=2, LOG_FATAL=3

# Initialize the WebDriver with options
service = Service(f"{const.SELENIUM_DRIVER_PATH}")  # Replace with the path to your ChromeDriver executable
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://erp.iitkgp.ac.in/")
driver.maximize_window()
driver.implicitly_wait(15)

# User Details
roll_no = const.YOUR_ROLL_NUMBER
password = const.YOUR_PASSWORD
your_school = const.YOUR_SCHOOL
your_fav_singer = const.YOUR_FAV_SINGER
your_fav_sport = const.YOUR_FAV_SPORT

roll_no_element = driver.find_element(By.ID, "user_id")
roll_no_element.clear()
roll_no_element.send_keys(roll_no)
time.sleep(1)
password_element = driver.find_element(By.ID, "password")
password_element.send_keys(password)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "answer_div")))
time.sleep(1)
security_question_element = driver.find_element(By.ID, "question")
security_question_input_element = driver.find_element(By.ID, "answer")

if str(security_question_element.text.strip()) == "Your First School ?":
    security_question_input_element.send_keys(your_school)
elif str(security_question_element.text.strip()) == "Your Favorite Singer ?":
    security_question_input_element.send_keys(your_fav_singer)
elif str(security_question_element.text.strip()) == "Your Favorite Sport ?":
    security_question_input_element.send_keys(your_fav_sport)

# Send OTP button
otp_button = driver.find_element(By.ID, "getotp")
otp_button.click()

# accepting the alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# Open gmail in another tab
driver.execute_script('window.open('');')
driver.switch_to.window(driver.window_handles[1])
driver.get("https://mail.google.com/")

# refresh mails
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-tooltip="Refresh"]')))
refresh_element = driver.find_element(By.CSS_SELECTOR, 'div[data-tooltip="Refresh"]')
refresh_element.click()
time.sleep(5)

# extracting OTP
OTP = ""
all_mails_subjects = driver.find_elements(By.CLASS_NAME, 'bog')
for subject in all_mails_subjects:
    if "OTP for Sign In in ERP Portal of IIT Kharagpur is" in str(subject.get_attribute('innerText').strip()):
        otp_line = str(subject.get_attribute('innerText').strip())
        words = otp_line.split()
        for word in words:
            if word.isdigit():
                OTP = word
                break

        break

print(OTP)
driver.switch_to.window(driver.window_handles[0])  # tab back to erp

otp_input_element = driver.find_element(By.ID, "email_otp1")
otp_input_element.send_keys(OTP)

sign_in_button = driver.find_element(By.ID, "loginFormSubmitButton")
sign_in_button.click()
