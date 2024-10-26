# form_fill script
    Video Demo:  https://youtu.be/geFXT0NGGjU

## Overview
This project, named **form_fill script**, is designed to automate the process of filling out a specific online form, reducing manual input time and improving efficiency. Using **Python** and the **Selenium WebDriver** library, the project interacts with the form, enters required information, and submits it. This automation script can be adapted to work with various web forms by adjusting the input fields and selectors.

## Features
1. **Data Extraction**: Reads data from a CSV file where each row represents a person’s details, such as name, last name, email, and other relevant information.
2. **Form Interaction**: Utilizes Selenium to locate web elements, enter text, and simulate button clicks on a form, replicating human interaction.
3. **Error Handling**: Includes error handling mechanisms to manage unexpected issues, such as missing elements or incorrect data formats.
4. **Browser Management**: Automates browser management by initiating a session, performing tasks, and gracefully closing the browser once the form is submitted.

## Project Files
The main project files included in this automation project are:

- **`project.py`**: The primary script that orchestrates the workflow of reading data, launching the browser, and managing form interactions. This file imports functions from `fill_form.py` and `csv_reader.py` and leverages Selenium to automate the form-filling process.
- **`csv_reader.py`**: Contains a function to read data from a CSV file, transforming it into a list of dictionaries. Each dictionary represents a single person’s details to be used in form-filling.
- **`fill_form.py`**: This file includes individual functions for each form field, enabling modular handling of each input element. Functions like `first_name`, `last_name`, and `email` ensure each part of the form is correctly completed based on provided data.
- **`test_project.py`**: Contains unit tests for each function in `project.py`, `csv_reader.py`, and `fill_form.py`, ensuring that data is read, processed, and inputted accurately. Tests cover aspects like correct function calls, handling of invalid inputs, and expected behavior of form interactions.
- **`requirements.txt`**: Lists all dependencies required to run the project, including Selenium and other helper libraries. Users can install these packages using `pip install -r requirements.txt`.
- **`README.md`**: Documentation file explaining the project’s purpose, structure, and features.

## Design Choices
Some key design choices and their rationales include:

1. **Modularity**: By separating CSV reading and form-filling logic into distinct files (`csv_reader.py` and `fill_form.py`), the code remains organized and reusable. This approach also improves testability by allowing each file’s functions to be tested independently.
2. **Selenium for Automation**: Selenium was chosen for its reliability in web automation and its compatibility with various browsers. It enables precise control over browser actions and handles dynamic web elements effectively.
3. **Error Handling**: To ensure robustness, each function in `fill_form.py` includes exception handling to manage cases where elements may not be found or data formats are unexpected.
4. **Unit Testing**: Automated tests in `test_project.py` validate that each function performs as expected. Mocking and patching are used to simulate interactions with the web elements, making tests reliable and independent of the actual web environment.

## Installation & Usage

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd project-directory
   python project.py data.csv
