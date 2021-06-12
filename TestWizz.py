from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time



valid_name = "Anna"
valid_lastname = "Nowak"
valid_gender = "female"
valid_country_code = "+48"
valid_phone_number = "123456789"
valid_password = "Nowak123"
valid_country = "Algeria"

invalid_email = "olao2.pl"

class WizzairRegistration(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://wizzair.com/pl-pl')

    def tearDown(self):
        self.driver.quit()

    def testInvalidEmail(self):

        driver = self.driver

        driver.implicitly_wait(90)

        zaloguj_btn = driver.find_element_by_css_selector('#app > div > header > div.header__inner > div > nav > ul > li:nth-child(6) > button')
        print(type(zaloguj_btn))

        zaloguj_btn.click()

        driver.find_element_by_xpath('//button[@data-test="registration"]').click()

        name_input = driver.find_element_by_name("firstName")
        name_input.send_keys(valid_name)

        lastname_input = driver.find_element_by_name("lastName")
        lastname_input.send_keys(valid_lastname)

        if valid_gender == "female":
            lastname_input.click()
            female = driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]')
            female.click()
        else:
            name_input.click()
            male = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            male.click()

        driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        cc_input = driver.find_element_by_name('phone-number-country-code')
        cc_input.send_keys(valid_country_code, Keys.RETURN)

        driver.find_element_by_name('phoneNumberValidDigits').send_keys(valid_phone_number)

        driver.find_element_by_name('email').send_keys(invalid_email)

        driver.find_element_by_name('password').send_keys(valid_password)

        nationality_input = driver.find_element_by_name('country-select')
        nationality_input.click()

        countries = driver.find_elements_by_xpath('//div[@class="register-form__country-container__locations"]/label')
        for label  in countries:

            country =label.find_element_by_tag_name("strong")
            if country.get_attribute("textContent") == valid_country:

                country.location_once_scrolled_into_view

                country.click()

                break

        error_messages = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')

        visible_error_messages = []

        for error in error_messages:

            if error.is_displayed():

                visible_error_messages.append(error)

        assert len(visible_error_messages) == 1
        
        assert visible_error_messages[0].text == "Nieprawidłowy adres e-mail"


        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
