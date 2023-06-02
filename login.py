import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from credentials import credentials
from random import random



class LoginPageTests(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://myportallogindev.aramark.com/login"
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
        Verify that the "Welcome back!" title is displayed
        """
        welcome_title = self.driver.find_element(By.CSS_SELECTOR, ".typography.h1.text-preset-2--medium")
        self.assertTrue(welcome_title.is_displayed())
        self.assertIn("Welcome back!", welcome_title.text)


    def test_AuthBannerDisplayed(self):
        """
        Verify that the Auth banner is displayed
        """
        auth_banner = self.driver.find_element(By.CLASS_NAME, "auth__banner")
        self.assertTrue(auth_banner.is_displayed())

    def test_RequiredFieldParagraph(self):
        """
        Verify that the page contains a paragraph that says "* indicates a required field"
        """
        required_field_paragraph = self.driver.find_element(By.CSS_SELECTOR, ".typography.p.text-preset-7")
        self.assertTrue(required_field_paragraph.is_displayed())
        self.assertIn("* indicates a required field", required_field_paragraph.text)

    def test_EmailTitleVisible(self):
        """
        Verify that the email title is visible
        """
        email_title = self.driver.find_element(By.CSS_SELECTOR,"[data-testid='email'] > .input > label > .input__label > .input__label-main > :nth-child(1) > .typography")
        self.assertTrue(email_title.is_displayed())


    def test_EmailTextbox(self):
        """
        Verify that there is a textbox to enter the email.
        """
        email_textbox = self.driver.find_element(By.ID, "email")
        self.assertTrue(email_textbox.is_displayed())

        # Enter a value into the email textbox
        email_textbox.send_keys("example@test.com")

    def test_InvalidEmailErrorMessage(self):
        """
         Verify that if an invalid email is entered, an error message should appear
        """
        email_textbox = self.driver.find_element(By.ID, "email")
        email_textbox.send_keys('correo_no_valido@')
        email_textbox.send_keys(Keys.TAB)  # Agrega un tab al otro campo
        time.sleep(2)
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".form__control-msg > .typography")
        self.assertTrue(error_message.is_displayed())
        self.assertIn("This field should be a valid email", error_message.text)

    def test_BlankEmailErrorMessage(self):
        """
        Verify that when you leave the email textbox blank, you receive an error message
        """
        email_textbox = self.driver.find_element(By.ID, "email")
        email_textbox.send_keys('correo_no_valido@example.com')

        # Delete characters one by one until the field is empty
        while email_textbox.get_attribute("value"):
            email_textbox.send_keys(Keys.BACKSPACE)

        # Wait for the error message element to become visible
        wait = WebDriverWait(self.driver, 10)
        error_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".form__control-msg > .typography")))

        self.assertTrue(error_message.is_displayed())
        self.assertIn("Field cannot be left blank", error_message.text)

    def test_BlankPasswordErrorMessage(self):
        """
        Verify that when you leave the password textbox blank, you receive an error message
        """
        password_textbox = self.driver.find_element(By.ID, "password")
        password_textbox.send_keys('password123')
        while password_textbox.get_attribute("value"):
            password_textbox.send_keys(Keys.BACKSPACE)
        wait = WebDriverWait(self.driver, 10)
        error_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".form__control-msg > .typography")))

        self.assertTrue(error_message.is_displayed())
        self.assertIn("Field cannot be left blank", error_message.text)

    def test_PasswordRequiredField(self):
        """
        Verify that label Password is displayed
        """
        password_label = self.driver.find_element(By.XPATH,
                                                  "/html/body/app-root/app-sign-in/div/main/div/app-login-form/form/div[1]/div[2]/aus-input/fieldset/label/span/div/aus-typography/p")
        self.assertTrue(password_label.is_displayed())
        self.assertEqual(password_label.text, "Password")

    def test_PasswordInputExists(self):
        """
        Verify that the input field with ID "password" exists
        """
        password_input = self.driver.find_element(By.ID, "password")
        self.assertTrue(password_input.is_displayed())

    def test_ForgotPasswordLinkExists(self):
        """
        Verify that there is a hyperlink with the class "link__label text-preset-9--underline text-preset-7--medium"
        """
        forgot_password_link = self.driver.find_element(By.CSS_SELECTOR,
                                                        ".link__label.text-preset-9--underline.text-preset-7--medium")
        self.assertTrue(forgot_password_link.is_displayed())

    def test_RememberMeCheckboxExists(self):
        """
        Verify that there is a checkbox with the ID "rememberme" and it is selectable
        """
        remember_me_checkbox = self.driver.find_element(By.ID, "rememberme")
        self.assertTrue(remember_me_checkbox.is_displayed())
        self.assertTrue(remember_me_checkbox.is_enabled())

    def test_RememberMeTextDisplayed(self):
        """
        Verify that the text "Remember me" is displayed
        """
        remember_me_text = self.driver.find_element(By.XPATH,
                                                    "/html/body/app-root/app-sign-in/div/main/div/app-login-form/form/div[1]/div[3]/aus-checkbox/div/label/aus-typography/p")
        self.assertTrue(remember_me_text.is_displayed())
        self.assertEqual(remember_me_text.text, "Remember me")

    def test_LoginButtonExists(self):
        """
        Verify that the button "Log in" exists
        """
        login_button = self.driver.find_element(By.CLASS_NAME,
                                                "button.button--bg-red.button--fullwidth.button--size-large")
        self.assertTrue(login_button.is_displayed())

    def test_LoginButtonDisabledWithoutEmail(self):
        """
        Verify that the "Log in" button is disabled when the email hasn't been entered
        """
        password_textbox = self.driver.find_element(By.ID, "password")
        password_textbox.send_keys("password123")
        button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        is_disabled = button.get_attribute('disabled') == 'true'

        # Verificar que el botón está deshabilitado
        self.assertTrue(is_disabled)

    def test_LoginButtonDisabledWithanInvalidEmail(self):
        """
        Verify that the 'Log in' button is disabled when the email hasn't been entered
        """
        # Ingresar un correo electrónico inválido
        email_textbox = self.driver.find_element(By.ID, "email")
        email_textbox.send_keys("correo_no_valido@")
        password_textbox = self.driver.find_element(By.ID, "password")
        password_textbox.send_keys("password123")
        button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        is_disabled = button.get_attribute('disabled') == 'true'
        self.assertTrue(is_disabled)

    def test_LoginButtonDisabledWithoutPassword(self):
        """
        Verify that the "Log in" button is disabled when the email hasn't been entered
        """
        password_textbox = self.driver.find_element(By.ID, "email")
        password_textbox.send_keys("validemail@example.com")
        button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        is_disabled = button.get_attribute('disabled') == 'true'

    def test_VerifyTextOnPage(self):
        """
        Verify that the page contains the text "Not set up yet?"
        """

        text_element = self.driver.find_element(By.XPATH,
                                                "/html/body/app-root/app-sign-in/div/main/div/app-login-form/form/div[2]/aus-typography/p")
        self.assertTrue(text_element.is_displayed())

    def test_VerifyCreateAccountButton(self):
        """
        Verify that the "Create an account" button exists
        """
        button_element = self.driver.find_element(By.XPATH,
                                                  "/html/body/app-root/app-sign-in/div/main/div/app-login-form/form/div[2]/a/aus-typography/p")
        self.assertTrue(button_element.is_displayed())

    def test_CreateAccountButtonRedirect(self):
        """
        Verify that the "Create an account" button takes the user to the self-registration page
        """
        button_element = self.driver.find_element(By.XPATH,
                                                  "/html/body/app-root/app-sign-in/div/main/div/app-login-form/form/div[2]/a/aus-typography/p")
        button_element.click()
        current_url = self.driver.current_url
        expected_url = "https://myportallogindev.aramark.com/self-registration"
        self.assertEqual(current_url, expected_url)

    def test_InvalidCredentialsAlert(self):
        """
        Verify that if invalid credentials are entered, an alert with the appropriate text is displayed
        """
        # Enter invalid credentials (username and password)
        username_textbox = self.driver.find_element(By.ID, "email")
        password_textbox = self.driver.find_element(By.ID, "password")
        username_textbox.send_keys("invalidemail@example.com")
        password_textbox.send_keys("invalid_password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        submit_button.click()
        time.sleep(2)
        alert_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-login-form/form/aus-alerts/div/div/aus-alert/div/div/div[2]/aus-typography[2]/p")
        expected_text = "You entered an incorrect user name or password."
        self.assertEqual(alert_element.text, expected_text)

    def test_ValidLoginRedirect(self):
        """
        Verify that a login with valid credentials redirects the user to the home page
        """
        user, password = next(iter(credentials.items()))
        username_textbox = self.driver.find_element(By.ID, "email")
        password_textbox = self.driver.find_element(By.ID, "password")
        username_textbox.send_keys(user)
        password_textbox.send_keys(password)
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'aus-button[btntype="submit"] button')
        submit_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-home/p')))
        home_element = self.driver.find_element(By.XPATH,
                                                '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-home/p')
        self.assertEqual(home_element.text, 'home works!')

    def test_ForgotPasswordRedirect(self):
        """
        Verify that clicking on "Forgot password?" redirects the user to the password reset page
        """
        forgot_password_link = self.driver.find_element(By.LINK_TEXT, "Forgot password?")
        forgot_password_link.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://myportallogindev.aramark.com/forgot-password"))
        current_url = self.driver.current_url
        self.assertIn("https://myportallogindev.aramark.com/forgot-password", current_url)

    def test_ShowPasswordOnClick(self):
        """
        Verify that clicking on the button in the password input reveals the entered password
        """
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("password123")
        show_password_button = self.driver.find_element(By.CLASS_NAME,
                                                        "input__visibility-toggle")
        show_password_button.click()
        password_value = password_input.get_attribute("value")
        self.assertEqual(password_value, "password123")


if __name__ == "__main__":
    unittest.main()
