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


valid_cities = {
	'NCR': ['Delhi', 'Gurgaon', 'Noida'],
	'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
	'Haryana': ['Karnal', 'Panipat'],
	'Rajasthan': ['Jaipur', 'Jaiselmer']
}

valid_subjects = [
	'Maths', 'Accounting', 'Arts', 'Social Studies', 'Biology',
	'Physics', 'Chemisty', 'Computer Science', 'Commerce',
	'Economics', 'Civics', 'Hindi', 'English', 'History'
]


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

	#first name
	first_name = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="firstName"]')))
	first_name.send_keys(people[0]['Name'])

	#last name
	last_name = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lastName"]')))
	last_name.send_keys(people[0]['Last Name'])

	#email
	email = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
	email.send_keys(people[0]['Email'])

	#gender
	if people[0]['Gender'] == "Male":
		gender_xpath = '//*[@for="gender-radio-1"]'
	elif people[0]['Gender'] == "Female":
		gender_xpath = '//*[@for="gender-radio-2"]'
	else:
		gender_xpath = '//*[@for="gender-radio-3"]'
	gender = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, gender_xpath)))
	gender.click()

	#mobile number
	mobile_number = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userNumber"]')))
	mobile_number.send_keys(people[0]['Mobile Number'])

	#birthday
	birthday = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dateOfBirthInput"]')))
	birthday.send_keys(Keys.COMMAND, 'a')  # For macOS
	birthday.send_keys(people[0]['Date of Birth'])
	birthday.send_keys(Keys.RETURN)

	#subject
	subject = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="subjectsInput"]')))
	subject.send_keys(people[0]['Subject'])
	subject.send_keys(Keys.RETURN)

	#address
	address = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="currentAddress"]')))
	address.send_keys(people[0]['Address'])

	#hobby
	if people[0]['Hobbies'] == "Sports":
		hobby_xpath = '//*[@for="hobbies-checkbox-1"]'
	elif people[0]['Hobbies'] == "Reading":
		hobby_xpath = '//*[@for="hobbies-checkbox-2"]'
	else:
		hobby_xpath = '//*[@for="hobbies-checkbox-3"]'
	hobby = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, hobby_xpath)))
	hobby.click()

	#state
	state = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-3-input"]')))
	state.send_keys(people[0]['State'])
	state.send_keys(Keys.RETURN)

	#city
	city = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-4-input"]')))
	city.send_keys(people[0]['City'])
	city.send_keys(Keys.RETURN)

	#submit
	submit = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit"]')))
	submit.click()

	time.sleep(3)
	#close
	closing = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="closeLargeModal"]')))
	closing.click()

	# Optional: Wait to observe the result
	time.sleep(10)

finally:
	# Close the browser
	driver.quit()

