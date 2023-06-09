import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from credentials import credentials
from commands import login
from commands import GetIntoEditAccount



class EditAccountPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://myportallogindev.aramark.com/login"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login(self.driver)
        GetIntoEditAccount(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_AramarkLogoDisplayed(self):
        """
        Verify that the Aramark logo is displayed on the page
        """
        logo = self.driver.find_element(By.CLASS_NAME, "top-navigation__logo-img")
        self.assertTrue(logo.is_displayed())

    def test_DropdownExists(self):
        """
        Verify that there is a dropdown on the right side
        """
        dropdown = self.driver.find_element(By.XPATH,
                                            "/html/body/app-root/portal-root/app-top-navigation/header/div/div/div/nav/ul/li/app-navigation-link/button/div[1]")
        self.assertTrue(dropdown.is_displayed())

    def test_DropdownOptions(self):
        """
        Verify that the dropdown options are "My account" and "Logout"
        """
        dropdown_button = self.driver.find_element(By.XPATH,
                                                   "/html/body/app-root/portal-root/app-top-navigation/header/div/div/div/nav/ul/li/app-navigation-link/button/div[1]")
        dropdown_button.click()
        time.sleep(2)

        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//*[@id="cdk-overlay-0"]')
            )
        )

        option_texts = [option.text for option in options]

        self.assertIn("My Account\nManage Users\nLog Out", option_texts)


    def test_ClickLogoutRedirectsToLoginPage(self):
        """
        Verify that clicking on "Logout" redirects to the page: https://myportallogindev.aramark.com/login
        """
        dropdown_button = self.driver.find_element(By.XPATH,
                                                   "/html/body/app-root/portal-root/app-top-navigation/header/div/div/div/nav/ul/li/app-navigation-link/button/div[1]")
        dropdown_button.click()
        time.sleep(2)

        logout_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='mat-menu-panel-0']/div/a[3]/app-navigation-link/button")
            )
        )
        logout_button.click()

        self.assertEqual(self.driver.current_url, "https://myportallogindev.aramark.com/login")

    def test_BackLinkExists(self):
        """
        Verify that there is a link with the text "Back to customer portal."
        """
        back_link = self.driver.find_element(By.XPATH, "/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-my-account/app-page-layout/header/aus-typography/a/span")
        self.assertTrue(back_link.is_displayed() and back_link.text == "Back to Customer Portal")

    def test_BackLinkRedirects(self):
        """
        Verify that clicking on the "Back to customer portal" link redirects to the previous page's link.
        """
        back_link = self.driver.find_element(By.XPATH, "/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-my-account/app-page-layout/header/aus-typography/a/span")
        back_link.click()
        time.sleep(2)
        previous_url = "https://myportalaccountdev.aramark.com/"
        self.assertEqual(self.driver.current_url, previous_url)

    def test_TitleDisplayed(self):
        """
        Verify that a title "My account" is displayed.
        """
        title = self.driver.find_element(By.XPATH, "/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-my-account/app-page-layout/header/app-heading/div/div[1]/aus-typography/p")
        self.assertTrue(title.is_displayed() and title.text == "My Account")

    def test_SidebarNavigationExists(self):
        """
        Verifica que existe una barra de navegación lateral
        """
        sidebar_nav = self.driver.find_element(By.XPATH, "/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav/div/aside/app-sidenav/nav/ul")
        self.assertTrue(sidebar_nav.is_displayed())

    def test_SidebarNavigationOptions(self):
        """
        Verify the options in the side navigation menu.
        """
        sidebar_nav = self.driver.find_element(By.CSS_SELECTOR, ".sidenav.sidenav--account")
        options = sidebar_nav.find_elements(By.TAG_NAME, "a")
        option_hrefs = [option.get_attribute("href") for option in options]
        expected_hrefs = ['https://myportalaccountdev.aramark.com/account',
                          'https://myportalaccountdev.aramark.com/account/change-password']
        for href in expected_hrefs:
            self.assertIn(href, option_hrefs)

    def test_BackToCustomerPortalLink(self):
        """
        Verify that clicking on the "Back to customer portal" link redirects to the previous page.
        """
        link = self.driver.find_element(By.XPATH,
                                        '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-my-account/app-page-layout/header/aus-typography/a')
        link.click()

        expected_url = "https://myportalaccountdev.aramark.com/"
        self.assertIn(expected_url, self.driver.current_url)

    def test_MyAccountTitleDisplayed(self):
        """
        Verify that the title "My account" is displayed.
        """
        title = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-my-account/app-page-layout/header/app-heading/div/div[1]/aus-typography/p')
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, "My account")

    def test_SideNavigationExists(self):
        """
        Verify that a side navigation bar exists.
        """
        sidebar_nav = self.driver.find_element(By.XPATH,
                                               '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav/div/aside/app-sidenav/nav/ul')
        self.assertTrue(sidebar_nav.is_displayed())

    def test_SideNavigationOptions(self):
        """
        Verify the options in the side navigation menu.
        """
        sidebar_nav = self.driver.find_element(By.XPATH,
                                               '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav/div/aside/app-sidenav/nav/ul')
        options = sidebar_nav.find_elements(By.TAG_NAME, "a")
        option_hrefs = [option.get_attribute("href") for option in options]
        expected_hrefs = ["/account", "/account/change-password"]
        for expected_href in expected_hrefs:
            self.assertIn(expected_href, option_hrefs)


    def test_FirstNameText(self):
        """
        Verify that the xpath contains the text "First Name".
        """
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[1]/formly-group/formly-field[1]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "First Name")]')
        self.assertTrue(text.is_displayed())

    def test_LastNameText(self):
        """
        Verify that the xpath contains the text "Last Name".
        """
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[1]/formly-group/formly-field[2]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "Last Name")]')
        self.assertTrue(text.is_displayed())

    def test_EmailText(self):
        """
        Verify that the xpath contains the text "Email".
        """
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[1]/formly-group/formly-field[3]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "Email")]')
        self.assertTrue(text.is_displayed())

    def test_RecoveryEmailText(self):
        """
        Verify that the xpath contains the text "Recovery Email".
        """
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[1]/formly-group/formly-field[4]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "Recovery Email")]')
        self.assertTrue(text.is_displayed())

    def test_PhoneNumberText(self):
        """
        Verify that the xpath contains the text "Phone Number".
        """
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[1]/formly-group/formly-field[5]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "Phone Number")]')
        self.assertTrue(text.is_displayed())

    def test_AdminText(self):
        """
        Verify that the xpath contains the text "Admin?".
        """
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[2]/formly-group/formly-field[1]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "Admin?")]')
        self.assertTrue(text.is_displayed())

    def test_PermissionsText(self):
        """
        Verify that the xpath contains the text "Permissions".
        """
        text = self.driver.find_element(By.XPATH,
                                        ' //*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[2]/formly-group/formly-field[2]/aus-form-input/div/label/span/div/aus-typography/p[contains(text(), "Permissions")]')
        self.assertTrue(text.is_displayed())

    def test_FirstNameField(self):
        """
        Verify that the field with ID 'firstName' exists and has the 'readonly' property.
        """
        field = self.driver.find_element(By.ID, "firstName")
        self.assertTrue(field.is_displayed() and field.get_attribute("readonly") == "true")

    def test_LastNameField(self):
        """
        Verify that the field with ID 'lastName' exists and has the 'readonly' property.
        """
        field = self.driver.find_element(By.ID, "lastName")
        self.assertTrue(field.is_displayed() and field.get_attribute("readonly") == "true")

    def test_EmailField(self):
        """
        Verify that the field with ID 'email' exists and has the 'readonly' property.
        """
        field = self.driver.find_element(By.ID, "email")
        self.assertTrue(field.is_displayed() and field.get_attribute("readonly") == "true")

    def test_RecoveryEmailField(self):
        """
        Verify that the field with ID 'recoveryEmail' exists and has the 'readonly' property.
        """
        field = self.driver.find_element(By.ID, "recoveryEmail")
        self.assertTrue(field.is_displayed() and field.get_attribute("readonly") == "true")

    def test_RadioButtonsDisplayed(self):
        """
        Verify that radio buttons are displayed
        """
        radio_buttons = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'input__control-wrapper')]")
        for button in radio_buttons:
            self.assertTrue(button.is_displayed())

    def test_PermissionsFormDisplayed(self):
        """
        Verify that the form in permissions is displayed
        """
        form = self.driver.find_element(By.XPATH,
                                        '//*[@id="mat-tab-content-0-0"]/div/form/formly-form/formly-field/formly-group/formly-field/formly-group/formly-field[2]/formly-group/formly-field[2]/aus-form-input')
        self.assertTrue(form.is_displayed())

    def test_PhoneNumberField(self):
        """
        Verify that the field with ID 'phoneNumber' exists and has the 'readonly' property.
        """
        field = self.driver.find_element(By.ID, "phoneNumber")
        self.assertTrue(field.is_displayed() and field.get_attribute("readonly") == "true")

    def test_ChangePasswordButton(self):
        """
        Verify that the button with class 'button button--secondary button--size-small ng-star-inserted' exists
        and clicking on it redirects to 'https://myportalaccountdev.aramark.com/account/change-password'.
        """
        button = self.driver.find_element(By.CSS_SELECTOR,
                                          ".button.button--secondary.button--size-small.ng-star-inserted")
        self.assertTrue(button.is_displayed())

        button.click()
        time.sleep(2)

        self.assertEqual(self.driver.current_url, "https://myportalaccountdev.aramark.com/account/change-password")



    def test_ChangePasswordButton(self):
        """
        Verify that the button with class 'button.button--primary-neutral.button--size-small.ng-star-inserted' is displayed,
        and it removes the 'readonly' attribute from the fields with IDs firstName, lastName, recoveryEmail, and phoneNumber.
        It also tests that the fields allow typing text.
        """
        button = self.driver.find_element(By.CSS_SELECTOR,
                                          ".button.button--primary-neutral.button--size-small.ng-star-inserted")
        self.assertTrue(button.is_displayed())

        firstName_field = self.driver.find_element(By.ID, "firstName")
        lastName_field = self.driver.find_element(By.ID, "lastName")
        recoveryEmail_field = self.driver.find_element(By.ID, "recoveryEmail")
        phoneNumber_field = self.driver.find_element(By.ID, "phoneNumber")

        self.assertTrue(firstName_field.get_attribute("readonly"))
        self.assertTrue(lastName_field.get_attribute("readonly"))
        self.assertTrue(recoveryEmail_field.get_attribute("readonly"))
        self.assertTrue(phoneNumber_field.get_attribute("readonly"))

        button.click()
        time.sleep(2)

        self.assertIsNone(firstName_field.get_attribute("readonly"))
        self.assertIsNone(lastName_field.get_attribute("readonly"))
        self.assertIsNone(recoveryEmail_field.get_attribute("readonly"))
        self.assertIsNone(phoneNumber_field.get_attribute("readonly"))

        firstName_field.clear()
        firstName_field.send_keys("John")

        lastName_field.clear()
        lastName_field.send_keys("Doe")

        recoveryEmail_field.clear()
        recoveryEmail_field.send_keys("john.doe@example.com")

        self.assertEqual(firstName_field.get_attribute("value"), "John")
        self.assertEqual(lastName_field.get_attribute("value"), "Doe")
        self.assertEqual(recoveryEmail_field.get_attribute("value"), "john.doe@example.com")

    import time

    def test_CanceldButton(self):
        """
        Verify that the cancel button is displayed,
        and it discards the changes made in the inputs : firstName, lastName, recoveryEmail, and phoneNumber.

        """
        button = self.driver.find_element(By.CSS_SELECTOR,
                                          ".button.button--primary-neutral.button--size-small.ng-star-inserted")
        self.assertTrue(button.is_displayed())

        firstName_field = self.driver.find_element(By.ID, "firstName")
        lastName_field = self.driver.find_element(By.ID, "lastName")
        recoveryEmail_field = self.driver.find_element(By.ID, "recoveryEmail")
        phoneNumber_field = self.driver.find_element(By.ID, "phoneNumber")

        self.assertTrue(firstName_field.get_attribute("readonly"))
        self.assertTrue(lastName_field.get_attribute("readonly"))
        self.assertTrue(recoveryEmail_field.get_attribute("readonly"))
        self.assertTrue(phoneNumber_field.get_attribute("readonly"))

        original_firstName_value = firstName_field.get_attribute("value")
        original_lastName_value = lastName_field.get_attribute("value")
        original_recoveryEmail_value = recoveryEmail_field.get_attribute("value")
        original_phoneNumber_value = phoneNumber_field.get_attribute("value")

        button.click()
        time.sleep(2)

        self.assertIsNone(firstName_field.get_attribute("readonly"))
        self.assertIsNone(lastName_field.get_attribute("readonly"))
        self.assertIsNone(recoveryEmail_field.get_attribute("readonly"))
        self.assertIsNone(phoneNumber_field.get_attribute("readonly"))

        firstName_field.clear()
        firstName_field.send_keys("John")

        lastName_field.clear()
        lastName_field.send_keys("Doe")

        recoveryEmail_field.clear()
        recoveryEmail_field.send_keys("john.doe@example.com")

        self.assertEqual(firstName_field.get_attribute("value"), "John")
        self.assertEqual(lastName_field.get_attribute("value"), "Doe")
        self.assertEqual(recoveryEmail_field.get_attribute("value"), "john.doe@example.com")

        cancel_button = self.driver.find_element(By.CSS_SELECTOR,
                                                 ".button.button--size-small.button--tertiary.ng-star-inserted")
        cancel_button.click()
        time.sleep(2)

        self.assertTrue(firstName_field.get_attribute("readonly"))
        self.assertTrue(lastName_field.get_attribute("readonly"))
        self.assertTrue(recoveryEmail_field.get_attribute("readonly"))
        self.assertTrue(phoneNumber_field.get_attribute("readonly"))

        self.assertEqual(firstName_field.get_attribute("value"), original_firstName_value)
        self.assertEqual(lastName_field.get_attribute("value"), original_lastName_value)
        self.assertEqual(recoveryEmail_field.get_attribute("value"), original_recoveryEmail_value)
        self.assertEqual(phoneNumber_field.get_attribute("value"), original_phoneNumber_value)

    def test_SaveChangesButton(self):
        from faker import Faker
        """
        Verify that clicking on the button Save Changes saves the changes
        and validates that the edited information is updated in the fields
        """
        faker = Faker()

        edit_button = self.driver.find_element(By.CSS_SELECTOR,
                                               ".button.button--primary-neutral.button--size-small.ng-star-inserted")
        edit_button.click()
        time.sleep(2)

        save_button = self.driver.find_element(By.CSS_SELECTOR,
                                               ".button.button--primary-brand.button--size-small.ng-star-inserted")
        self.assertTrue(save_button.is_displayed())

        firstName_field = self.driver.find_element(By.ID, "firstName")
        lastName_field = self.driver.find_element(By.ID, "lastName")
        recoveryEmail_field = self.driver.find_element(By.ID, "recoveryEmail")
        phoneNumber_field = self.driver.find_element(By.ID, "phoneNumber")

        original_firstName_value = firstName_field.get_attribute("value")
        original_lastName_value = lastName_field.get_attribute("value")
        original_recoveryEmail_value = recoveryEmail_field.get_attribute("value")

        new_firstName = faker.first_name()
        new_lastName = faker.last_name()
        new_recoveryEmail = faker.email()

        firstName_field.clear()
        firstName_field.send_keys(new_firstName)

        lastName_field.clear()
        lastName_field.send_keys(new_lastName)

        recoveryEmail_field.clear()
        recoveryEmail_field.send_keys(new_recoveryEmail)

        # Click on a radio button
        radio_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".radio-buttons__option.ng-star-inserted")
        radio_buttons[0].click()

        # Click on a checkbox
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[name='permissions-checkboxes']")
        checkboxes[0].click()

        save_button.click()
        time.sleep(2)

        self.assertEqual(firstName_field.get_attribute("value"), new_firstName)
        self.assertEqual(lastName_field.get_attribute("value"), new_lastName)
        self.assertEqual(recoveryEmail_field.get_attribute("value"), new_recoveryEmail)

        #validate the alert
        alert_message = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-my-account/app-page-layout/main/aus-alert/div/div/div[2]/aus-typography[2]/p')
        self.assertTrue(alert_message.is_displayed())
        self.assertEqual(alert_message.text, 'Your account has been updated.')









