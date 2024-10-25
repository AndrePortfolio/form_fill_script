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

def	get_people_from_csv():
	if len(sys.argv) != 2:
		sys.exit("Usage: python your_script.py <path_to_csv>")
	csv_file_path = sys.argv[1]
	people = []
	# Read the CSV file
	with open(csv_file_path, mode='r') as file:
		csv_reader = csv.DictReader(file)
		for row in csv_reader:
			people.append(row)
	return people

def	init_driver():
	# Initialize WebDriver
	driver = webdriver.Chrome()

	# Open Google
	driver.get('https://www.google.pt/?hl=pt-PT')
	driver.maximize_window()
	return driver

def	accept_cookies(driver):
	try:
		# Wait for the consent pop-up and click "Accept All"
		accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Aceitar tudo"]')))
		accept_button.click()
	except:
		pass

def	search_bar(driver):
	try:
		# Wait for the Google search bar to load
		search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

		search_bar.send_keys('Practice Form on Automation')
		search_bar.send_keys(Keys.RETURN)

		# Wait for search results to load
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search')))

		# Find and click the first result link
		site = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Practice Form"]')))
		site.click()
	except:
		pass

def	fill_first_name(driver, person):
	try:
		first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="firstName"]')))
		first_name.send_keys(person['Name'])
	except:
		pass

def	fill_last_name(driver, person):
	try:
		last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lastName"]')))
		last_name.send_keys(person['Last Name'])
	except:
		pass

def	fill_email(driver, person):
	try:
		email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
		email.send_keys(person['Email'])
	except:
		pass

def	fill_gender(driver, person):
	try:
		if person['Gender'] == "Male":
			gender_xpath = '//*[@for="gender-radio-1"]'
		elif person['Gender'] == "Female":
			gender_xpath = '//*[@for="gender-radio-2"]'
		else:
			gender_xpath = '//*[@for="gender-radio-3"]'
		gender = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, gender_xpath)))
		gender.click()
	except:
		pass

def	fill_mobile_number(driver, person):
	try:
		mobile_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userNumber"]')))
		mobile_number.send_keys(person['Mobile Number'])
	except:
		pass

def	fill_birthday(driver, person):
	try:
		birthday = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dateOfBirthInput"]')))
		birthday.send_keys(Keys.COMMAND, 'a')  # For macOS
		birthday.send_keys(person['Date of Birth'])
		birthday.send_keys(Keys.RETURN)
	except:
		pass

def	fill_subject(driver, person):
	valid_subjects = [
		'Maths', 'Accounting', 'Arts', 'Social Studies', 'Biology',
		'Physics', 'Chemisty', 'Computer Science', 'Commerce',
		'Economics', 'Civics', 'Hindi', 'English', 'History'
	]
	try:
		subject = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="subjectsInput"]')))
		subject.send_keys(person['Subject'])
		subject.send_keys(Keys.RETURN)
	except:
		pass

def	fill_address(driver, person):
	try:
		address = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="currentAddress"]')))
		address.send_keys(person['Address'])
	except:
		pass

def	fill_hobby(driver, person):
	try:
		if person['Hobbies'] == "Sports":
			hobby_xpath = '//*[@for="hobbies-checkbox-1"]'
		elif person['Hobbies'] == "Reading":
			hobby_xpath = '//*[@for="hobbies-checkbox-2"]'
		else:
			hobby_xpath = '//*[@for="hobbies-checkbox-3"]'
		hobby = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, hobby_xpath)))
		hobby.click()
	except:
		pass

def	fill_state(driver, person):
	try:
		state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-3-input"]')))
		state.clear()
		state.send_keys(person['State'])
		state.send_keys(Keys.RETURN)
	except:
		driver.quit()
		sys.exit(1)

def	fill_city(driver, person):
	valid_cities = {
		'NCR': ['Delhi', 'Gurgaon', 'Noida'],
		'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
		'Haryana': ['Karnal', 'Panipat'],
		'Rajasthan': ['Jaipur', 'Jaiselmer']
	}
	try:
		city = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-4-input"]')))
		city.clear()
		city.send_keys(person['City'])
		city.send_keys(Keys.RETURN)
	except:
		driver.quit()
		sys.exit(1)

def	submit(driver):
	try:
		submit = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit"]')))
		driver.execute_script("arguments[0].scrollIntoView(true);", submit)
		submit.click()
	except:
		pass

def	close(driver):
	try:
		time.sleep(2)
		closing = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="closeLargeModal"]')))
		closing.click()
	except:
		pass

def	fill_form(driver, person):
	try:
		fill_first_name(driver, person)
		fill_last_name(driver, person)
		fill_email(driver, person)
		fill_gender(driver, person)
		fill_mobile_number(driver, person)
		fill_birthday(driver, person)
		fill_subject(driver, person)
		fill_address(driver, person)
		fill_hobby(driver, person)
		fill_state(driver, person)
		fill_city(driver, person)
		submit(driver)
		close(driver)
		time.sleep(3)
	except:
		driver.quit()


def	main():
	people = get_people_from_csv()
	driver = init_driver()
	accept_cookies(driver)
	search_bar(driver)
	try:
		for person in people:
			fill_form(driver, person)
	finally:
		driver.quit()

if __name__ in "__main__":
	main()
