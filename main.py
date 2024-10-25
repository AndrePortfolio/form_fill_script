# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  ____   ____       ____     ___                 #
#                 / ___| / ___|     | ___|   / _ \                #
#                | |     \___ \     |___ \  | | | |               #
#                | |___   ___) |     ___) | | |_| |               #
#                 \____| |____/     |____/   \___/                #
#                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from	selenium import webdriver
from	selenium.webdriver.common.by import By
from	selenium.webdriver.common.keys import Keys
from	selenium.webdriver.support.ui import WebDriverWait
from	selenium.webdriver.support import expected_conditions as EC
import	time
import	csv
import	sys

if len(sys.argv) != 2:
	sys.exit("Usage: python your_script.py <path_to_csv>")

csv_file_path = sys.argv[1]
people = []

# Read the CSV file
with open(csv_file_path, mode='r') as file:
	csv_reader = csv.DictReader(file)
	for row in csv_reader:
		people.append(row)

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get('https://www.google.pt/?hl=pt-PT')
driver.maximize_window()

try:
	# Wait for the consent pop-up and click "Accept All"
	accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Aceitar tudo"]')))
	accept_button.click()

	# Wait for the Google search bar to load
	search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

	search_bar.send_keys('Practice Form on Automation')
	search_bar.send_keys(Keys.RETURN)	# Press Enter to search

	# Wait for search results to load
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search')))

	# Find and click the first result link
	site = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Practice Form"]')))
	site.click()

	# Wait for the form to load (you may need to adjust this to wait for the specific form)
	time.sleep(1)
	first_name = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="firstName"]')))
	first_name.send_keys(people[0]['Name'])

	time.sleep(1)
	last_name = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lastName"]')))
	last_name.send_keys(people[0]['Last Name'])

	time.sleep(1)
	email = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
	email.send_keys(people[0]['Email'])

	time.sleep(1)
	if people[0]['Gender'] == "Male":
		gender_xpath = '//*[@for="gender-radio-1"]'
	elif people[0]['Gender'] == "Female":
		gender_xpath = '//*[@for="gender-radio-2"]'
	else:
		gender_xpath = '//*[@for="gender-radio-3"]'
	gender = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, gender_xpath)))
	gender.click()

	time.sleep(1)
	mobile_number = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userNumber"]')))
	mobile_number.send_keys(people[0]['Mobile Number'])








	time.sleep(1)
	birthday = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dateOfBirth"]')))
	birthday.send_keys(people[0]['Date of Birth'])

	time.sleep(1)
	subject = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="subjectsContainer"]')))
	subject.send_keys(people[0]['Subject'])

	time.sleep(1)
	address = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="currentAddress"]')))
	address.send_keys(people[0]['Address'])

	# Optional: Wait to observe the result
	time.sleep(10)

finally:
	# Close the browser
	driver.quit()

