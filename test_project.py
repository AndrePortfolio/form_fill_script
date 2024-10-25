# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  ____   ____       ____     ___                 #
#                 / ___| / ___|     | ___|   / _ \                #
#                | |     \___ \     |___ \  | | | |               #
#                | |___   ___) |     ___) | | |_| |               #
#                 \____| |____/     |____/   \___/                #
#                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import	pytest
from	unittest.mock import patch, MagicMock
from	selenium.webdriver.common.keys import Keys
from	project import get_people_from_csv, init_driver, accept_cookies, search_bar, fill_form_params

@pytest.fixture
def temporary_csv_file(tmpdir):
	csv_content = "Name,Last Name,Email\nJohn,Doe,john.doe@example.com\n"
	tmp_file = tmpdir.join("test.csv")
	tmp_file.write(csv_content)
	return str(tmp_file)


# Tests if the get_people_from_csv function extracts the correct data from the CSV file.
@patch('project.get_people_from_csv')
def test_get_people_from_csv(mock_get_people, temporary_csv_file):
	mock_get_people.return_value = [{'Name': 'John', 'Last Name': 'Doe', 'Email': 'john.doe@example.com'}]

	people = get_people_from_csv(temporary_csv_file)
	expected_data = [{'Name': 'John', 'Last Name': 'Doe', 'Email': 'john.doe@example.com'}]
	assert people == expected_data


# Tests if the init_driver function correctly initializes the WebDriver.
@patch('project.webdriver.Chrome')
def test_init_driver(mock_chrome):
	driver = init_driver()
	mock_chrome.assert_called_once()
	assert driver


# Tests if the accept_cookies function clicks the accept button correctly.
@patch('project.WebDriverWait')
def test_accept_cookies(mock_wait):
	mock_driver = MagicMock()
	mock_accept_button = MagicMock()
	mock_wait.return_value.until.return_value = mock_accept_button

	accept_cookies(mock_driver)
	mock_accept_button.click.assert_called_once()


# Tests if the search_bar function sends the correct search query to the search bar.
@patch('project.WebDriverWait')
def test_search_bar(mock_wait):
	mock_driver = MagicMock()
	mock_search_bar = MagicMock()
	mock_wait.return_value.until.return_value = mock_search_bar

	search_bar(mock_driver)
	mock_search_bar.send_keys.assert_any_call('Practice Form on Automation')
	mock_search_bar.send_keys.assert_any_call(Keys.RETURN)


# Tests if the fill_form_params function passes the correct parameters to the fill_form functions.
@patch('project.fill_form')
def test_fill_form_params(mock_fill_form):
	mock_driver = MagicMock()
	person_data = {'Name': 'John', 'Last Name': 'Doe', 'Email': 'john.doe@example.com'}

	fill_form_params(mock_driver, person_data)

	mock_fill_form.first_name.assert_called_with(mock_driver, person_data)
	mock_fill_form.last_name.assert_called_with(mock_driver, person_data)
	mock_fill_form.email.assert_called_with(mock_driver, person_data)
	mock_fill_form.gender.assert_called_with(mock_driver, person_data)
	mock_fill_form.mobile_number.assert_called_with(mock_driver, person_data)
	mock_fill_form.birthday.assert_called_with(mock_driver, person_data)
	mock_fill_form.subject.assert_called_with(mock_driver, person_data)
	mock_fill_form.address.assert_called_with(mock_driver, person_data)
	mock_fill_form.hobby.assert_called_with(mock_driver, person_data)
	mock_fill_form.state.assert_called_with(mock_driver, person_data)
	mock_fill_form.city.assert_called_with(mock_driver, person_data)
	mock_fill_form.submit.assert_called_with(mock_driver)
	mock_fill_form.close.assert_called_with(mock_driver)



