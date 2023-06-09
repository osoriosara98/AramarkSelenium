import time
from selenium.webdriver.common.by import By
from credentials import credentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    """
    Login with valid credentials
    """
    user, password = next(iter(credentials.items()))
    username_textbox = driver.find_element(By.ID, "email")
    password_textbox = driver.find_element(By.ID, "password")
    username_textbox.send_keys(user)
    password_textbox.send_keys(password)
    submit_button = driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
    submit_button.click()

def GetIntoEditAccount(driver):
    """
    Get into edit account page
    """
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "/html/body/app-root/portal-root/app-top-navigation/header/div/div/div/nav/ul/li/app-navigation-link/button")
        )
    )

    dropdown_button.click()
    menu_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, "mat-focus-indicator.mat-menu-item.ng-tns-c121-1.ng-star-inserted"))
    )

    if menu_items:
        first_menu_item = menu_items[0]
        first_menu_item.click()

    time.sleep(2)