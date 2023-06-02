import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from credentials import credentials
from random import random



class ForgotPasswordTests(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://myportallogindev.aramark.com/forgot-password"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        email_textbox = self.driver.find_element(By.ID, "email")
        email_textbox.send_keys("correo_valido@example.com")

        send_reset_password_button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        send_reset_password_button.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


    def test_AramarkLogoDisplayed(self):
        """
        Verify that the Aramark logo is displayed on the page
        """
        logo = self.driver.find_element(By.CLASS_NAME, "auth__logo")
        self.assertTrue(logo.is_displayed())

    def test_ConfirmationPageHeaderText(self):
        """
        Verify that the text "Your request has been sent" is displayed
        """
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".typography.h2")
        header_text = header_element.text
        self.assertIn("Your request has been sent", header_text)

    def test_ConfirmationPageMessageText(self):
        """
        Verify that the text "Please check your email for a link to reset your password" is displayed
        """
        message_element = self.driver.find_element(By.XPATH,
                                                   "/html/body/app-root/app-sign-in/div/main/div/app-forgot-password-form/div/aus-typography[2]/p")
        message_text = message_element.text
        self.assertEqual(message_text, "Please check your email for a link to reset your password.")


    def test_ConfirmationPageReturnToLoginLink(self):
        """
        Verify that there's a "Return to login" link on the confirmation page.
        """
        return_to_login_link = self.driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/div/main/div/app-forgot-password-form/div/div/a/aus-typography/p")
        self.assertTrue(return_to_login_link.is_displayed())

    def test_ConfirmationPageReturnToLoginRedirection(self):
        """
        Verify that clicking on the "Return to login" link on the confirmation page redirects the user to the login page.
        """
        return_to_login_link = self.driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/div/main/div/app-forgot-password-form/div/div/a/aus-typography/p")
        return_to_login_link.click()
        expected_url = "https://myportallogindev.aramark.com/login"
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url)
