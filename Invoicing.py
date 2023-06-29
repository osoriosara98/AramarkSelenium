import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import credentials
from commands import login, GetIntoInvoice

class EditAccountPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://myportallogindev.aramark.com/login"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "auth__logo")))
        login(self.driver)
        GetIntoInvoice(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/header/app-heading/div/div[1]/aus-typography/p')))

    def tearDown(self):
        self.driver.quit()

    def test_InvoicingText(self):
        """
        Verify that the text 'Invoicing' is present on the Invoicing page
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/header/app-heading/div/div[1]/aus-typography/p'))
        )
        text = element.text

        self.assertEqual(text, "Invoicing", "The text 'Invoicing' is not present on the Invoicing page")

    def test_amount_due_present(self):
        """
        Verify Amount Due is present
        """
        time.sleep(5)
        amount_due_element = self.driver.find_element(By.XPATH, '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[1]/aus-typography/p')
        self.assertEqual(amount_due_element.text, "Amount Due")

    def test_amountIsNumeric(self):
        """
        Verify the amount is a numeric value
        """
        amount_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[1]/div/div/div/div[1]/div/aus-typography/p'))
        )
        amount_text = amount_element.text

        # Remove comma and dollar sign
        amount_text = amount_text.replace(',', '').replace('$', '')

        # Verify numeric value
        try:
            amount_value = float(amount_text)
            self.assertGreaterEqual(amount_value, 0, "Amount is not a positive number")
        except ValueError:
            self.fail("Amount is not a numeric value")

    def test_startPaymentButtonDisplayed(self):
        """
        Verify Start payment button is displayed
        """
        start_payment_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[1]/div/div/div/div[2]/aus-button[1]/a'))
        )
        self.assertTrue(start_payment_button.is_displayed())

    def test_startPaymentButtonRedirects(self):
        """
        Verify Start payment button redirects to https://myportalaccountdev.aramark.com/invoicing/make-a-payment
        """
        start_payment_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[1]/div/div/div/div[2]/aus-button[1]/a'))
        )
        start_payment_button.click()
        self.assertEqual(self.driver.current_url, "https://myportalaccountdev.aramark.com/invoicing/make-a-payment")

    def test_viewOutstandingInvoicesButtonDisplayed(self):
        """
        Verify View Outstanding invoices button is displayed
        """
        view_invoices_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[1]/div/div/div/div[2]/aus-button[2]/a'))
        )
        self.assertTrue(view_invoices_button.is_displayed())

    def test_viewOutstandingInvoicesButtonRedirects(self):
        """
        Verify View Outstanding invoices button redirects to https://myportalaccountdev.aramark.com/invoicing/outstanding-invoices
        """
        view_invoices_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[1]/div/div/div/div[2]/aus-button[2]/a'))
        )
        view_invoices_button.click()
        self.assertEqual(self.driver.current_url,
                         "https://myportalaccountdev.aramark.com/invoicing/outstanding-invoices")
        time.sleep(3)

    def test_statementsButtonDisplayed(self):
        """
        Verify Statements button is displayed
        """
        statements_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[2]/div[1]/aus-typography/a'))
        )
        self.assertTrue(statements_button.is_displayed())

    def test_statementsButtonRedirects(self):
        """
        Verify Statements button redirects to https://myportalaccountdev.aramark.com/invoicing/statements
        """
        statements_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[2]/div[1]/aus-typography/a'))
        )
        statements_button.click()
        self.assertEqual(self.driver.current_url, "https://myportalaccountdev.aramark.com/invoicing/statements")
        time.sleep(3)

    def test_paymentHistoryButtonDisplayed(self):
        """
        Verify Payment history button is displayed
        """
        payment_history_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[2]/div[2]/aus-typography/a'))
        )
        self.assertTrue(payment_history_button.is_displayed())

    def test_paymentHistoryButtonRedirects(self):
        """
        Verify Payment history button redirects to https://myportalaccountdev.aramark.com/invoicing/payment-history
        """
        payment_history_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[1]/app-amount-due-card/div/app-box/div/div[2]/div[2]/aus-typography/a'))
        )
        payment_history_button.click()
        self.assertEqual(self.driver.current_url, "https://myportalaccountdev.aramark.com/invoicing/payment-history")
        time.sleep(3)

    def test_payment_methods_title_displayed(self):
        """
        Verify Payment Methods title is displayed
        """
        payment_methods_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/aus-typography/p'))
        )
        self.assertTrue(payment_methods_title.is_displayed())

    def test_icon_displayed(self):
        """
        Verify Icon is displayed
        """
        icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'empty-state__icon-template-wrapper'))
        )
        self.assertTrue(icon.is_displayed())

    def test_no_stored_payment_methods_text_displayed(self):
        """
        Verify Text: "No stored payment methods" is displayed
        """
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/div/div/div[1]/aus-empty-state/div/aus-typography[1]/p'))
        )
        self.assertEqual(text.text, "No stored payment methods")

    def test_add_payment_method_text_displayed(self):
        """
        Verify text "Add a payment method or enroll in autopay to make paying your invoices faster and easier!" is displayed
        """
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/div/div/div[1]/aus-empty-state/div/aus-typography[2]/p'))
        )
        self.assertEqual(text.text,
                         "Add a payment method or enroll in autopay to make paying your invoices faster and easier!")

    def test_add_payment_method_button_displayed(self):
        """
        Verify that Add a payment method button is displayed
        """
        add_payment_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/div/div/div[2]/aus-button[1]/a'))
        )
        self.assertTrue(add_payment_button.is_displayed())

    def test_add_payment_method_button_redirects(self):
        """
        Verify that Add a payment method button redirects to https://myportalaccountdev.aramark.com/invoicing/payment-methods
        """
        add_payment_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/div/div/div[2]/aus-button[1]/a'))
        )
        add_payment_button.click()
        self.assertEqual(self.driver.current_url, "https://myportalaccountdev.aramark.com/invoicing/payment-methods")

    def test_enroll_auto_pay_button_displayed(self):
        """
        Verify that Enroll in auto pay button is displayed
        """
        enroll_auto_pay_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/div/div/div[2]/aus-button[2]/a'))
        )
        self.assertTrue(enroll_auto_pay_button.is_displayed())

    def test_enroll_auto_pay_button_redirects(self):
        """
        Verify that Enroll in auto pay button redirects to https://myportalaccountdev.aramark.com/invoicing/auto-pay
        """
        enroll_auto_pay_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[2]/app-payment-method-card/div/app-box/div/div/div/div/div[2]/aus-button[2]/a'))
        )
        enroll_auto_pay_button.click()
        self.assertEqual(self.driver.current_url, "https://myportalaccountdev.aramark.com/invoicing/auto-pay")

    def test_need_help_title_displayed(self):
        """
        Verify that Need help? Title is displayed
        """
        need_help_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[3]/app-support-card/div/app-box/div/div[1]/div/div/div[1]/div[2]/aus-typography[1]/p'))
        )
        self.assertTrue(need_help_title.is_displayed())

    def test_customer_support_text_displayed(self):
        """
        Verify that text: "Our customer support team is ready to help you with any request." is displayed
        """
        customer_support_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[3]/app-support-card/div/app-box/div/div[1]/div/div/div[1]/div[2]/aus-typography[2]/p'))
        )
        self.assertEqual(customer_support_text.text, "Our customer support team is ready to help you with any request.")

    def test_faq_button_displayed(self):
        """
        Verify that FAQ button is displayed
        """
        faq_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[3]/app-support-card/div/app-box/div/div[1]/div/div/div[2]/aus-button/a'))
        )
        self.assertTrue(faq_button.is_displayed())

    def test_faq_button_redirects(self):
        """
        Verify that FAQ button redirects to https://myportalaccountdev.aramark.com/invoicing/frequently-asked-questions
        """
        faq_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[3]/app-support-card/div/app-box/div/div[1]/div/div/div[2]/aus-button/a'))
        )
        faq_button.click()
        self.assertEqual(self.driver.current_url,
                         "https://myportalaccountdev.aramark.com/invoicing/frequently-asked-questions")

    def test_email_button_displayed(self):
        """
        Verify that Email button is displayed
        """
        email_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[3]/app-support-card/div/app-box/div/div[2]/div/aus-typography/a'))
        )
        self.assertTrue(email_button.is_displayed())

    def test_img_displayed(self):
        """
        Verify that img is displayed
        """
        img = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/app-root/portal-root/mat-sidenav-container/mat-sidenav-content/div/div/app-invoicing/app-page-layout/main/div/div/div[3]/app-support-card/div/app-box/div/div[1]/div/div/div[1]/div[1]'))
        )
        self.assertTrue(img.is_displayed())

if __name__ == '__main__':
    unittest.main()


