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

    def tearDown(self):
        self.driver.quit()

    def test_AramarkLogoDisplayed(self):
        """
        Verify that the Aramark logo is displayed on the page
        """
        logo = self.driver.find_element(By.CLASS_NAME, "auth__logo")
        self.assertTrue(logo.is_displayed())

    def test_WelcomeBackTitle(self):
        """
        Verify that the "Forgot password" title is displayed
        """
        forgot_title = self.driver.find_element(By.CSS_SELECTOR, ".typography.h1.text-preset-2--medium")
        self.assertTrue(forgot_title.is_displayed())
        self.assertIn("Forgot password", forgot_title.text)

    def test_RequiredFieldText(self):
        """
        Verify that the '* indicates a required field' text is displayed
        """
        required_field_text = self.driver.find_element(By.XPATH,
                                                       "/html/body/app-root/app-sign-in/div/main/div/app-forgot-password-form/form/div[1]/div/aus-typography/p").text
        self.assertEqual(required_field_text, "* indicates a required field")

    def test_EmailLabelDisplayed(self):
        """
        Verify that the 'Email*' label is displayed
        """
        email_label = self.driver.find_element(By.XPATH,
                                               "/html/body/app-root/app-sign-in/div/main/div/app-forgot-password-form/form/div[1]/div/aus-input/fieldset/label/span/div/aus-typography/p")
        self.assertTrue(email_label.is_displayed())

    def test_EmailInputDisplayed(self):
        """
        Verify that the email input field is displayed
        """
        email_input = self.driver.find_element(By.ID, "email")
        self.assertTrue(email_input.is_displayed())

    def test_EmailInputPlaceholder(self):
        """
        Verify that the email input field has a placeholder text
        """
        email_input = self.driver.find_element(By.ID, "email")
        placeholder_text = email_input.get_attribute("placeholder")
        expected_placeholder = "first.last@aramark.com"
        self.assertEqual(placeholder_text, expected_placeholder)

    def test_SendResetPasswordButtonDisabled(self):
        """
        Verify that the 'Send reset password link' button is disabled until a valid email address is entered
        """
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@")
        reset_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Send reset password link')]")
        self.assertFalse(reset_button.is_enabled())

    def test_SendResetPasswordButtonEnabled(self):
        """
        Verify that the 'Send reset password link' button is enabled when a valid email address is entered
        """
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("valid_email@example.com")
        reset_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Send reset password link')]")
        self.assertTrue(reset_button.is_enabled())

    def test_ReturnToLoginRedirect(self):
        """
        Verify that clicking on the 'Return to login' link redirects the user to the login page
        """
        return_to_login_link = self.driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/div/main/div/app-forgot-password-form/form/div[2]/a/aus-typography/p")
        return_to_login_link.click()
        time.sleep(5)
        expected_url = "https://myportallogindev.aramark.com/login"
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url)

    import time

    def test_SendResetPasswordRedirect(self):
        """
        Verify that clicking on the 'Send reset password link' button redirects the user to a confirmation page
        """
        email_textbox = self.driver.find_element(By.ID, "email")
        email_textbox.send_keys("correo_valido@example.com")

        send_reset_password_button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        send_reset_password_button.click()

        # Esperar 2 segundos para que se cargue la página de confirmación
        time.sleep(2)

        # Verificar que el texto de confirmación esté presente en la página
        confirmation_text = "Your request has been sent."
        confirmation_element = self.driver.find_element(By.XPATH,
                                                        "//*[contains(text(), '{0}')]".format(confirmation_text))
        self.assertTrue(confirmation_element.is_displayed())
