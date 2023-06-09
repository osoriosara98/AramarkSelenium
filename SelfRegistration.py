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
        self.base_url = "https://myportallogindev.aramark.com/self-registration"
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

    def test_RegistrationPageTitle(self):
        """
        Verify that the title "Let's Get Started" is displayed on the registration page
        """

        title_element = self.driver.find_element(By.CSS_SELECTOR, ".typography.h1.text-preset-2--medium")
        title_text = title_element.text
        self.assertEqual("Let's get started", title_text)

    def test_RequiredFieldParagraph(self):
        """
        Verify that the paragraph "* Indicates a Required Field" is displayed on the registration page
        """
        paragraph_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[1]/aus-typography/p")
        paragraph_text = paragraph_element.text
        self.assertEqual("* indicates a required field", paragraph_text)

    def test_FirstNameLabel(self):
        label_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[1]/aus-input/fieldset/label/span/div/aus-typography/p")
        label_text = label_element.text
        self.assertEqual("First Name", label_text)

    def test_LastNameLabel(self):
        label_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[2]/aus-input/fieldset/label/span/div/aus-typography/p")
        label_text = label_element.text
        self.assertEqual("Last Name", label_text)

    def test_PhoneNumberLabel(self):
        label_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[3]/aus-input/fieldset/label/span/div/aus-typography/p")
        label_text = label_element.text
        self.assertEqual("Phone Number", label_text)

    def test_EmailLabel(self):
        label_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[4]/aus-input/fieldset/label/span/div/aus-typography/p")
        label_text = label_element.text
        self.assertEqual("Email", label_text)

    def test_AccountNumberLabel(self):
        label_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[5]/aus-input/fieldset/label/span/div/aus-typography/p")
        label_text = label_element.text
        self.assertEqual("Account #", label_text)

    def test_BillingZipCodeLabel(self):
        label_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/div[6]/aus-input/fieldset/label/span/div/aus-typography/p")
        label_text = label_element.text
        self.assertEqual("Billing Zip Code", label_text)

    def test_FirstNameInputDisplayed(self):
        """
        Verify that the 'firstName' input field is displayed on the registration page
        """
        input_element = self.driver.find_element(By.ID, 'firstName')
        self.assertTrue(input_element.is_displayed(), "The 'firstName' input field is not displayed")

    def test_LastNameInputDisplayed(self):
        """
        Verify that the 'lastName' input field is displayed on the registration page
        """
        input_element = self.driver.find_element(By.ID, 'lastName')
        self.assertTrue(input_element.is_displayed(), "The 'lastName' input field is not displayed")

    def test_PhoneNumberInputDisplayed(self):
        """
        Verify that the 'phoneNumber' input field is displayed on the registration page
        """
        input_element = self.driver.find_element(By.ID, 'phoneNumber')
        self.assertTrue(input_element.is_displayed(), "The 'phoneNumber' input field is not displayed")

    def test_EmailInputDisplayed(self):
        """
        Verify that the 'email' input field is displayed on the registration page
        """
        input_element = self.driver.find_element(By.ID, 'email')
        self.assertTrue(input_element.is_displayed(), "The 'email' input field is not displayed")

    def test_AccountNumberInputDisplayed(self):
        """
        Verify that the 'accountNumber' input field is displayed on the registration page
        """
        input_element = self.driver.find_element(By.ID, 'accountNumber')
        self.assertTrue(input_element.is_displayed(), "The 'accountNumber' input field is not displayed")

    def test_AccountBillingPostalCodeInputDisplayed(self):
        """
        Verify that the 'accountBillingPostalCode' input field is displayed on the registration page
        """
        input_element = self.driver.find_element(By.ID, 'accountBillingPostalCode')
        self.assertTrue(input_element.is_displayed(), "The 'accountBillingPostalCode' input field is not displayed")

    def test_CreateAccountButtonDisabledWithMissingInfo(self):
        """
        Verify that the 'Create account' button is disabled with missing information in required fields
        """
        # Leave one or more required fields empty
        first_name_input = self.driver.find_element(By.ID, 'firstName')
        first_name_input.send_keys('John')

        email_input = self.driver.find_element(By.ID, 'email')
        email_input.send_keys('johndoe@example.com')

        billing_zip_code_input = self.driver.find_element(By.ID, 'accountBillingPostalCode')
        billing_zip_code_input.send_keys('12345')

        create_account_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/aus-button/button')
        self.assertFalse(create_account_button.is_enabled(),
                         "The 'Create account' button is enabled with missing information in required fields")

    def test_AlreadyHaveAccountTextDisplayed(self):
        """
        Verify that the text "Already have an account?" is displayed on the registration page
        """
        text_element = self.driver.find_element(By.XPATH,
                                                "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[2]/aus-typography/p")
        text = text_element.text
        self.assertEqual("Already have an account?", text,
                         "The text 'Already have an account?' is not displayed on the registration page")

    def test_LoginLinkRedirectsToLoginPage(self):
        """
        Verify that the 'Log In' link redirects to the login page
        """
        login_link = self.driver.find_element(By.XPATH,
                                              "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[2]/a/aus-typography/p")
        login_link.click()
        current_url = self.driver.current_url
        self.assertEqual("https://myportallogindev.aramark.com/login", current_url,
                         "Clicking the 'Log In' link did not redirect to the login page")

    def test_FirstNameInputDisplayedAndValidation(self):
        """
        Verify that the 'firstName' input field is displayed on the registration page and validate its input
        """
        input_element = self.driver.find_element(By.ID, 'firstName')
        self.assertTrue(input_element.is_displayed(), "The 'firstName' input field is not displayed")

        input_element.send_keys("123")
        self.driver.find_element(By.ID, 'lastName').click()  # Click on another field

        error_element = self.driver.find_element(By.XPATH,
                                                 "//input[@id='firstName']/following-sibling::span[contains(@class, 'error-message')]")
        self.assertEqual("This field should be a valid name", error_element.text)

    def test_LastNameInputDisplayedAndValidation(self):
        """
        Verify that the 'lastName' input field is displayed on the registration page and validate its input
        """
        input_element = self.driver.find_element(By.ID, 'lastName')
        self.assertTrue(input_element.is_displayed(), "The 'lastName' input field is not displayed")

        input_element.send_keys("!")
        self.driver.find_element(By.ID, 'phoneNumber').click()  # Click on another field

        error_element = self.driver.find_element(By.XPATH,
                                                 "//input[@id='lastName']/following-sibling::span[contains(@class, 'error-message')]")
        self.assertEqual("This field should be a valid name", error_element.text)

    def test_PhoneNumberInputDisplayedAndValidation(self):
        """
        Verify that the 'phoneNumber' input field is displayed on the registration page and validate its input
        """
        input_element = self.driver.find_element(By.ID, 'phoneNumber')
        self.assertTrue(input_element.is_displayed(), "The 'phoneNumber' input field is not displayed")

        input_element.send_keys("abc")
        self.driver.find_element(By.ID, 'email').click()  # Click on another field

        error_element = self.driver.find_element(By.XPATH,
                                                 "//input[@id='phoneNumber']/following-sibling::span[contains(@class, 'error-message')]")
        self.assertEqual("This field should be a valid phone number", error_element.text)

    def test_EmailInputDisplayedAndValidation(self):
        """
        Verify that the 'email' input field is displayed on the registration page and validate its input
        """
        input_element = self.driver.find_element(By.ID, 'email')
        self.assertTrue(input_element.is_displayed(), "The 'email' input field is not displayed")

        input_element.send_keys("invalidemail")
        self.driver.find_element(By.ID, 'accountNumber').click()  # Click on another field

        error_element = self.driver.find_element(By.XPATH,
                                                 "//input[@id='email']/following-sibling::span[contains(@class, 'error-message')]")
        self.assertEqual("This field should be a valid email", error_element.text)

    def test_AccountNumberInputDisplayedAndValidation(self):
        """
        Verify that the 'accountNumber' input field is displayed on the registration page and validate its input
        """
        input_element = self.driver.find_element(By.ID, 'accountNumber')
        self.assertTrue(input_element.is_displayed(), "The 'accountNumber' input field is not displayed")

        input_element.send_keys("!123")
        self.driver.find_element(By.ID, 'accountBillingPostalCode').click()  # Click on another field

        error_element = self.driver.find_element(By.XPATH,
                                                 "//input[@id='accountNumber']/following-sibling::span[contains(@class, 'error-message')]")
        self.assertEqual("This field should be a valid account number", error_element.text)

    def test_AccountBillingPostalCodeInputDisplayedAndValidation(self):
        """
        Verify that the 'accountBillingPostalCode' input field is displayed on the registration page and validate its input
        """
        input_element = self.driver.find_element(By.ID, 'accountBillingPostalCode')
        self.assertTrue(input_element.is_displayed(), "The 'accountBillingPostalCode' input field is not displayed")

        input_element.send_keys("abc")
        self.driver.find_element(By.XPATH, "//body").click()  # Click on another field

        error_element = self.driver.find_element(By.XPATH,
                                                 "//input[@id='accountBillingPostalCode']/following-sibling::span[contains(@class, 'error-message')]")
        self.assertEqual("This field should be a valid zip code", error_element.text)

    def test_CreateAccountButtonEnabled(self):
        """
        Verify that the 'Create Account' button is enabled when all required fields are filled
        """
        # Enter valid information into the input fields
        self.driver.find_element(By.ID, 'firstName').send_keys("John")
        self.driver.find_element(By.ID, 'lastName').send_keys("Doe")
        self.driver.find_element(By.ID, 'phoneNumber').send_keys("1234567890")
        self.driver.find_element(By.ID, 'email').send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, 'accountNumber').send_keys("A123456")
        self.driver.find_element(By.ID, 'accountBillingPostalCode').send_keys("12345")

        # Verify that the 'Create Account' button is enabled
        create_account_button = self.driver.find_element(By.XPATH, "//button[text()='Create Account']")
        self.assertTrue(create_account_button.is_enabled(), "The 'Create Account' button is not enabled")

    def test_AccountCreation(self):
        """
        Verify User can create an account
        """
        self.driver.find_element(By.ID, 'firstName').send_keys("John")
        self.driver.find_element(By.ID, 'lastName').send_keys("Doe")
        self.driver.find_element(By.ID, 'phoneNumber').send_keys("1234567890")
        self.driver.find_element(By.ID, 'email').send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, 'accountNumber').send_keys("N9264025290")
        self.driver.find_element(By.ID, 'accountBillingPostalCode').send_keys("12345")

        create_account_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/div/main/div/app-self-registration/form/div[1]/aus-button/button")
        create_account_button.click()

        time.sleep(2)
        current_url = self.driver.current_url

        expected_url = "https://example.com/confirmation"  # Replace with the expected URL
        self.assertEqual(expected_url, current_url, "The user is not redirected to the appropriate page")




