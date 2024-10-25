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
from	csv_reader import get_people_from_csv
import	fill_form

def	main():
	people = get_people_from_csv()
	driver = init_driver()
	accept_cookies(driver)
	search_bar(driver)
	try:
		i = 1
		for person in people:
			print(f"Person number {i} ({person['Name']}), form being filled...")
			fill_form_params(driver, person)
			print("Success.")
			i += 1
	finally:
		print("All forms filled.\nExit ...")
		driver.quit()

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

def	fill_form_params(driver, person):
	try:
		fill_form.first_name(driver, person)
		fill_form.last_name(driver, person)
		fill_form.email(driver, person)
		fill_form.gender(driver, person)
		fill_form.mobile_number(driver, person)
		fill_form.birthday(driver, person)
		fill_form.subject(driver, person)
		fill_form.address(driver, person)
		fill_form.hobby(driver, person)
		fill_form.state(driver, person)
		fill_form.city(driver, person)
		fill_form.submit(driver)
		fill_form.close(driver)
		driver.refresh()
		time.sleep(1)
	except:
		driver.quit()

if __name__ in "__main__":
	main()
