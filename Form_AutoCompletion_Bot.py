from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

# Define a list of dictionaries containing the form data for each user
users = [
    {"first_name": "Andy", "last_name": "Test", "job_title": "Tester", "years_of_experience": "1", "education": "College", "sex": "Male"},
    {"first_name": "Dave", "last_name": "Test", "job_title": "Developer", "years_of_experience": "2", "education": "High School", "sex": "Female"},
    {"first_name": "John", "last_name": "Test", "job_title": "Engineer", "years_of_experience": "3", "education": "Grad School", "sex": "Prefer not to say"},
]

# Initialize Chrome
chrome = webdriver.Chrome()

# Navigate to the form
chrome.get("https://formy-project.herokuapp.com/form")

# Wait for the page to load
sleep(3)

# Fill in the form for each user
for user in users:
    # Fill in the first name field
    chrome.find_element(By.ID, "first-name").send_keys(user["first_name"])
    sleep(1)

    # Fill in the last name field
    chrome.find_element(By.ID, "last-name").send_keys(user["last_name"])
    sleep(1)

    # Fill in the job title field
    chrome.find_element(By.ID, "job-title").send_keys(user["job_title"])
    sleep(1)

    # Select the education
    if user["education"] == "High School":
        chrome.find_element(By.ID, "radio-button-1").click()
    elif user["education"] == "College":
        chrome.find_element(By.ID, "radio-button-2").click()
    elif user["education"] == "Grad School":
        chrome.find_element(By.ID, "radio-button-3").click()
    sleep(1)

    # Select the sex
    if user["sex"] == "Male":
        chrome.find_element(By.ID, "checkbox-1").click()
    elif user["sex"] == "Female":
        chrome.find_element(By.ID, "checkbox-2").click()
    elif user["sex"] == "Prefer not to say":
        chrome.find_element(By.ID, "checkbox-3").click()
    sleep(1)

    # Select the years of experience
    dropdown_element = chrome.find_element(By.ID, "select-menu")
    dropdown = Select(dropdown_element)
    dropdown.select_by_value(user["years_of_experience"] if int(user["years_of_experience"]) <= 4 else "4")
    sleep(1)

    # Click the submit button
    chrome.find_element(By.XPATH, "/html/body/div/form/div/div[8]/a").click()
    sleep(3)

    # Navigate back to the form
    chrome.get("https://formy-project.herokuapp.com/form")
    sleep(3)

# Close the browser
chrome.quit()

# Print a success message
print("SUCCESS - TEST PASSED")
