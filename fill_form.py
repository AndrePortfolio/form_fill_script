# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  ____   ____       ____     ___                 #
#                 / ___| / ___|     | ___|   / _ \                #
#                | |     \___ \     |___ \  | | | |               #
#                | |___   ___) |     ___) | | |_| |               #
#                 \____| |____/     |____/   \___/                #
#                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from	selenium.webdriver.support.ui import WebDriverWait
from	selenium.webdriver.common.by import By
from	selenium.webdriver.support import expected_conditions as EC
from	selenium.webdriver.common.keys import Keys
import	sys
import	time

def	first_name(driver, person):
	try:
		first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="firstName"]')))
		first_name.send_keys(person['Name'])
	except:
		pass

def	last_name(driver, person):
	try:
		last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lastName"]')))
		last_name.send_keys(person['Last Name'])
	except:
		pass

def	email(driver, person):
	try:
		email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
		email.send_keys(person['Email'])
	except:
		pass

def	gender(driver, person):
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

def	mobile_number(driver, person):
	try:
		mobile_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userNumber"]')))
		mobile_number.send_keys(person['Mobile Number'])
	except:
		pass

def	birthday(driver, person):
	try:
		birthday = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dateOfBirthInput"]')))
		birthday.send_keys(Keys.COMMAND, 'a')
		birthday.send_keys(person['Date of Birth'])
		birthday.send_keys(Keys.RETURN)
	except:
		pass

def	subject(driver, person):
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

def	address(driver, person):
	try:
		address = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="currentAddress"]')))
		address.send_keys(person['Address'])
	except:
		pass

def	hobby(driver, person):
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

def	state(driver, person):
	try:
		state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-3-input"]')))
		state.clear()
		state.send_keys(person['State'])
		state.send_keys(Keys.RETURN)
	except:
		driver.quit()
		sys.exit(1)

def	city(driver, person):
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
		time.sleep(1)
		closing = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="closeLargeModal"]')))
		closing.click()
	except:
		pass
